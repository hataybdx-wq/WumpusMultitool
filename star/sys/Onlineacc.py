import os
import json
import asyncio
import websockets
from pystyle import Center, Colorate, Colors, Anime
import colorama
import os
import requests
from datetime import datetime, timezone

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
                                               
                ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                ┃ Author : Ace | Adwares      ┃
                ┃ Discord: .gg/leak-internet  ┃
                ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛     
                   
"""))
tokens_file = os.path.join('input', 'tokens.txt')

if not os.path.exists(tokens_file):
    print(f"[ERREUR] Le fichier '{tokens_file}' est introuvable.")
    exit()

with open(tokens_file, 'r') as f:
    tokens = [line.strip() for line in f if line.strip()]

if not tokens:
    print("[ERREUR] Aucun token trouvé dans le fichier.")
    exit()

server_id = input("Server ID: ")
channel_id = input("Channel ID: ")

print("Choisis le statut du bot :")
print("1 - En ligne")
print("2 - Inactif")
print("3 - Ne pas déranger")
print("4 - Invisible")

status_choice = input("Ton choix (1-4) : ")

status_map = {
    "1": "online",
    "2": "idle",
    "3": "dnd",
    "4": "invisible"
}

status = status_map.get(status_choice, "online") 

async def connect_bot(token):
    try:
        async with websockets.connect("wss://gateway.discord.gg/?v=9&encoding=json") as ws:
            hello = await ws.recv()
            hello_json = json.loads(hello)
            heartbeat_interval = hello_json['d']['heartbeat_interval']

            await ws.send(json.dumps({
                "op": 2,
                "d": {
                    "token": token,
                    "properties": {
                        "os": "windows",
                        "browser": "Discord",
                        "device": "desktop"
                    },
                    "presence": {
                        "status": status,
                        "afk": False,
                        "since": 0,
                        "activities": []
                    }
                }
            }))

            await ws.send(json.dumps({
                "op": 4,
                "d": {
                    "guild_id": server_id,
                    "channel_id": channel_id,
                    "self_mute": False,
                    "self_deaf": False
                }
            }))

            print(f"[+] Bot connecté : {token[:30]}... avec le statut '{status}'")

            while True:
                await asyncio.sleep(heartbeat_interval / 1000)
                await ws.send(json.dumps({"op": 1, "d": None}))

    except Exception as e:
        print(f"[!] Erreur avec le token {token[:30]}... : {e}")

async def main():
    tasks = [asyncio.create_task(connect_bot(token)) for token in tokens]
    await asyncio.gather(*tasks)

asyncio.run(main())
