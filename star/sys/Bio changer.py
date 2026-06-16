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
def change_bio_in_guild(token, guild_id, new_bio):
    url = f"https://discord.com/api/v9/guilds/{guild_id}/members/@me"
    headers = {
        "Authorization": token.strip(),
        "Content-Type": "application/json"
    }
    payload = {
        "about": new_bio  
    }

    response = requests.patch(url, headers=headers, json=payload)

    if response.status_code == 200:
        print(f"[✅] Bio successfully updated for guild {guild_id}.")
    else:
        print(f"[❌] Error with token ({response.status_code}): {response.text}")


def get_guilds(token):
    url = "https://discord.com/api/v9/users/@me/guilds"
    headers = {
        "Authorization": token.strip(),
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        guilds = response.json()
        return guilds
    else:
        print(f"[❌] Unable to retrieve guilds: {response.status_code}")
        return []


token_path = os.path.join("input", "tokens.txt")

if not os.path.exists(token_path):
    print("❌ The file 'input/tokens.txt' is missing.")
    exit()

with open(token_path, "r") as file:
    tokens = [line.strip() for line in file if line.strip()]

if not tokens:
    print("❌ No tokens found in the file.")
    exit()

new_bio = input("✏️ Enter the new bio to apply: ")
choice = input("Do you want to change the bio for (1) a specific guild or (2) all guilds? (1/2): ").strip()

if choice == "1":
    guild_id = input("🏠 Enter the guild ID (guild_id) where you want to apply the change: ")
    for i, token in enumerate(tokens, 1):
        print(f"\n🔄 Processing token {i}/{len(tokens)}")
        change_bio_in_guild(token, guild_id, new_bio)

elif choice == "2":
    for i, token in enumerate(tokens, 1):
        print(f"\n🔄 Processing token {i}/{len(tokens)}")
        guilds = get_guilds(token)
        if guilds:
            for guild in guilds:
                guild_id = guild['id']
                print(f"  Applying change for guild {guild['name']} ({guild_id})")
                change_bio_in_guild(token, guild_id, new_bio)
        else:
            print(f"[❌] Unable to retrieve guilds for token {token}")
else:
    print("❌ Invalid choice, please select 1 or 2.")