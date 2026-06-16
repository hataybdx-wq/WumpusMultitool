import requests
import random
import os
import asyncio
import aiohttp
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
def get_tokens():
    token_path = "input/tokens.txt"
    if not os.path.exists(token_path):
        print("[❌] 'tokens.txt' not found.")
        return []
    with open(token_path, "r") as file:
        return [line.strip() for line in file if line.strip()]

def random_user_agent():
    return random.choice([
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
    ])

emojis = ["🔥", "💀", "👎", "🤯", "🍆", "🔞", "🍑",]

async def spam_reactions(session, token, channel_id, message_id):
    headers = {
        "Authorization": token,
        "User-Agent": random_user_agent(),
        "Content-Type": "application/json"
    }

    while True:
        emoji = random.choice(emojis)

        add_url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me"
        async with session.put(add_url, headers=headers) as resp_add:
            if resp_add.status == 204:
                print(f"[+✅] {token[:15]}... reacted with {emoji}")
            else:
                print(f"[+❌] {token[:15]}... failed to react with {emoji} ({resp_add.status})")

        await asyncio.sleep(0.1)

        async with session.delete(add_url, headers=headers) as resp_del:
            if resp_del.status == 204:
                print(f"[-🗑️] {token[:15]}... removed {emoji}")
            else:
                print(f"[-❌] {token[:15]}... failed to remove {emoji} ({resp_del.status})")

        await asyncio.sleep(0.1)

async def main():
    channel_id = input("[=] Channel ID: ").strip()
    message_id = input("[=] Message ID: ").strip()
    tokens = get_tokens()

    if not tokens:
        print("[❌] No tokens found.")
        return

    async with aiohttp.ClientSession() as session:
        tasks = [
            spam_reactions(session, token, channel_id, message_id)
            for token in tokens
        ]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
