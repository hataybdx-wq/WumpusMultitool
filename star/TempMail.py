import json
import string
import random
import requests
import time
from threading import Thread
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
class Listen:
    listen = False
    message_ids = []

    def message_list(self):
        url = "https://api.mail.tm/messages"
        headers = {'Authorization': 'Bearer ' + self.token}
        response = self.session.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        return [
            msg for msg in data['hydra:member']
            if msg['id'] not in self.message_ids
        ]

    def message(self, idx):
        url = f"https://api.mail.tm/messages/{idx}"
        headers = {'Authorization': 'Bearer ' + self.token}
        response = self.session.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def run(self):
        while self.listen:
            for message in self.message_list():
                self.message_ids.append(message['id'])
                message_details = self.message(message['id'])
                self.listener(message_details)

            time.sleep(self.interval)

    def start(self, listener, interval=3):
        if self.listen:
            self.stop()

        self.listener = listener
        self.interval = interval
        self.listen = True
        self.thread = Thread(target=self.run)
        self.thread.start()

    def stop(self):
        self.listen = False
        self.thread.join()


def username_gen(length=24, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(length))


def password_gen(length=8, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(length))


class Email(Listen):
    token = ""
    domain = ""
    address = ""
    session = requests.Session()

    def __init__(self):
        if not self.domains():
            raise Exception("Failed to get available domains")

    def domains(self):
        url = "https://api.mail.tm/domains"
        response = self.session.get(url)
        response.raise_for_status()

        try:
            data = response.json()
            for domain in data['hydra:member']:
                if domain['isActive']:
                    self.domain = domain['domain']
                    return True
            raise Exception("No active domain found")
        except Exception as e:
            print(f"Error fetching domains: {e}")
            return False

    def register(self, username=None, password=None, domain=None):
        self.domain = domain or self.domain
        username = username or username_gen()
        password = password or password_gen()

        url = "https://api.mail.tm/accounts"
        payload = {
            "address": f"{username}@{self.domain}",
            "password": password
        }
        headers = {'Content-Type': 'application/json'}
        response = self.session.post(url, headers=headers, json=payload)
        response.raise_for_status()

        data = response.json()
        self.address = data.get('address', f"{username}@{self.domain}")

        self.get_token(password)

        if not self.address:
            raise Exception("Failed to create email address")

    def get_token(self, password):
        url = "https://api.mail.tm/token"
        payload = {
            "address": self.address,
            "password": password
        }
        headers = {'Content-Type': 'application/json'}
        response = self.session.post(url, headers=headers, json=payload)
        response.raise_for_status()

        try:
            self.token = response.json()['token']
        except KeyError:
            raise Exception("Failed to retrieve token")


if __name__ == "__main__":
    def listener(message):
        print(Colors.red,"\n==================================NEW MAIL=========================")
        print(Colors.blue,"\nSubject:" + Fore.WHITE, message.get('subject', 'No subject'))
        print(Colors.blue," Content:" + Fore.WHITE, message.get('text', message.get('html', 'No content')))
        print("\n\n")
        print(Colors.red,"===============================Waiting more mails...===========================")
    tempmail = Email()
    print(Colors.cyan,"\n Domain:" + Fore.WHITE, tempmail.domain)

    tempmail.register()
    print(Colors.cyan,"Email Address:" + Fore.WHITE, tempmail.address)
    tempmail.start(listener)
    print(Colors.pink,"Waiting for new emails...")

