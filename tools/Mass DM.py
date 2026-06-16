from pystyle import Center, Colorate, Colors, Anime
import colorama
import os
import requests
import threading
import time

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

def ErrorToken():
    print(colorama.Fore.RED + "Invalid Token.")
    exit()

def ErrorNumber():
    print(colorama.Fore.RED + "Invalid number input.")
    exit()

def MassDM(token_discord, channels, message):
    for channel in channels:
        for user in [x["username"]+"#"+x["discriminator"] for x in channel["recipients"]]:
            try:
                requests.post(f"https://discord.com/api/v9/channels/{channel['id']}/messages", headers={'Authorization': token_discord}, data={"content": message})
                print(f'{colorama.Fore.GREEN}Status: Send User: {user}')
            except Exception as e:
                print(f'{colorama.Fore.RED}Status: Error: {e}')

def main():
    try:
        token_discord = input("Enter your Discord token: ")
        validityTest = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token_discord, 'Content-Type': 'application/json'})
        if validityTest.status_code != 200:
            ErrorToken()

        message = str(input("Enter the message to send: "))
        try:
            repetition = int(input("Enter number of repetitions: "))
        except:
            ErrorNumber()

        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': token_discord}).json()

        processes = []
        number = 0
        for i in range(repetition):
            number += 1
            if not channelIds:
                continue
            for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
                t = threading.Thread(target=MassDM, args=(token_discord, channel, message))
                t.start()
                processes.append(t)
            for process in processes:
                process.join()
            print(f"{colorama.Fore.YELLOW}Finish {number}.")
            time.sleep(0.5)

    except Exception as e:
        print(colorama.Fore.RED + f"Error: {e}")

if __name__ == "__main__":
    main()
