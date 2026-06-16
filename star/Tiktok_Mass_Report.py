import requests
import time
import colorama
from colorama import Fore
import re
from pystyle import Colors, Colorate
import os
from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore
import os
colorama.init()

session = requests.session()
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

acc = input(Fore.CYAN + "[Account URL]> ")

pattern = r'tiktok\.com/@([a-zA-Z0-9._]+)'
match = re.search(pattern, acc)
username = match.group(1) if match else ''
x = input(Fore.CYAN + '[Request URL]> ')
x2 = input(Fore.CYAN + '[Request URL 2]> ')
print("")

try:
    number_of_requests = int(input('[Report]> '))
    if number_of_requests <= 0:
        print(Fore.RED + "Please enter a positive integer.")
        exit()
except ValueError:
    print(Fore.RED + "Invalid input. Please enter a valid number.")
    exit()


print(" ")
os.system('cls')
print(Colorate.Horizontal(Colors.blue_to_cyan,"""
 /$$$$$$$  /$$$$$$$$ /$$       /$$   /$$  /$$$$$$   /$$$$$$ 
| $$__  $$| $$_____/| $$      | $$  | $$ /$$__  $$ /$$__  $$
| $$  \ $$| $$      | $$      | $$  | $$| $$  \__/| $$  \ $$
| $$$$$$$ | $$$$$   | $$      | $$  | $$| $$ /$$$$| $$$$$$$$
| $$__  $$| $$__/   | $$      | $$  | $$| $$|_  $$| $$__  $$
| $$  \ $$| $$      | $$      | $$  | $$| $$  \ $$| $$  | $$
| $$$$$$$/| $$$$$$$$| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$  | $$
|_______/ |________/|________/ \______/  \______/ |__/  |__/

                ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                ┃ Author : Ace | Adwares      ┃
                ┃ Discord: .gg/leak-internet  ┃
                ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                          
"""))
print(Colorate.Horizontal(Colors.blue_to_cyan,"""======================================================================================================================""",1))
print(" ")
for i in range(number_of_requests):
    try:
        req = session.post(x, x2)
        print(Colorate.Horizontal(Colors.green_to_cyan,f"Report : {i + 1} | Status Code {req.status_code} | Reported successfully send to {username}"))
    except requests.exceptions.RequestException as e:
        print(f"Error occurred during request {i + 1}: {e}")
    time.sleep(2)

print("Successfully report!")
input(Fore.RED + 'Press enter to exit..')
