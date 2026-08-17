import webbrowser, os, sys

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    launch_path = os.path.join(parent_dir, "launch.py")

    webbrowser.open("https://discord.gg/leakdb")

    if os.path.exists(launch_path):
        os.system(f'start /B "" "{sys.executable}" "{launch_path}"' if os.name == 'nt' else f"'{sys.executable}' '{launch_path}' &")
    
    sys.exit()

if __name__ == "__main__":
    main()
