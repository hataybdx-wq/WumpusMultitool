import os
import requests
import colorama
from pystyle import Center, Colorate, Colors
from colorama import Fore

os.system('cls')
print(Colorate.Vertical(Colors.yellow_to_red,"""
                                                                    
                    (       (                   )\ )         (     
                     ( )\    ( )\  (  (  (     )  (()/(   ) (   )\ )  
                    )((_)  ))((_)))\ )\))( ( /(   /(_)| /( )\ (()/(  
                   ((_)_  /((_) /((_|(_))\ )(_)) (_)) )(_)|(_) ((_)) 
                    | _ )(_))| (_))( (()(_|(_)_  | _ ((_)_ (_) _| |  
                    | _ \/ -_) | || / _` |/ _` | |   / _` || / _` |  
                    |___/\___|_|\_,_\__, |\__,_| |_|_\__,_||_\__,_|  
                                     |___/     
                      
"""))

colorama.init(autoreset=True)
input("Are you sure? (Press enter to continue): ")

def ErrorToken(token):
    print(Fore.RED + f"Invalid Token: {token}\n")

def Error(e):
    print(Fore.RED + f"Error: {e}")
    exit()

def leaver(guilds, token):
    for guild in guilds:
        try:
            response = requests.delete(f'https://discord.com/api/v7/users/@me/guilds/{guild["id"]}', headers={'Authorization': token})
            if response.status_code == 204 or response.status_code == 200:
                print(Fore.GREEN + f"[{token[:20]}...] Leave Server: {guild['name']}")
            elif response.status_code == 400:
                response = requests.delete(f'https://discord.com/api/v3/guilds/{guild["id"]}', headers={'Authorization': token})
                if response.status_code == 204 or response.status_code == 200:
                    print(Fore.GREEN + f"[{token[:20]}...] Leave Server: {guild['name']}")
            else:
                print(Fore.RED + f"[{token[:20]}...] Error {response.status_code} on server: {guild['name']}")
        except Exception as e:
            print(Fore.RED + f"[{token[:20]}...] Exception: {e}")

def changer_pseudo_guild(token, guild_id, nouveau_pseudo):
    url = f"https://discord.com/api/v9/guilds/{guild_id}/members/@me"
    headers = {
        "Authorization": token.strip(),
        "Content-Type": "application/json"
    }
    payload = {
        "nick": nouveau_pseudo 
    }

    response = requests.patch(url, headers=headers, json=payload)

    if response.status_code == 200:
        print(f"[✅] Changed nickname in {guild_id}.")
    else:
        print(f"[❌] Error ({response.status_code}) : {response.text}")

def obtenir_guildes(token):
    url = "https://discord.com/api/v9/users/@me/guilds"
    headers = {
        "Authorization": token.strip(),
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"[❌] Can't get guilds: {response.status_code}")
        return []

token_path = os.path.join("input", "tokens.txt")
if not os.path.exists(token_path):
    Error("❌ Fichier 'input/tokens.txt' introuvable.")

with open(token_path, "r") as file:
    tokens = [line.strip() for line in file if line.strip()]

if not tokens:
    Error("❌ Aucun token trouvé.")

for token in tokens:
    try:
        headers = {'Authorization': token}
        response = requests.get("https://discord.com/api/v7/users/@me/guilds", headers=headers)
        if response.status_code != 200:
            ErrorToken(token)
            continue

        guilds_id = response.json()
        if not guilds_id:
            print(Fore.YELLOW + f"[{token[:20]}...] Aucun serveur trouvé.")
            continue

        for guild_chunk in [guilds_id[i:i+3] for i in range(0, len(guilds_id), 3)]:
            leaver(guild_chunk, token)

    except Exception as e:
        Error(e)

nouveau_pseudo = "Format | Beluga"
for i, token in enumerate(tokens, 1):
    print(f"\n🔄 Loading.. {i}/{len(tokens)}")
    guildes = obtenir_guildes(token)
    if guildes:
        for guilde in guildes:
            print(f"  ... {guilde['name']} ({guilde['id']})")
            changer_pseudo_guild(token, guilde['id'], nouveau_pseudo)
    else:
        print(f"[❌] No guilds found for token: {token[:20]}...")
else:
    print("❌ Invalid choice.")
