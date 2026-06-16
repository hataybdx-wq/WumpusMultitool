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

message_count = 0
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

def raid(tokens, channel, message, user_id):
    global message_count
    try:
        token = random.choice(tokens)
        response = requests.post(
            f"https://discord.com/api/channels/{channel}/messages",
            data={'content': f"<@{user_id}> {message}"},
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                'Authorization': token
            }
        )
        response.raise_for_status()

        with lock:
            message_count += 1
            print(colorama.Fore.GREEN + f"Send #{message_count} | {message[:10]}... Channel: {channel} Status: Sent")
        message_id = response.json()['id']
        requests.delete(
            f"https://discord.com/api/channels/{channel}/messages/{message_id}",
            headers={'Authorization': token}
        )
        print(colorama.Fore.YELLOW + f"Message #{message_count} deleted from channel {channel}")

    except requests.exceptions.RequestException:
        print(colorama.Fore.RED + f"Ratelimit")

def main():
    tokens_file_path = os.path.join("input", "tokens.txt")
    
    if not os.path.exists(tokens_file_path):
        print(colorama.Fore.RED + "Le fichier 'tokens.txt' est introuvable dans le dossier 'input'.")
        exit()

    try:
        with open(tokens_file_path, 'r') as file:
            tokens = file.read().splitlines()
    except Exception as e:
        print(colorama.Fore.RED + f"Erreur lors de la lecture du fichier de tokens : {e}")
        exit()

    channel = input("Channel ID: ")
    user_id = input("User ID to ping: ")
    message = ("silend ping")

    try:
        threads_number = int(input(f"Threads Number (recommended: 2, 4) -> "))
    except:
        ErrorNumber()

    def request():
        threads = []
        try:
            for _ in range(int(threads_number)):
                t = threading.Thread(target=raid, args=(tokens, channel, message, user_id))
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
