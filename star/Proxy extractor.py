import re
import requests
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
def extract_proxies_from_text(text):

    proxy_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{2,5})')
    proxies = proxy_pattern.findall(text)
    return [f"{ip}:{port}" for ip, port in proxies]

def extract_proxies_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return extract_proxies_from_text(response.text)
    except requests.RequestException as e:
        print(Fore.RED + f"Erreur{e}")
        return []


if __name__ == "__main__":
    url = input(Fore.CYAN + "URL (https://free-proxy-list.net): " + Fore.WHITE)
    proxies = extract_proxies_from_url(url)

    if proxies:
        print(Fore.CYAN + "Proxys extraits :")
        print(Fore.WHITE + " ")
        for proxy in proxies:
            print(proxy)
    else:
        print("Aucun proxy trouvé.")

input(Fore.RED + "PRESS ENTER TO EXIT...")
