from pystyle import Center, Colorate, Colors, Anime
import colorama
import os
import requests

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

def Error(e):
    print(colorama.Fore.RED + f"Error: {e}")
    exit()

def leaver(guilds, token):
    for guild in guilds:
        try:
            response = requests.delete(f'https://discord.com/api/v8/users/@me/guilds/{guild["id"]}', headers={'Authorization': token})
            if response.status_code == 204 or response.status_code == 200:
                print(colorama.Fore.GREEN + f"Status: Leave Server: {guild['name']}")
            elif response.status_code == 400:
                response = requests.delete(f'https://discord.com/api/v8/guilds/{guild["id"]}', headers={'Authorization': token})
                if response.status_code == 204 or response.status_code == 200:
                    print(colorama.Fore.GREEN + f"Status: Leave Server: {guild['name']}")
            else:
                print(colorama.Fore.RED + f"Status: Error {response.status_code} Server: {guild['name']}")
        except Exception as e:
            print(colorama.Fore.RED + f"Status: Error: {e}")

try:
    token = input("Enter your token: ")

    guilds_id = requests.get("https://discord.com/api/v8/users/@me/guilds", headers={'Authorization': token}).json()
    if not guilds_id:
        print(colorama.Fore.YELLOW + "No Server found.")
        exit()

    for guild in [guilds_id[i:i+3] for i in range(0, len(guilds_id), 3)]:
        leaver(guild, token)

except Exception as e:
    Error(e)
