from pystyle import Center, Colorate, Colors, Anime
import colorama
import os
import requests

colorama.init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear')

print(Colorate.Horizontal(Colors.blue_to_cyan, """
 /$$$$$$$  /$$$$$$$$ /$$       /$$   /$$  /$$$$$$   /$$$$$$ 
| $$__  $$| $$_____/| $$      | $$  | $$ /$$__  $$ /$$__  $$ 
| $$  \ $$| $$      | $$      | $$  | $$| $$  \__/| $$  \ $$ 
| $$$$$$$ | $$$$$   | $$      | $$  | $$| $$ /$$$$| $$$$$$$$
| $$__  $$| $$__/   | $$      | $$  | $$| $$|_  $$| $$__  $$ 
| $$  \ $$| $$      | $$      | $$  | $$| $$  \ $$| $$  | $$ 
| $$$$$$$/| $$$$$$$$| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$  | $$ 
|_______/ |________/|________/ \______/  \______/ |__/  |__/ 

                ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                ┃ Author : Ace | Adwares      ┃
                ┃ Discord: .gg/leak-internet  ┃
                ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 
"""))

def get_all_tokens():
    tokens = set()

    # Read from tokens.txt
    if os.path.exists("tokens.txt"):
        with open("tokens.txt", "r", encoding="utf-8") as f:
            for line in f:
                token = line.strip()
                if token:
                    tokens.add(token)

    # Read from input/ folder
    if os.path.exists("input"):
        for filename in os.listdir("input"):
            filepath = os.path.join("input", filename)
            if os.path.isfile(filepath):
                with open(filepath, "r", encoding="utf-8") as f:
                    for line in f:
                        token = line.strip()
                        if token:
                            tokens.add(token)
    return list(tokens)

def set_status(token, status_text):
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    custom_status = {"custom_status": {"text": status_text}}

    try:
        r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=custom_status)
        if r.status_code == 200:
            print(colorama.Fore.GREEN + f"[{token[:20]}...] Status set successfully -> {status_text}")
        else:
            print(colorama.Fore.RED + f"[{token[:20]}...] Failed to set status (code {r.status_code})")
    except Exception as e:
        print(colorama.Fore.RED + f"[{token[:20]}...] Error: {e}")

try:
    status = input("Enter the custom status to set for all tokens -> ")

    tokens = get_all_tokens()
    if not tokens:
        print(colorama.Fore.RED + "No tokens found.")
        exit()

    for token in tokens:
        print(colorama.Fore.CYAN + f"Setting status for token: {token[:20]}...")
        set_status(token, status)

except Exception as e:
    print(colorama.Fore.RED + f"General error: {e}")
