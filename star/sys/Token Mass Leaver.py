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

def leaver(guilds, token):
    for guild in guilds:
        try:
            response = requests.delete(f'https://discord.com/api/v7/users/@me/guilds/{guild["id"]}', headers={'Authorization': token})
            if response.status_code == 204 or response.status_code == 200:
                print(colorama.Fore.GREEN + f"[{token[:20]}...] Leave Server: {guild['name']}")
            elif response.status_code == 400:
                response = requests.delete(f'https://discord.com/api/v3/guilds/{guild["id"]}', headers={'Authorization': token})
                if response.status_code == 204 or response.status_code == 200:
                    print(colorama.Fore.GREEN + f"[{token[:20]}...] Leave Server: {guild['name']}")
            else:
                print(colorama.Fore.RED + f"[{token[:20]}...] Error {response.status_code} on server: {guild['name']}")
        except Exception as e:
            print(colorama.Fore.RED + f"[{token[:20]}...] Exception: {e}")

try:
    with open("input/tokens.txt", "r") as file:
        tokens = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    Error("Fichier 'input/tokens.txt' introuvable.")
except Exception as e:
    Error(e)

for token in tokens:
    try:
        headers = {'Authorization': token}
        response = requests.get("https://discord.com/api/v7/users/@me/guilds", headers=headers)
        if response.status_code != 200:
            ErrorToken(token)
            continue

        guilds_id = response.json()
        if not guilds_id:
            print(colorama.Fore.YELLOW + f"[{token[:20]}...] Aucun serveur trouvé.")
            continue

        for guild_chunk in [guilds_id[i:i+3] for i in range(0, len(guilds_id), 3)]:
            leaver(guild_chunk, token)

    except Exception as e:
        Error(e)
