from pystyle import Center, Colorate, Colors
from colorama import Fore, init
import os
import subprocess

init(autoreset=True)

# ====================== FORCER LE BON DOSSIER ======================
def fix_working_directory():
    # Récupère le dossier où se trouve le script main.py
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    print(Fore.GREEN + f"✅ Dossier de travail corrigé → {script_dir}")

fix_working_directory()

# ====================== VÉRIFICATION DISCORD.PY ======================
def check_discord_version(expected_version="1.7.1"):
    try:
        import discord
        if discord.__version__ == expected_version:
            print(Fore.GREEN + f"✅ discord.py {expected_version} OK")
        else:
            print(Fore.YELLOW + f"⚠️ Mise à jour discord.py...")
            os.system("pip uninstall -y discord.py")
            os.system(f"pip install discord.py=={expected_version}")
    except:
        print(Fore.YELLOW + "Installation de discord.py...")
        os.system(f"pip install discord.py=={expected_version}")

check_discord_version()

# ====================== DEBUG ======================
def debug_paths():
    print(Fore.CYAN + "\n" + "="*70)
    print(Fore.YELLOW + "DEBUG - CHEMINS ACTUELS")
    print(Fore.WHITE + f"Dossier actuel : {os.getcwd()}")
    
    sys_path = os.path.join(os.getcwd(), 'sys')
    if os.path.exists(sys_path):
        print(Fore.GREEN + "✅ Dossier 'sys' trouvé")
        print(Fore.WHITE + "Fichiers disponibles :")
        for f in sorted(os.listdir(sys_path)):
            if f.endswith('.py'):
                print(Fore.GREEN + f"   → {f}")
    else:
        print(Fore.RED + "❌ Dossier 'sys' non trouvé !")
    print(Fore.CYAN + "="*70 + "\n")

# ====================== FONCTIONS ======================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print(Colorate.Vertical(Colors.yellow_to_red, """
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
                ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛s
    """))
    
    print(Colorate.Vertical(Colors.green_to_cyan, """
    ┌──────────────────────────┐ ┌──────────────────────────┐ ┌──────────────────────────┐ ┌──────────────────────────┐
    │ <01> Token Spammer       │ │ <07> Mass Reactions      │ │ <13> HypeSquads Changer  │ │ <19> Statut Spammer      │
    │ <02> Token Mass Leaver   │ │ <08> Vocal Tools         │ │ <14> Guild Checker       │ │ <20> Threads Spam        │
    │ <03> Token Leaver        │ │ <09> Onliner             │ │ <15> Flood Spammer       │ │ <21> Poll Spammer        │
    │ <04> Token Info          │ │ <10> Statut Changer      │ │ <16> Logs Spammer        │ │                          │
    │ <05> Bio Changer         │ │ <11>                     │ │ <17> Reactions Nuker     │ │                          │
    │ <06> Nickname Changer    │ │ <12> Token Checker       │ │ <18> Silent Ping         │ │                          │
    └──────────────────────────┘ └──────────────────────────┘ └──────────────────────────┘ └──────────────────────────┘
    """))

def run_script(script_name):
    path = os.path.join('sys', script_name)
    full_path = os.path.abspath(path)
    
    print(Fore.YELLOW + f"\n[→] Tentative d'exécution : {script_name}")
    
    if os.path.isfile(path):
        print(Fore.GREEN + "✅ Script trouvé ! Lancement...")
        subprocess.run(['python', path])
    else:
        print(Fore.RED + f"❌ Script non trouvé : {script_name}")
        print(Fore.WHITE + f"Chemin testé : {full_path}")

# ====================== LANCEMENT ======================
debug_paths()

while True:
    show_menu()
    choice = input(Colorate.Vertical(Colors.yellow_to_red, "\nbeluga@menu$~ Choice ~> ")).strip()

    if choice in ['00', '0', 'exit', 'quit']:
        print(Fore.CYAN + "👋 Au revoir !")
        break

    scripts = {
        '1': 'Token Spammer.py',
        '2': 'Token Mass Leaver.py',
        '3': 'Token leavers.py',
        '4': 'Token info.py',
        '5': 'Bio changer.py',
        '6': 'Nickname changer.py',
        '7': 'Mass reaction.py',
        '8': 'Voice Tools.py',
        '9': 'Onlineacc.py',
        '10': 'Statut changer.py',
        '11': 'Statut changer.py',
        '12': 'Token Checker.py',
        '13': 'HypeSquads.py',
        '14': 'Guild Checker.py',
        '15': 'Flood Spammer.py',
        '16': 'Logs spam.py',
        '17': 'Reactions nuker.py',
        '18': 'Silent Ping.py',
        '19': 'Statut Spammer.py',
        '20': 'Threads Spam.py',
        '21': 'Poll Spammer.py'
    }

    if choice in scripts:
        clear_screen()
        run_script(scripts[choice])
        input(Fore.GREEN + "\nAppuie sur ENTRÉE pour retourner au menu...")
    else:
        print(Fore.RED + "❌ Choix invalide.")
        input(Fore.YELLOW + "Appuie sur ENTRÉE pour réessayer...")