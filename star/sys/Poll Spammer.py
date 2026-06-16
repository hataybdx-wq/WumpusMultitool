import requests
import random
import threading
import time
import os
from itertools import cycle
from colorama import Fore 
import requests
import random
import os
import asyncio
import aiohttp
import os
import json
import asyncio
import websockets
from pystyle import Center, Colorate, Colors, Anime
import colorama
import os
import requests
from datetime import datetime, timezone


def read_tokens_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"{Fore.RED}Error: The file '{file_path}' was not found!")
        return []


def read_tokens_from_folder(folder_path):
    tokens = []
    try:
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                tokens.extend(read_tokens_from_file(file_path))
    except FileNotFoundError:
        print(f"{Fore.RED}Error: The folder '{folder_path}' was not found!")
    return tokens

tokens = read_tokens_from_file("input/tokens.txt")

os.system('cls' if os.name == 'nt' else 'clear')

os.system('cls' if os.name == 'nt' else 'clear')
print(Colorate.Vertical(Colors.yellow_to_red, """
                                                                    
                    (       (                   )\ )         (     
                     ( )\    ( )\  (  (  (     )  (()/(   ) (   )\ )  
                    )((_)  ))((_)))\ )\))( ( /(   /(_)| /( )\ (()/(  
                   ((_)_  /((_) /((_|(_))\ )(_)) (_)) )(_)|(_) ((_)) 
                    | _ )(_))| (_))( (()(_|(_)_  | _ ((_)_ (_) _| |  
                    | _ \/ -_) | || / _` |/ _` | |   / _` || / _` |  
                    |___/\___|_|\_,_\__, |\__,_| |_|_\__,_||_\__,_|  
                                     |___/     
                                               
                ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                ┃ Author : Ace | Adwares      ┃
                ┃ Discord: .gg/leak-internet  ┃
                ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛     
         
"""))

class PollSpammer:
    @staticmethod
    def gen_nonce():
        return ''.join(str(random.randint(0, 9)) for _ in range(19))

    @staticmethod
    def get_cookies():
        try:
            response = requests.get("https://discord.com/api/v9/experiments")
            if response.status_code == 200:
                cookies = response.cookies.get_dict()
                return "; ".join([f"{key}={value}" for key, value in cookies.items()])
            else:
                print(f"Failed to fetch cookies: {response.status_code} > {response.text}")
                return ""
        except requests.RequestException as e:
            print(f"Error fetching cookies: {e}")
            return ""

    @staticmethod
    def poll_spam(token, nonce, cookies, chan, mess):
        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "cs,en-US;q=0.9",
            "authorization": token,
            "content-type": "application/json",
            "cookie": cookies,
            "origin": "https://discord.com",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9175 Chrome/128.0.6613.186 Electron/32.2.7 Safari/537.36",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MTc1Iiwib3NfdmVyc2lvbiI6IjEwLjAuMjI2MzEiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoiY3MiLCJoYXNfY2xpZW50X21vZHMiOmZhbHNlLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBkaXNjb3JkLzEuMC45MTc1IENocm9tZS8xMjguMC42NjEzLjE4NiBFbGVjdHJvbi8zMi4yLjcgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjMyLjIuNyIsIm9zX3Nka192ZXJzaW9uIjoiMjI2MzEiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjozNTU2MjQsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjU2NzE2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
        }

        payload = {
            "content": "",
            "flags": 0,
            "mobile_network_type": "unknown",
            "nonce": nonce,
            "poll": {
                "allow_multiselect": False,
                "question": {"text": mess},
                "answers": [
                    {"poll_media": {"text": mess}}
                ],
                "duration": 24
            },
            "layout_type": 1,
            "tts": False
        }

        try:
            response = requests.post(f"https://discord.com/api/v9/channels/{chan}/messages", headers=headers, json=payload)
            if response.status_code == 200:
                print(f"Poll successfully sent with token > {token[:35]}****")
            else:
                print(f"Failed to send poll. Status code > {response.status_code} Response > {response.text}")
        except requests.RequestException as e:
            print(f"Error while sending poll: {e}")

def spam_polls(chan, mess, delay, how_many_polls):
    poll_in = PollSpammer
    threads = []
    cl_tokens = cycle(tokens)

    def send(token):
        nonce = poll_in.gen_nonce()
        cookies = poll_in.get_cookies()
        if cookies:
            poll_in.poll_spam(token, nonce, cookies, chan, mess)

    for _ in range(how_many_polls):
        token = next(cl_tokens)
        thread = threading.Thread(target=send, args=(token,))
        threads.append(thread)
        thread.start()
        time.sleep(delay)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    try:
        chan = input(Fore.YELLOW + "Enter the Channel ID > ").strip()
        mess = input(Fore.YELLOW + "Enter the Message to send > ").strip()
        how_many_polls = int(input(Fore.YELLOW + "How many polls to spam? > ").strip())

        while True:
            print(Fore.YELLOW + "Recommended delay is 0.5!")
            delay = float(input(Fore.YELLOW + "Delay between polls (at least 0.4) > ").strip())
            if delay >= 0.4:
                break
            else:
                print(Fore.RED + "Warning > You should use at least delay 0.4 to avoid CloudFlare Restrict!")

        spam_polls(chan, mess, delay, how_many_polls)

    except ValueError:
        print(Fore.RED + "Invalid input.")
    input(Fore.YELLOW + "Press enter to exit...")
