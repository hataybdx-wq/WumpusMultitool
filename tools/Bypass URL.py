import urllib.parse
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
def encoder_url():
    url = input("URL: ").strip()

    if url.startswith("https://"):
        prefix = "https://"
        rest = url[len(prefix):]
    else:
        print("You dont have in link :'https://'")
        return

    encoded_rest = ''
    for char in rest:
        if char.isalnum():
            encoded_rest += f'%{ord(char):02x}'
        else:
            encoded_rest += char

    encoded_url = prefix + encoded_rest

    print("\nURL encodée :")
    print(encoded_url)

encoder_url()
input("Press Enter to exit...")
