from pystyle import Center, Colorate, Colors, Anime
import colorama
import os
import random
import requests
import threading

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
    print(colorama.Fore.RED + "Invalid number.")
    exit()

def raid(tokens, channels, message):
    try:
        token = random.choice(tokens)
        channel = random.choice(channels)
        response = requests.post(f"https://discord.com/api/channels/{channel}/messages", data={'content': message}, headers={'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7', 'Authorization': token})
        response.raise_for_status()
        print(colorama.Fore.GREEN + f"Message: {message} Channel: {channel} Status: Send")
    except requests.exceptions.RequestException as e:
        print(colorama.Fore.RED + f"Message: {message} Channel: {channel} Status: Error {e}")

def main():
    tokens_file_path = os.path.join("Input", "tokens.txt")
    
    if not os.path.exists(tokens_file_path):
        print(colorama.Fore.RED + "Le fichier 'tokens.txt' est introuvable dans le dossier 'Input'.")
        exit()

    try:
        with open(tokens_file_path, 'r') as file:
            tokens = file.read().splitlines()
    except Exception as e:
        print(colorama.Fore.RED + f"Erreur lors de la lecture du fichier de tokens : {e}")
        exit()

    channels = input("Enter your channels (comma separated): ").split(",")
    message = input(f"Spam Message -> ")
    message_len = len(message)
    if message_len > 10:
        message_sensur = message[:10] + "..."
    else:
        message_sensur = message

    try:
        threads_number = int(input(f"Threads Number (recommended: 2, 4) -> "))
    except:
        ErrorNumber()

    def request():
        threads = []
        try:
            for _ in range(int(threads_number)):
                t = threading.Thread(target=raid, args=(tokens, channels, message))
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
