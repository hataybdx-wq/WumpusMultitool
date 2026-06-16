from pystyle import Center, Colorate, Colors, Anime
import colorama
import os
import requests
import time

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

def ErrorNumber():
    print(colorama.Fore.RED + "Invalid number input.")
    exit()

def ErrorToken():
    print(colorama.Fore.RED + "Invalid token.")
    exit()

def ChangeStatus(token, statues):
    headers = {'Authorization': token, 'Content-Type': 'application/json'}

    while True:
        for i in range(len(statues)):
            custom_status = {"custom_status": {"text": statues[i]}}
            try:
                r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=custom_status)
                print(colorama.Fore.GREEN + f"Changed Status Discord: {statues[i]}")
                time.sleep(5)
            except Exception as e:
                print(colorama.Fore.RED + f"Error changing Status Discord: {statues[i]}")
                time.sleep(5)

try:
    token = input("Enter your token: ")
    try:
        statue_number = int(input("How many statuses do you want to cycle (max 4) -> "))
    except:
        ErrorNumber()

    statues = []

    if statue_number >= 1 and statue_number <= 4:
        for loop in range(0, statue_number):
            choice = str(input(f"Custom Status {loop+1} -> "))
            statues.append(choice)
    else:
        ErrorNumber()

    ChangeStatus(token, statues)

except Exception as e:
    print(colorama.Fore.RED + f"Error: {e}")
