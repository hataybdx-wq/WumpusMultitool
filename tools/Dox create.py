import random
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import os
from random import randint
from time import time, sleep
from getpass import getpass as hinput
from pystyle import Colors
import socket
import colorama
from colorama import Fore
import os
import subprocess
import time
import webbrowser
import threading
from pystyle import Center, Colorate, Colors, Anime
import colorama
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


def current_time_hour():
    from datetime import datetime
    return datetime.now().strftime("%H:%M:%S")


def Continue():
    input("Appuyez sur Entrée pour continuer...")


try:
    ("DOX Creation by Riskow\n")

    by = input("Doxed By: ")
    reason = input("Reason: ")
    pseudo1 = input("First Pseudo: ")
    pseudo2 = input("Second Pseudo: ")


    print("\nDiscord Information:")
    username_discord = input("Username: ")
    token = input("Token: ")
    display_name_discord = input("Display Name: ")
    user_id_discord = input("Id: ")
    avatar_url_discord = input("Avatar: ")
    created_at_discord = input("Created At: ")
    email_discord = input("Email: ")
    phone_discord = input("Phone: ")
    nitro_discord = input("Nitro: ")
    friends_discord = input("Friends: ")
    gift_codes_discord = input("Gift Code: ")
    mfa_discord = input("Mfa: ")
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

    print("\nIP Information:")
    ip_public = input("Public IP: ")
    ip_local = input("Local IP: ")
    ipv6 = input("IPv6: ")
    vpn_pc = input("VPN (y/n): ")
    operator_ip = input("Operator: ")
    host_ip = input("Hostname: ")
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

    print("\nPC Information:")
    name_pc = input("Name: ")
    username_pcc = input("Username: ")
    displayname_pc = input("Display Name: ")
    platform_pc = input("Platform: ")
    exploitation_pc = input("OS: ")
    windowskey_pc = input("Windows Key: ")
    mac_pc = input("Mac adresse: ")
    cpu_pc = input("CPU: ")
    hwid_pc = input("HWID: ")
    disk_pc = input("Hard Disk: ")
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


    print("\nPersonal Information:")
    gender = input("Gender: ")
    last_name = input("Last Name: ")
    first_name = input("First Name: ")
    mother = input("Mother: ")
    father = input("Father: ")
    brother = input("Brother: ")
    sister = input("Sister: ")
    age = input("Age: ")
    number_phone = input("Number phone: ")
    number_phoneold = input("Number phone old: ")
    operator_phone = input("Operator: ")
    email = input("email: ")
    email2 = input("email 2: ")
    email3 = input("email 3: ")
    email4 = input("email 4: ")
    Adresse = input("Adresse: ")
    Adresseold = input("Adresse old: ")
    Iban = input("Iban: ")
    Credit_card = input("Credit card: ")
    Expiration = input("Expiration: ")
    CSV = input("CSV: ")
    First_Namepay = input("First Name: ")
    last_namepay = input("Last nam: ")
    Bank = input("Bank: ")
    Image = input("Image: ")
    Document = input("Document: ")
    Document2 = input("Document 2: ")
    Document3 = input("Document 3: ")
    Document4 = input("Document 4: ")
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


    print("\nLocation Information:")
    continent = input("Continent: ")
    country = input("Country: ")
    region = input("Region: ")
    postal_code = input("Postal Code: ")
    city = input("City: ")
    adress = input("Address: ")
    timezone = input("Timezone: ")
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
    
    print("\nOther:")
    other = input("Other Info: ")

    name_file = input(f"{current_time_hour()} Choose the file name -> ")
    if not name_file.strip():
        name_file = f'No Name {random.randint(1, 999)}'


    dox_path_relative = f"D0x - {name_file} - Wumpus.txt"

    with open(f"D0x - {name_file} - Riskow.txt", 'w', encoding='utf-8') as file:
        file.write(f'''
    ██████   ██████  ██   ██ 
    ██   ██ ██    ██  ██ ██  
    ██   ██ ██    ██   ███   
    ██   ██ ██    ██  ██ ██  
    ██████   ██████  ██   ██ Made with WumpusTool
                                                          
    ╚Doxed By : {by}
    ╚Reason   : {reason}
    ╚Pseudo   : "{pseudo1}", "{pseudo2}"
╔→ 0x01 - Discord...................──────────────────────────────────╗
    ║ | [+] Token               <-> {token}
    ║ | [+] Username            <-> {username_discord}
    ║ | [+] Display Name        <-> {display_name_discord}
    ║ | [+] ID                  <-> {user_id_discord}
    ║ | [+] Avatar              <-> {avatar_url_discord}
    ║ | [+] Created At          <-> {created_at_discord}
    ║ | [+] E-Mail              <-> {email_discord}
    ║ | [+] Phone               <-> {phone_discord}
    ║ | [+] Nitro               <-> {nitro_discord}
    ║ | [+] Friends             <-> {friends_discord}
    ║ | [+] Gift Code           <-> {gift_codes_discord}
    ║ | [+] Multi-FA            <-> {mfa_discord} 
    ╚──────────────────────────────────────────────────────────────────────────────────╝
╔→ 0x02 - IP INFOS...................──────────────────────────────────╗
    ║ | [+] Public IP           <-> {ip_public}
    ║ | [+] Local IP            <-> {ip_local}
    ║ | [+] IPv6                <-> {ipv6}
    ║ | [+] VPN Used            <-> {vpn_pc}
    ║ | [+] Operator            <-> {operator_ip}
    ║ | [+] Hostname            <-> {host_ip}
    ╚──────────────────────────────────────────────────────────────────────────────────╝
╔→ 0x03 - PC INFOS...................──────────────────────────────────╗
    ║ | [+] Name                <-> {name_pc}
    ║ | [+] Username            <-> {username_pcc}
    ║ | [+] Display Name        <-> {displayname_pc}
    ║ | [+] Platform            <-> {platform_pc}
    ║ | [+] OS                  <-> {exploitation_pc}
    ║ | [+] Windows Key         <-> {windowskey_pc}
    ║ | [+] Mac adresse         <-> {mac_pc}
    ║ | [+] CPU                 <-> {cpu_pc}
    ║ | [+] HWID                <-> {hwid_pc}
    ║ | [+] Hard Disk           <-> {disk_pc}
    ╚──────────────────────────────────────────────────────────────────────────────────╝

╔→ 0x04 - PERSONAL INFO...................──────────────────────────────────╗
    ║ | [+] Gender              <-> {gender}
    ║ | [+] Last Name           <-> {last_name}
    ║ | [+] First Name          <-> {first_name}
    ║ | [+] Sister              <-> {sister}
    ║ | [+] Brother             <-> {brother}
    ║ | [+] Father              <-> {father}
    ║ | [+] Mother              <-> {mother}
    ║ | [+] Age                 <-> {age}
    ║ | [+] Number phone        <-> {number_phone}
    ║ | [+] Number phone(old)   <-> {number_phoneold}
    ║ | [+] Operator            <-> {operator_phone}
    ║ | [+] Email               <-> {email}
    ║ | [+] Email 2             <-> {email2}
    ║ | [+] Email 3             <-> {email3}
    ║ | [+] Email 4             <-> {email4}
    ║ | [+] Adresse             <-> {Adresse}
    ║ | [+] Adresse(old)        <-> {Adresseold}
    ║ | [+] Continent           <-> {continent}
    ║ | [+] Country             <-> {country}
    ║ | [+] Region              <-> {region}
    ║ | [+] Postal code         <-> {postal_code}
    ║ | [+] City                <-> {city}
    ║ | [+] Timezone            <-> {timezone}
    ║ | [+] Image               <-> {Image}
    ║ | [+] Document            <-> {Document}
    ║ | [+] Document 2          <-> {Document2}
    ║ | [+] Document 3          <-> {Document3}
    ║ | [+] Document 4          <-> {Document4}
    ╚──────────────────────────────────────────────────────────────────────────────────╝
╔→ 0x05 - Payement...................──────────────────────────────────╗
    ║ | [+] Iban                <-> {Iban}
    ║ | [+] Credit card         <-> {Credit_card}
    ║ | [+] Expiration          <-> {Expiration}
    ║ | [+] CSV                 <-> {CSV}
    ║ | [+] First Name          <-> {First_Namepay}
    ║ | [+] Last name           <-> {last_namepay}
    ║ | [+] Bank                <-> {Bank}
    ╚──────────────────────────────────────────────────────────────────────────────────╝
╔→ 0x06 - Other...................──────────────────────────────────╗
    ║ | [+] OTHER INFO         <-> {other}
    ╚──────────────────────────────────────────────────────────────────────────────────╝
        ''')

    print(f"{current_time_hour()} The DOX {name_file} was saved to {dox_path_relative}")
    Continue()
except Exception as e:
    print(f"An error occurred: {e}")
