import instaloader
import os
from pystyle import Colors
import colorama
from colorama import Fore
import subprocess
import time
import webbrowser
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

loader = instaloader.Instaloader()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def handle_error(message):
    print(f"{Colors.blue}Error: {message}{Colors.reset}")

def get_profile_info(username):
    try:
        profile = instaloader.Profile.from_username(loader.context, username)

        print(f"{Colors.blue}Username: {profile.username}{Colors.reset}")
        print(f"{Colors.blue}Name: {profile.full_name}{Colors.reset}")
        print(f"{Colors.blue}Bio: {profile.biography}{Colors.reset}")
        print(f"{Colors.blue}Followers: {profile.followers}{Colors.reset}")
        print(f"{Colors.blue}Following: {profile.followees}{Colors.reset}")
        print(f"{Colors.blue}Posts: {profile.mediacount}{Colors.reset}")
        print(f"{Colors.blue}Profile Picture URL: {profile.profile_pic_url}{Colors.reset}")

        for post in profile.get_posts():
            print(f"{Colors.blue}Post URL:{Colors.reset} {post.url}")
            print(f"{Colors.blue}Caption:{Colors.reset} {post.caption[:100]}")  
            print(f"{Colors.blue}Likes:{Colors.reset} {post.likes}")
            print(f"{Colors.blue}Comments:{Colors.reset} {post.comments}")
            print()

    except instaloader.exceptions.InstaloaderException as e:
        handle_error(str(e))

if __name__ == "__main__":
    username = input(f"{Colors.blue}username: {Colors.reset}")
    get_profile_info(username)