from pystyle import Center, Colorate, Colors
import colorama
import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options

os.system('cls' if os.name == 'nt' else 'clear')
print(Colorate.Horizontal(Colors.blue_to_cyan, """
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
navigator = ""

try:
    invite = input("Enter Discord Invite Link: ")
    if browser in ['1', '01']:
        navigator = "Chrome"
        print(colorama.Fore.YELLOW + f"{navigator} Starting with stealth mode...")
        chrome_options = Options()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = uc.Chrome(options=chrome_options)

    elif browser in ['2', '02']:
        if sys.platform.startswith("linux"):
            OnlyLinux()
            sys.exit()
        navigator = "Edge"
        print(colorama.Fore.YELLOW + f"{navigator} Starting...")
        driver = webdriver.Edge()

    elif browser in ['3', '03']:
        if sys.platform.startswith("linux"):
            OnlyLinux()
            sys.exit()
        navigator = "Firefox"
        print(colorama.Fore.YELLOW + f"{navigator} Starting...")
        driver = webdriver.Firefox()

    else:
        ErrorChoice()
        sys.exit()

    print(colorama.Fore.GREEN + f"{navigator} Ready!")

    driver.get("https://discord.com/login")
    print(colorama.Fore.YELLOW + "Connecting using token...")

    # Inject login script
    script = """
    function login(token) {
        setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`;
        }, 50);
        setTimeout(() => {
            location.reload();
        }, 2500);
    }
    """
    driver.execute_script(script + f'\nlogin("{token}")')
    time.sleep(5)
    print(colorama.Fore.GREEN + "Connected to Discord account!")

    # ========== Rejoindre un serveur ==========
    print(colorama.Fore.YELLOW + "Accès au menu d'ajout de serveur...")

    # 1. Clique sur "Ajouter un serveur"
    time.sleep(3)
    add_server_btn = driver.find_element(By.CSS_SELECTOR, "div.circleIconButton__5bc7e[aria-label][role='treeitem']")
    add_server_btn.click()
    print(colorama.Fore.YELLOW + "→ Étape 1 : Bouton 'Ajouter un serveur' cliqué")

    # 2. Clique sur "Rejoindre un serveur"
    time.sleep(2)
    join_server_btn = driver.find_element(By.CSS_SELECTOR, "button.footerButton_c04f35.button__201d5")
    join_server_btn.click()
    print(colorama.Fore.YELLOW + "→ Étape 2 : Bouton 'Rejoindre un serveur' cliqué")

    # 3. Input de l'invite

    time.sleep(2)
    invite_input = driver.find_element(By.CSS_SELECTOR, "input.inputDefault__0f084.input__0f084.inputInner__991a0")
    invite_input.send_keys(invite)
    print(colorama.Fore.YELLOW + "→ Étape 3 : Lien d'invitation inséré")

    # 4. Clique sur "Rejoindre"
    time.sleep(2)
    confirm_btn = driver.find_element(By.CSS_SELECTOR, "button.button__201d5.lookFilled__201d5.colorBrand__201d5")
    driver.execute_script("arguments[0].click();", confirm_btn)
    print(colorama.Fore.GREEN + "✅ Serveur rejoint avec succès !")


    print(colorama.Fore.YELLOW + "Le navigateur restera ouvert même après avoir fermé l'outil.")

except Exception as e:
    print(colorama.Fore.RED + f"Erreur : {e}")

while True:
    time.sleep(1)
