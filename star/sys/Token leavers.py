from pystyle import Center, Colorate, Colors, Anime
import colorama
import os
import requests

os.system('cls' if os.name == 'nt' else 'clear')
print(Colorate.Vertical(Colors.yellow_to_red,"""
                                                                    
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

colorama.init(autoreset=True)
input("Are you sure? (Press enter to continue): ")

def ErrorToken(token):
    print(colorama.Fore.RED + f"Invalid Token: {token}\n")

def Error(e):
    print(colorama.Fore.RED + f"Error: {e}")
    exit()

def leave_server_by_id(server_id, token):
    try:
        response = requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{server_id}', headers={'Authorization': token})
        if response.status_code in [200, 204]:
            print(colorama.Fore.GREEN + f"[{token[:20]}...] Successfully left server ID: {server_id}")
        else:
            print(colorama.Fore.RED + f"[{token[:20]}...] Failed to leave server ID: {server_id}, status code: {response.status_code}")
    except Exception as e:
        print(colorama.Fore.RED + f"[{token[:20]}...] Exception: {e}")

try:
    with open("input/tokens.txt", "r") as file:
        tokens = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    Error("Fichier 'input/tokens.txt' introuvable.")
except Exception as e:
    Error(e)

server_id = input("Entrez l'ID du serveur à quitter : ")

for token in tokens:
    leave_server_by_id(server_id, token)
