import sys
import time
import colorama
from colorama import Fore, Back, Style
import webbrowser
import requests
import json
import os
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

print(Fore.WHITE + " ")

def send_webhook(url, data):
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        response.raise_for_status()
        print(Fore.GREEN + "Webhook envoyé avec succès ! Réponse: " + response.text)
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Erreur lors de l'envoi du webhook: {e}")

def delete_webhook(url):
    try:
        response = requests.delete(url)
        response.raise_for_status()
        print(Fore.GREEN + "Webhook supprimé avec succès !")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Erreur lors de la suppression du webhook: {e}")


print(Fore.BLUE + "Drag your files in this website to scan and pick webhook.")
choice1 = input(Fore.WHITE + "You want open the website? (y/n): ")

if choice1 == "y":
    webbrowser.open("https://www.uncoverit.org")
    print(Fore.GREEN + "succes opened.")
    webhook_url = input("Enter Webhook URL :")
    message = input("Enter your username :")
    payload = {
            "content": "This webhook has been fucked by " + message + "[@everyone @here] Hiro de puta!!",
            "username": "Funcover | BY Ace"
        }
    for _ in range(5):
        send_webhook(webhook_url, payload)
        
    delete_webhook(webhook_url)
    print(Fore.CYAN + "Succes Fucked ! Thx!")
    time.sleep(3)
    os.system('exit')
if choice1 == "n":
    print(Fore.GREEN + "Succes !")
    webhook_url = input(Fore.BLUE + "Enter Webhook URL :" + Fore.WHITE)
    message = input(Fore.BLUE + "Enter your username :" + Fore.WHITE)
    payload = {
            "content": "This webhook has been fucked by" + message + "[@everyone @here] Hiro de puta!!",
            "username": "Funcover | BY Ace"
        }
    for _ in range(5):
        send_webhook(webhook_url, payload)

    delete_webhook(webhook_url)
    print(Fore.CYAN + "Succes Fucked ! Thx!")
    time.sleep(3)
    os.system('exit')
    sys.exit()