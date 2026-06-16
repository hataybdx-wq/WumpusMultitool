import os
import requests
import json
import time 
import sys 
import threading
from pystyle import Center, Colorate, Colors


class Discord():

    @staticmethod
    def createthread(token, name, channelid):
        payload = json.dumps({
            "name": name,
            "type": 11,
            "auto_archive_duration": 60,
            "location": "Thread Browser Toolbar"
        })
        headers = {
            'authorization': token.strip(),
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.42 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
            'content-type': 'application/json',
            'accept': '*/*'
        }
        url = f"https://canary.discord.com/api/v9/channels/{channelid}/threads"
        while True:
            response = requests.post(url, headers=headers, data=payload)
            print(response.text)
            if response.status_code == 201:
                print(Colorate.Horizontal(Colors.blue_to_cyan, "[+] Thread created successfully."))
            elif response.status_code == 429:
                retry_after = response.json().get("retry_after", 5)
                print("Rate limited.")
                time.sleep(retry_after)
            else:
                print("Error:")
                break


if __name__ == "__main__":
    try:
        with open("input/tokens.txt", "r") as f:
            tokens = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("[-] File 'input/tokens.txt' not found.")
        sys.exit(1)

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
    ThreadName = input(Colorate.Horizontal(Colors.blue_to_cyan,"riskow@Threads$~ → Threads name ~  "))
    channelid = input(Colorate.Horizontal(Colors.blue_to_cyan,"riskow@Threads$~ → Channel id ~ "))
    how_many = int(input(Colorate.Horizontal(Colors.blue_to_cyan,"riskow@menu$~ → How much ~ ")))

    threads = []

    for i in range(how_many):
        for token in tokens:
            thread = threading.Thread(
                target=Discord.createthread,
                args=(token, ThreadName, channelid),
                daemon=True
            )
            threads.append(thread)
            thread.start()
            time.sleep(0.5)

    for thread in threads:
        thread.join()