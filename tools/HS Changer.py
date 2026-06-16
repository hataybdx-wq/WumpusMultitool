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

import colorama
import requests
import os

colorama.init(autoreset=True)

def ErrorToken():
    print(colorama.Fore.RED + "Invalid Token.")
    exit()

def ErrorChoice():
    print(colorama.Fore.RED + "Invalid Choice.")
    exit()

def ChangeHouse(token, house_choice):
    response = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
    if response.status_code != 200:
        ErrorToken()

    headers = {'Authorization': token, 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}

    if house_choice in ["1", "01"]:
        payload = {'house_id': 1}
    elif house_choice in ["2", "02"]:
        payload = {'house_id': 2}
    elif house_choice in ["3", "03"]:
        payload = {'house_id': 3}
    else:
        ErrorChoice()

    r = requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    if r.status_code == 204:
        print(colorama.Fore.GREEN + "Hypesquad house changed.")
    else:
        print(colorama.Fore.RED + "Hypesquad house has not changed.")

try:
    token = input("Enter your token: ")
    print("""
    01 Bravery
    02 Brilliance
    03 Balance
    """)

    house = input("Choose house -> ").lstrip("0")

    ChangeHouse(token, house)

except Exception as e:
    print(colorama.Fore.RED + f"Error: {e}")
