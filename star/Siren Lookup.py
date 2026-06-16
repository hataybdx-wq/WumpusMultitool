import time
from selenium import webdriver
from undetected_chromedriver import Chrome, ChromeOptions
from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore
import os
import webbrowser

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
options = ChromeOptions()
options.add_argument('--headless')  
options.add_argument('--disable-gpu')  

driver = Chrome(options=options)
siren = input(Fore.BLUE + "Siren: " + Fore.WHITE)
url = f"https://www.societe.ninja/data.html?siren={siren}"
driver.get(url)

time.sleep(2)

html_content = driver.page_source
opens = input("You want open source(Y/N):")
if opens =="Y":
    webbrowser.open(url)
    with open(f"Scrap {siren} - Beluga.html", "w", encoding="utf-8") as file:
        file.write(html_content)

if opens =="y":
    webbrowser.open(url)
    with open(f"Scrap {siren} - Beluga.html", "w", encoding="utf-8") as file:
        file.write(html_content)

if opens =="N":
    print(Fore.GREEN + "save in progress..")
    with open(f"Scrap {siren} - Beluga.html", "w", encoding="utf-8") as file:
        file.write(html_content)


if opens =="n":
    print(Fore.GREEN + "save in progress..")
    with open(f"Scrap {siren} - Beluga.html", "w", encoding="utf-8") as file:
        file.write(html_content)

driver.quit()

print("Successfully saved!")
input(Fore.RED + "Press enter to exit...")
