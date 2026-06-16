import os
import requests
from colorama import Fore, init
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
init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def extract_tokens(raw_text):
    tokens = raw_text.replace('\r', '').replace('\n', ' ').split()
    return [token.strip() for token in tokens if token.strip()]

def read_tokens_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return extract_tokens(f.read())
    except FileNotFoundError:
        return []

def read_tokens_from_folder(folder_path):
    tokens = []
    if not os.path.exists(folder_path):
        return tokens
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                tokens += extract_tokens(f.read())
        except:
            continue
    return tokens

def is_in_guild(token, guild_id):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    response = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
    
    if response.status_code != 200:
        print(Fore.RED + f"[INVALID TOKEN] {token[:30]}...")
        return False
    
    guilds = response.json()
    for guild in guilds:
        if guild['id'] == guild_id:
            return True
    return False

def main():
    
    guild_id = input(Fore.YELLOW + "Enter the Guild (Server) ID to check: ").strip()

    tokens_file = read_tokens_from_file("tokens.txt")
    tokens_folder = read_tokens_from_folder("input")

    all_tokens = list(set(tokens_file + tokens_folder))

    print(Fore.CYAN + f"\n[INFO] {len(all_tokens)} tokens loaded.\n")

    for token in all_tokens:
        try:
            in_guild = is_in_guild(token, guild_id)
            status = Fore.GREEN + "[IN SERVER]" if in_guild else Fore.YELLOW + "[NOT IN SERVER]"
            print(f"{status} {token[:30]}...")
        except Exception as e:
            print(Fore.RED + f"[ERROR] {token[:30]}... -> {str(e)}")

    print(Fore.CYAN + "\nVerification complete.")
    input(Fore.YELLOW + "Press Enter to exit...")

if __name__ == "__main__":
    main()
