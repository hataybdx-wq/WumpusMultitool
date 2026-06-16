import requests
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
def check_token(token):
    url = "https://discord.com/api/v9/users/@me"
    headers = {
        "Authorization": token
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("✅ Token valid !")
        user = response.json()
        print(f"user : {user['username']}#{user['discriminator']}")
    elif response.status_code == 401:
        print("❌ Token invalid.")
    else:
        print(f"⚠️ Error (code {response.status_code})")

if __name__ == "__main__":
    token = input("🔐 Token : ")
    check_token(token)
