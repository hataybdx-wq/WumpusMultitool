from pystyle import Center, Colorate, Colors, Anime
import colorama
import os
import requests
import time
import random

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

colorama.init(autoreset=True)

def ErrorToken():
    print(colorama.Fore.RED + "Invalid Token.")
    exit()

def ErrorNumber():
    print(colorama.Fore.RED + "Invalid number of cycles.")
    exit()

def ChangeLanguage(token, amount):
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)

    if r.status_code == 200:
        for i in range(amount):
            try:
                time.sleep(0.6)
                random_language = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
                setting = {'locale': random_language}
                requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
                print(colorama.Fore.GREEN + f"Status: Changed Language: {random_language}")
            except Exception as e:
                print(colorama.Fore.RED + f"Status: Error Language: {random_language} Error: {e}")
        print(colorama.Fore.GREEN + "Finish.")
    else:
        ErrorToken()

try:
    token = input("Enter your Discord token: ")
    try:
        amount = int(input("Enter the number of cycles -> "))
    except:
        ErrorNumber()

    ChangeLanguage(token, amount)
except Exception as e:
    print(colorama.Fore.RED + f"Error: {e}")
