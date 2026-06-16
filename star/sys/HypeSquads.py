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

def ErrorChoice():
    print(colorama.Fore.RED + "Invalid Choice.")
    exit()

def ChangeHouse(token, house_choice):
    response = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
    if response.status_code != 200:
        print(colorama.Fore.RED + f"[INVALID] Token: {token}")
        return

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }

    if house_choice in ["1", "01"]:
        payload = {'house_id': 1}
    elif house_choice in ["2", "02"]:
        payload = {'house_id': 2}
    elif house_choice in ["3", "03"]:
        payload = {'house_id': 3}
    else:
        ErrorChoice()

    r = requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    if r.status_code == 204:
        print(colorama.Fore.GREEN + f"[SUCCESS] Token: {token} -> Hypesquad house changed.")
    else:
        print(colorama.Fore.RED + f"[FAILED] Token: {token} -> Failed to change house.")

try:
    print("""
    01 Bravery
    02 Brilliance
    03 Balance
    """)

    house = input("Choose house -> ").lstrip("0")

    tokens_path = os.path.join("input", "tokens.txt")
    if not os.path.exists(tokens_path):
        print(colorama.Fore.RED + "tokens.txt not found in 'input/' folder.")
        exit()

    with open(tokens_path, 'r') as f:
        tokens = [line.strip() for line in f if line.strip()]

    if not tokens:
        print(colorama.Fore.RED + "No tokens found in tokens.txt.")
        exit()

    for token in tokens:
        ChangeHouse(token, house)

except Exception as e:
    print(colorama.Fore.RED + f"Error: {e}")
