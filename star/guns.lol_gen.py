import requests
from bs4 import BeautifulSoup
import random
import string
import colorama
from colorama import Fore
import os
import time
import keyboard
from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore
import os
pause = False
def toggle_pause():
    global pause
    pause = not pause  # Inverser l'état de pause
    if pause:
        print(Fore.YELLOW + "\nPause activée. Appuyez sur F6 pour reprendre.\n")
    else:
        print(Fore.GREEN + "\nReprise...\n")

keyboard.add_hotkey("F6", toggle_pause)  # Associer la touche F6 à la fonction toggle_pause


os.system('cls')
def is_username_taken(username):
    url = f"https://guns.lol/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        claim_button = soup.find("a", href=f"/register?claim={username}")
        if claim_button:
            return False
        return True  
    elif response.status_code == 404:
        return False 
    else:
        return None 

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def get_random_word():
    common_words = [
        "apple", "banana", "orange", "house", "table", "chair", "window", "computer", "phone", "light", 
        "car", "tree", "river", "mountain", "book", "paper", "bottle", "glass", "pencil", "keyboard", 
        "monitor", "mouse", "television", "radio", "music", "guitar", "violin", "piano", "drum", "ocean",
        "school", "teacher", "student", "chalk", "blackboard", "notebook", "backpack", "lunch", "soccer", "tennis",
        "basketball", "hockey", "baseball", "football", "volleyball", "shoes", "socks", "pants", "shirt", "jacket",
        "hat", "cap", "gloves", "scarf", "watch", "clock", "calendar", "map", "passport", "ticket", "train",
        "airplane", "airport", "bicycle", "motorcycle", "bus", "subway", "tram", "taxi", "restaurant", "menu"
    ] * 4 
    return random.choice(common_words)

def get_random_name():
    common_names = [
        "alice", "bob", "charlie", "david", "emma", "frank", "grace", "henry", "irene", "jack", "karen", "leo",
        "michael", "nancy", "oliver", "paul", "quentin", "rachel", "steve", "tina", "ursula", "victor", "william",
        "xavier", "yvonne", "zach", "adam", "brian", "carl", "daniel", "edward", "felix", "george", "hannah"
    ] * 4 
    return random.choice(common_names)

if __name__ == "__main__":     
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
[1] 3 Letter  [2] 2 Letter  [3] Everyday words  [4] Well-known names  [5] Custom                          
"""))                                           
                                                                                                                                                                                         
                                                                                                                                                                                        
choice = input(Fore.WHITE + "Your Choice: " + Fore.MAGENTA)

if choice == "1":
        count = int(input(Fore.WHITE + "How many: " + Fore.MAGENTA))
        usernames = [generate_random_string(3) for _ in range(count)]
elif choice == "2":
        count = int(input(Fore.WHITE + "How many: " + Fore.MAGENTA))
        usernames = [generate_random_string(2) for _ in range(count)]
elif choice == "3":
        count = int(input(Fore.WHITE + "How many: " + Fore.MAGENTA))
        usernames = [get_random_word() for _ in range(count)]
elif choice == "4":
        count = int(input(Fore.WHITE + "How many: " + Fore.MAGENTA))
        usernames = [get_random_name() for _ in range(count)]
elif choice == "5":
        usernames = input(Fore.WHITE + "Usernames: " + Fore.MAGENTA)
else:
        print(Fore.RED + "invalid.")
        exit()
    
for username in usernames:
    while pause:
        print(Fore.YELLOW + "\nEn pause... Appuyez sur F6 pour continuer.\n", end="\r")
        time.sleep(0.5) 

    result = is_username_taken(username)
    if result is True:
        print(Fore.RED + f"'{username}' taken.")
    elif result is False:
        print(Fore.GREEN + f"'{username}' available.")
    else:
        print(Fore.RED + f"ERROR'{username}' Use VPN Or change VPN server.")
