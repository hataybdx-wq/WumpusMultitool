# NAME = "Flooder"

import sys
import asyncio
import aiohttp
import random
import threading
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QLineEdit, QPushButton, QLabel
)
from PyQt5.QtCore import Qt

class MessageSender:
    def __init__(self, tokens, channel_ids, messages, send_all, mentions, mode="normal", callback=None):
        self.tokens = [t.strip() for t in tokens if t.strip()]
        self.channel_ids = [c.strip() for c in channel_ids if c.strip()]
        self.messages = messages
        self.send_all = send_all
        self.mode = mode  # normal, explosion, spam
        self.mentions = mentions
        self.callback = callback
        self._running = True
        self.tasks = []
        self.session = None
        self.delay = 0.2 if mode != "spam" else 0.5

    def stop(self):
        self._running = False
        for t in self.tasks:
            if not t.done():
                t.cancel()
        if self.session and not self.session.closed:
            async def close_session():
                await self.session.close()
            try:
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    asyncio.run_coroutine_threadsafe(close_session(), loop)
                else:
                    loop.run_until_complete(close_session())
            except:
                pass
        if self.callback:
            self.callback("🛑 Tous les envois ont été arrêtés immédiatement.")

    def format_mentions(self):
        return " ".join([f"<@{id.strip()}>" for id in self.mentions if id.strip()])

    def bypass_antispam(self, content):
        invisible_chars = ['\u200b', '\u200c', '\u200d']
        return content + random.choice(invisible_chars)

    async def send_message(self, token, channel_id, content):
        if not self._running:
            return
        full_content = f"{content} {self.format_mentions()}".strip()
        full_content = self.bypass_antispam(full_content)
        url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
        headers = {"Authorization": token, "Content-Type": "application/json"}
        json_data = {"content": full_content}

        try:
            async with self.session.post(url, headers=headers, json=json_data) as resp:
                if not self._running:
                    return
                if resp.status == 429:
                    try:
                        data = await resp.json()
                        retry = data.get("retry_after", self.delay)
                        if self.callback:
                            self.callback(f"⚠️ Rate limit {token[:10]}..., retry {retry}s")
                        if self._running:
                            await asyncio.sleep(retry)
                            if self._running:
                                await self.send_message(token, channel_id, content)
                    except:
                        return
                elif resp.status in (200, 201):
                    if self.callback:
                        self.callback(f"✅ Envoyé ({token[:10]}...) : {content[:50]}")
                else:
                    text = await resp.text()
                    if self.callback:
                        self.callback(f"❌ Erreur {resp.status} ({token[:10]}...) : {text}")
        except asyncio.CancelledError:
            return
        except Exception as e:
            if self.callback:
                self.callback(f"❌ Exception {token[:10]}...: {str(e)}")

    async def send_all_messages_token(self, token):
        while self._running:
            for channel_id in self.channel_ids:
                for msg in self.messages:
                    if not self._running:
                        break
                    await self.send_message(token, channel_id, msg)
                    if not self._running:
                        break
                    await asyncio.sleep(self.delay)

    async def main(self):
        async with aiohttp.ClientSession() as self.session:
            if self.mode in ["explosion", "spam"]:
                self.tasks = [asyncio.create_task(self.send_all_messages_token(token)) for token in self.tokens]
                await asyncio.gather(*self.tasks, return_exceptions=True)
            else:
                for token in self.tokens:
                    for channel_id in self.channel_ids:
                        if self.send_all:
                            for msg in self.messages:
                                if not self._running:
                                    break
                                await self.send_message(token, channel_id, msg)
                        else:
                            if self._running:
                                await self.send_message(token, channel_id, self.messages[0])

    def start(self):
        try:
            asyncio.run(self.main())
        except Exception as e:
            if self.callback:
                self.callback(f"❌ Exception fatale: {str(e)}")

