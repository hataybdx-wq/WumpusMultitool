import requests
from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore
import os
import subprocess
import discord

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
        print(f"[✅] Succes changed {guild_id}.")
    else:
        print(f"[❌] Error with token ({response.status_code}) : {response.text}")


def obtenir_guildes(token):
    url = "https://discord.com/api/v9/users/@me/guilds"
    headers = {
        "Authorization": token.strip(),
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        guildes = response.json()
        return guildes
    else:
        print(f"[❌] I cant get guild : {response.status_code}")
        return []

token_path = os.path.join("input", "tokens.txt")

if not os.path.exists(token_path):
    print("❌ Dont find 'input/tokens.txt'")
    exit()

with open(token_path, "r") as file:
    tokens = [line.strip() for line in file if line.strip()]

if not tokens:
    print("❌ No token found.")
    exit()

nouveau_pseudo = input("✏️ New username : ")

choix = input("(1) One guild  |  (2) all guild : ").strip()

if choix == "1":
    guild_id = input("🏠 Enter guild id (guild_id) : ")
    for i, token in enumerate(tokens, 1):
        print(f"\n🔄 Loading.. {i}/{len(tokens)}")
        changer_pseudo_guild(token, guild_id, nouveau_pseudo)

elif choix == "2":
    for i, token in enumerate(tokens, 1):
        print(f"\n🔄 Loading.. {i}/{len(tokens)}")
        guildes = obtenir_guildes(token)
        if guildes:
            for guilde in guildes:
                guild_id = guilde['id']
                print(f"  ... {guilde['name']} ({guild_id})")
                changer_pseudo_guild(token, guild_id, nouveau_pseudo)
        else:
            print(f"[❌] Error found guild with {token}")
else:
    print("❌ Invalide choice")