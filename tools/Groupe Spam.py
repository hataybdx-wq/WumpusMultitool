import requests
import random
from time import sleep

from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore
import os

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

def clear():
    print("\033c", end="")

def proxy():
    return None

def getheaders(token):
    return {
        "Authorization": token,
        "Content-Type": "application/json"
    }

def handle_error(message):
    print(f"Error: {message}")

def main():
    clear()
    print("Returning to main menu...")

def selector(token, users):
    clear()
    while True:
        try:
            response = requests.post(
                'https://discordapp.com/api/v9/users/@me/channels',
                proxies=proxy(),
                headers=getheaders(token),
                json={"recipients": users}
            )

            if response.status_code in [200, 204]:
                print("Created groupchat")
            elif response.status_code == 429:
                print(f"Rate limited ({response.json().get('retry_after', 'N/A')}ms)")
            else:
                handle_error(f"HTTP {response.status_code}")
        except Exception as e:
            handle_error(str(e))
        except KeyboardInterrupt:
            break
    main()

def randomizer(token, IDs):
    while True:
        users = random.sample(IDs, 2)
        try:
            response = requests.post(
                'https://discordapp.com/api/v9/users/@me/channels',
                proxies={"http": f'{proxy()}'},
                headers=getheaders(token),
                json={"recipients": users}
            )

            if response.status_code in [200, 204]:
                print("Created groupchat")
            elif response.status_code == 429:
                print(f"Rate limited ({response.json().get('retry_after', 'N/A')}ms)")
            else:
                handle_error(f"HTTP {response.status_code}")
        except Exception as e:
            handle_error(str(e))
        except KeyboardInterrupt:
            break
    main()


token = input("Your Account Token: ")

print('\nDo you want to choose user(s) yourself to groupchat spam or do you want to select randoms?')
print('''
[01] Choose user(s) yourself
[02] Randomize the users
                    ''')
try:
    secondchoice = int(input('Choice: '))
except ValueError:
    handle_error("Invalid input. Please enter a number.")
    main()

if secondchoice not in [1, 2]:
    handle_error('Invalid Choice')
    main()

if secondchoice == 1:
    print('\nInput the users you want to create a groupchat with (separate by , id,id2,id3)')
    recipients = input('Users ID: ')
    user = recipients.split(',')
    if len(user) < 2:
        handle_error("You need to input at least two user IDs, separated by commas.")
        main()
    input('\n\n\nPress enter to continue ("ctrl + c" at anytime to stop)')
    selector(token, user)

elif secondchoice == 2:
    IDs = []
    try:
        friendIds = requests.get(
            "https://discord.com/api/v9/users/@me/relationships",
            proxies={"http": f'http://{proxy()}'},
            headers=getheaders(token)
        ).json()
        for friend in friendIds:
            IDs.append(friend['id'])
    except Exception as e:
        handle_error(f"Failed to get friend IDs: {str(e)}")
        main()
    input('Press enter to continue ("ctrl + c" at anytime to stop)')
    randomizer(token, IDs)

if __name__ == "__main__":
    main()
    input(" ")
