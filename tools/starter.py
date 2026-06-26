import webbrowser
import time
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    cls()

    print()
    print("╔════════════════════════════╗")
    print("║      Discord  OPENER       ║")
    print("╚════════════════════════════╝")
    print()

    print("[~] Ouverture de Telegram...")
    webbrowser.open("https://discord.gg/xvQXbG5VtN")
    print("[✓] Discord ouvert")

    time.sleep(2)

if __name__ == "__main__":
    main()
