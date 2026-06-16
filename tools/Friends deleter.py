import os
from pystyle import Colorate, Colors
import requests
import threading
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

def delete_friends(token, friends):
    headers = {'Authorization': token}
    for friend in friends:
        try:
            requests.delete(f'https://discord.com/api/v9/users/@me/relationships/{friend["id"]}', headers=headers)
            print(f"{Fore.GREEN}[DELETED] User: {friend['user']['username']}#{friend['user']['discriminator']}")
        except Exception as e:
            print(f"{Fore.RED}[ERROR] Could not delete {friend['user']['username']} - {e}")

def main():
    token = input(f"{Fore.YELLOW}Enter Discord Token: {Style.RESET_ALL}").strip()
    headers = get_token_info(token)

    friend_id = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).json()
    if not friend_id:
        print(f"{Fore.BLUE}[INFO] No friends found.")
        return

    processes = []
    for friend_chunk in [friend_id[i:i+3] for i in range(0, len(friend_id), 3)]:
        t = threading.Thread(target=delete_friends, args=(token, friend_chunk))
        t.start()
        processes.append(t)

    for process in processes:
        process.join()

    print(f"{Fore.YELLOW}[DONE] All friends deleted.")

if __name__ == "__main__":
    main()
