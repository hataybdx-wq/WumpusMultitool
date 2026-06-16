import webbrowser
import time
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    cls()

    print()
    print("╔════════════════════════════╗")
    print("║      TELEGRAM OPENER       ║")
    print("╚════════════════════════════╝")
    print()

    print("[~] Ouverture de Telegram...")
    webbrowser.open("https://t.me/wumpusmultitool")
    print("[✓] Telegram ouvert")

    time.sleep(2)

if __name__ == "__main__":
    main()
