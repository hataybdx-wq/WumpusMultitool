from pystyle import Center, Colorate, Colors
import colorama
import os
from selenium import webdriver
import time
import sys

os.system('cls')
print(Colorate.Horizontal(Colors.blue_to_cyan,"""
▄▄▄▄  ▄▄▄  ▄▄▄▄                                 
▀███  ███  ███▀                                 
 ███  ███  ███ ██ ██ ███▄███▄ ████▄ ██ ██ ▄█▀▀▀ 
 ███▄▄███▄▄███ ██ ██ ██ ██ ██ ██ ██ ██ ██ ▀███▄ 
  ▀████▀████▀  ▀██▀█ ██ ██ ██ ████▀ ▀██▀█ ▄▄▄█▀ 
                              ██                
                              ▀▀                

                ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                ┃ Author : Wumpus             ┃
                ┃ Discord: .gg/datas          ┃
                ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                          
"""))

colorama.init(autoreset=True)

def ErrorChoice():
    print(colorama.Fore.RED + "Invalid Choice.")
    return

def ErrorToken():
    print(colorama.Fore.RED + "Invalid Token.")
    return

def OnlyLinux():
    print(colorama.Fore.RED + "This feature is only available on Linux.")
    return

token = input("Enter your Discord token: ")

print("""
01 Chrome (Windows / Linux)
02 Edge (Windows)
03 Firefox (Windows) (Recommended)
""")

browser = input("Choose browser -> ")

driver = None

try:
    if browser in ['1', '01']:
        try:
            navigator = "Chrome"
            print(colorama.Fore.YELLOW + f"{navigator} Starting..")
            driver = webdriver.Chrome()
            print(colorama.Fore.GREEN + f"{navigator} Ready!")
        except:
            print(colorama.Fore.RED + f"{navigator} not installed or driver not up to date.")
            
    elif browser in ['2', '02']:
        if sys.platform.startswith("linux"):
            OnlyLinux()
        else:
            try:
                navigator = "Edge"
                print(colorama.Fore.YELLOW + f"{navigator} Starting..")
                driver = webdriver.Edge()
                print(colorama.Fore.GREEN + f"{navigator} Ready!")
            except:
                print(colorama.Fore.RED + f"{navigator} not installed or driver not up to date.")
                
    elif browser in ['3', '03']:
        if sys.platform.startswith("linux"):
            OnlyLinux()
        else:
            try:
                navigator = "Firefox"
                print(colorama.Fore.YELLOW + f"{navigator} Starting..")
                driver = webdriver.Firefox()
                print(colorama.Fore.GREEN + f"{navigator} Ready!")
            except:
                print(colorama.Fore.RED + f"{navigator} not installed or driver not up to date.")
    else:
        ErrorChoice()
    
    if driver:
        script = """
        function login(token) {
            setInterval(() => {
                document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
                location.reload();
            }, 2500);
        }
        """

        driver.get("https://discord.com/login")
        print(colorama.Fore.YELLOW + "Token Connection..")
        driver.execute_script(script + f'\nlogin("{token}")')
        time.sleep(4)
        print(colorama.Fore.GREEN + "Connected Token!")
        print(colorama.Fore.YELLOW + "If you leave the tool, the browser will stay open!")

except Exception as e:
    print(colorama.Fore.RED + f"Error: {e}")

while True:
    time.sleep(1)