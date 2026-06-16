import requests
import colorama
import os
import threading
from threading import Thread
from colorama import Fore, Style
import requests
import time
import threading
from pystyle import Colors
import requests
from pystyle import Colors
import colorama
from colorama import Fore
import os
import subprocess
import time
import webbrowser
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
s = Style.BRIGHT
print(f"""{s+Fore.BLUE}
{s+Fore.BLUE} 1 > {Fore.RESET}Illegal Content
{s+Fore.BLUE} 2 > {Fore.RESET}Harrassment
{s+Fore.BLUE} 3 > {Fore.RESET}Spam Or Phishing Links
{s+Fore.BLUE} 4 > {Fore.RESET}Self Harm
{s+Fore.BLUE} 5 > {Fore.RESET}NSFW Content
""")

token = input(f"{s+Fore.BLUE} > Token{Fore.RESET}: ")
headers = {'Authorization': token, 'Content-Type':  'application/json'}  
r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)

if r.status_code == 200:
        pass
else:
        print(f"{s+Fore.RED} > Invalid Token")
        print(f"{s+Fore.RED} > Press Anything To Exit. . .")
        input()

reason1 = input(f"{s+Fore.BLUE} > Choose A Reason{Fore.RESET}: ")
guild_id1 = input(f"{s+Fore.BLUE} > Server ID{Fore.RESET}: ")
channel_id1 = input(f"{s+Fore.BLUE} > Channel ID{Fore.RESET}: ")
message_id1 = input(f"{s+Fore.BLUE} > Message ID{Fore.RESET}: ")

def MassReport():
  global sent
  headers = {
        'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
        'Authorization': token,
        'Content-Type': 'application/json'
      }

  payload = {
    'channel_id': channel_id1,
    'guild_id': guild_id1,
    'message_id': message_id1,
    'reason': reason1
  }

  while True:
    r = requests.post('https://discord.com/api/v9/report', headers=headers, json=payload)
    if r.status_code == 201:
      print(f"{s+Fore.BLUE} > {Fore.RESET}Sent Report ID {message_id1}")
      os.system(f'Sending Reports. . .')
      
    elif r.status_code == 401:
      print(f"{Fore.RED} > Invalid token")
      input()
      exit()
    else:
      print(f"{Fore.RED} > Error")


print()
for i in range(500, 1000):
    Thread(target=MassReport).start()
