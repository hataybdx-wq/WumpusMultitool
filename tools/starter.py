import webbrowser
import os
import sys

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    launch_path = os.path.join(parent_dir, "launch.py")

    # Ouvre Discord uniquement si le marqueur n'existe pas
    marker = os.path.join(parent_dir, ".discord_opened")

    if not os.path.exists(marker):
        webbrowser.open("https://discord.gg/leakdb")
        open(marker, "w").close()

    if os.path.exists(launch_path):
        if os.name == "nt":
            os.system(f'start /B "" "{sys.executable}" "{launch_path}"')
        else:
            os.system(f'"{sys.executable}" "{launch_path}" &')

    sys.exit()

if __name__ == "__main__":
    main()
