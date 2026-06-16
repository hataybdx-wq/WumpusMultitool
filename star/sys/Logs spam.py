from pystyle import Center, Colorate, Colors, Anime
import colorama
import os
import random
import requests
import threading
from threading import Lock

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

invitation_count = 0
lock = Lock()

def ErrorToken():
    print(colorama.Fore.RED + "Invalid Token.")
    exit()

def ErrorChoice():
    print(colorama.Fore.RED + "Invalid Choice.")
    exit()

def ErrorNumber():
    print(colorama.Fore.RED + "Invalid number.")
    exit()

def invite(tokens, channels, invitations_per_token):
    global invitation_count
    try:
        token = random.choice(tokens)
        for _ in range(invitations_per_token):
            channel = random.choice(channels)
            response = requests.post(
                f"https://discord.com/api/v10/channels/{channel}/invites",
                headers={
                    'Authorization': token
                }
            )
            response.raise_for_status()

            with lock:
                invitation_count += 1
                print(colorama.Fore.GREEN + f"Invite #{invitation_count} | Channel: {channel} Status: Sent")

    except requests.exceptions.RequestException:
        print(colorama.Fore.RED + f"Ratelimit or other error.")

def main():
    tokens_file_path = os.path.join("input", "tokens.txt")
    
    if not os.path.exists(tokens_file_path):
        print(colorama.Fore.RED + "The 'tokens.txt' file is missing in the 'input' folder.")
        exit()

    try:
        with open(tokens_file_path, 'r') as file:
            tokens = file.read().splitlines()
    except Exception as e:
        print(colorama.Fore.RED + f"Error reading the tokens file: {e}")
        exit()

    channels = input("Enter channel(s) ID(s) (comma separated): ").split(",")

    try:
        threads_number = int(input(f"Enter number of threads (recommended: 2, 4): "))
    except:
        ErrorNumber()

    try:
        invitations_per_token = int(input(f"How many invitations per token? "))
    except:
        ErrorNumber()

    def request():
        threads = []
        try:
            for _ in range(int(threads_number)):
                t = threading.Thread(target=invite, args=(tokens, channels, invitations_per_token))
                t.start()
                threads.append(t)
        except:
            ErrorNumber()

        for thread in threads:
            thread.join()

    while True:
        request()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(colorama.Fore.RED + f"Error: {e}")
