import time
import telebot
from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore
import os

os.system('cls')
print(Colorate.Horizontal(Colors.blue_to_cyan,"""
▄▄▄▄  ▄▄▄  ▄▄▄▄                                 
▀███  ███  ███▀                                 
 ███  ███  ███ ██ ██ ███▄███▄ ████▄ ██ ██ ▄█▀▀▀ 
 ███▄▄███▄▄███ ██ ██ ██ ██ ██ ██ ██ ██ ██ ▀███▄ 
  ▀████▀████▀  ▀██▀█ ██ ██ ██ ████▀ ▀██▀█ ▄▄▄█▀ 
                              ██                
                              ▀▀                

                ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                ┃ Author : Wumpus             ┃
                ┃ Discord: .gg/datas          ┃
                ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                          
"""))
def spam_telegram_channel():
    bot_token = input("Telegram bot token: ")
    channel_id = input("Entrez l'ID du canal Telegram: ")
    message = input("Entrez le message à envoyer: ")
    count = int(input("Combien de fois envoyer le message? "))
    delay = float(input("Délai entre les messages (en secondes)? "))
    
    bot = telebot.TeleBot(bot_token)
    
    for i in range(count):
        try:
            bot.send_message(chat_id=channel_id, text=message)
            print(f"Message {i+1}/{count} envoyé.")
            time.sleep(delay)
        except Exception as e:
            print(f"Erreur lors de l'envoi du message: {e}")
            break
    
    print("Spam terminé.")

if __name__ == "__main__":
    spam_telegram_channel()