class ANCord(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WumpusCord")
        self.resize(950, 850)
        self.sender_thread = None
        self.sender = None
        self.set_dark_theme()

        layout = QVBoxLayout()
        title = QLabel("Discord.gg/Datas Cord")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size:20px;font-weight:bold;color:#00b4d8;padding:10px;border-bottom:2px solid #00b4d8;")
        layout.addWidget(title)

        self.token_inputs = []
        for i in range(1, 5):
            lbl = QLabel(f"Token {i} :")
            inp = QLineEdit()
            inp.setEchoMode(QLineEdit.Password)
            layout.addWidget(lbl)
            layout.addWidget(inp)
            self.token_inputs.append(inp)

        self.channel_label = QLabel("IDs des salons (un par ligne) :")
        self.channel_input = QTextEdit()
        self.channel_input.setPlaceholderText("123456789012345678\n987654321098765432")
        layout.addWidget(self.channel_label)
        layout.addWidget(self.channel_input)

        self.mention_label = QLabel("IDs à mentionner (un par ligne) :")
        self.mention_input = QTextEdit()
        self.mention_input.setPlaceholderText("123456789012345678\n987654321098765432")
        layout.addWidget(self.mention_label)
        layout.addWidget(self.mention_input)

        self.messages_input = QTextEdit()
        self.messages_input.setPlaceholderText("Écris un ou plusieurs messages (liens inclus), un par ligne")
        layout.addWidget(self.messages_input)

        buttons_layout = QHBoxLayout()
        self.send_single_btn = QPushButton("Envoyer 1er message")
        self.send_all_btn = QPushButton("Envoyer tous")
        self.explosion_btn = QPushButton("💥 EXPLOSION")
        self.spam_btn = QPushButton("⚡ SPAM SAFE")
        self.stop_btn = QPushButton("🛑 STOP")
        buttons_layout.addWidget(self.send_single_btn)
        buttons_layout.addWidget(self.send_all_btn)
        buttons_layout.addWidget(self.explosion_btn)
        buttons_layout.addWidget(self.spam_btn)
        buttons_layout.addWidget(self.stop_btn)
        layout.addLayout(buttons_layout)

        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setPlaceholderText("Logs d’envoi en temps réel...")
        layout.addWidget(self.log_output)

        self.setLayout(layout)

        # Connections
        self.send_single_btn.clicked.connect(lambda: self.start_sender(send_all=False, mode="normal"))
        self.send_all_btn.clicked.connect(lambda: self.start_sender(send_all=True, mode="normal"))
        self.explosion_btn.clicked.connect(lambda: self.start_sender(send_all=True, mode="explosion"))
        self.spam_btn.clicked.connect(lambda: self.start_sender(send_all=True, mode="spam"))
        self.stop_btn.clicked.connect(self.stop_sender)

    def set_dark_theme(self):
        self.setStyleSheet("""
            QWidget {background-color:#0e0e0e;color:white;font-family:Arial;}
            QLabel {font-weight:bold;margin-top:5px;}
            QLineEdit,QTextEdit {background-color:#1a1a1a;border:1px solid #444;border-radius:8px;padding:5px;color:white;}
            QLineEdit:focus,QTextEdit:focus {border:1px solid #00b4d8;background-color:#222;}
            QPushButton {background-color:#1f1f1f;border:1px solid #444;border-radius:8px;padding:8px;font-weight:bold;color:white;}
            QPushButton:hover {background-color:#00b4d8;color:black;}
            QPushButton:pressed {background-color:#0096c7;}
        """)

    def log(self, text):
        self.log_output.append(text)

    def get_tokens(self):
        return [inp.text().strip() for inp in self.token_inputs if inp.text().strip()]

    def get_channel_ids(self):
        return [c.strip() for c in self.channel_input.toPlainText().split("\n") if c.strip()]

    def get_mentions(self):
        return [m.strip() for m in self.mention_input.toPlainText().split("\n") if m.strip()]

    def get_messages(self):
        return [m.strip() for m in self.messages_input.toPlainText().split("\n") if m.strip()]

    def start_sender(self, send_all, mode="normal"):
        tokens = self.get_tokens()
        channel_ids = self.get_channel_ids()
        mentions = self.get_mentions()
        messages = self.get_messages()
        if not tokens or not channel_ids or not messages:
            self.log("⚠ Remplis au moins 1 token, 1 salon et message(s).")
            return

        self.sender = MessageSender(tokens, channel_ids, messages, send_all, mentions, mode, self.log)
        self.sender_thread = threading.Thread(target=self.sender.start, daemon=True)
        self.sender_thread.start()
        self.log(f"🚀 Envoi mode {mode.upper()} démarré...")

    def stop_sender(self):
        if self.sender:
            self.sender.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ANCord()
    win.show()
    sys.exit(app.exec_())

