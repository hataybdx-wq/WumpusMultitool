import webbrowser
import requests
from pystyle import Center, Colorate, Colors, Anime
import colorama
import os
from colorama import Fore

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

try:
    IdBot = int(input(Fore.BLUE + "ID bot -> " + Fore.WHITE))
    invite_url = f'https://discord.com/oauth2/authorize?client_id={IdBot}&scope=bot&permissions=8'
    response = requests.get(invite_url)
    print(f"Invite Url: {invite_url} (status: {response.status_code})")

    choice = input(Fore.CYAN + "Open in browser ? (y/n) -> ")
    if choice.lower() in ['y', 'yes']:
        webbrowser.open_new_tab(invite_url)
except Exception as e:
    print(f"Error: {e}")