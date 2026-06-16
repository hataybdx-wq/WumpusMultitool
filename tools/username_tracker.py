import requests
from bs4 import BeautifulSoup
import time
from colorama import Fore, init
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
init(autoreset=True)

def run():
    try:
        sites = {
            "500px": "https://500px.com/{}",
            "8tracks": "https://8tracks.com/{}",
            "About.me": "https://about.me/{}",
            "AngelList": "https://angel.co/{}",
            "Badoo": "https://badoo.com/profile/{}",
            "Behance": "https://www.behance.net/{}",
            "Blogger": "https://{}.blogspot.com",
            "CodePen": "https://codepen.io/{}",
            "CodeWars": "https://www.codewars.com/users/{}",
            "Couchsurfing": "https://www.couchsurfing.com/people/{}",
            "Dailymotion": "https://www.dailymotion.com/{}",
            "Deezer": "https://www.deezer.com/en/user/{}",
            "DeviantArt": "https://www.deviantart.com/{}",
            "Discord": "https://discord.com/users/{}",
            "Disqus": "https://disqus.com/by/{}",
            "Dribbble": "https://dribbble.com/{}",
            "Ello": "https://ello.co/{}",
            "Facebook": "https://www.facebook.com/{}",
            "Fiverr": "https://www.fiverr.com/{}",
            "Flickr": "https://www.flickr.com/people/{}",
            "Foursquare": "https://foursquare.com/user/{}",
            "GitHub": "https://github.com/{}",
            "GitLab": "https://gitlab.com/{}",
            "Giters": "https://giters.com/{}",
            "Giphy": "https://giphy.com/{}",
            "Goodreads": "https://www.goodreads.com/{}",
            "Groupon": "https://www.groupon.com/profile/{}",
            "Gumroad": "https://gumroad.com/{}",
            "HackerRank": "https://www.hackerrank.com/{}",
            "Instagram": "https://www.instagram.com/{}",
            "LinkedIn": "https://www.linkedin.com/in/{}",
            "Snapchat": "https://www.snapchat.com/add/{}",
            "TikTok": "https://www.tiktok.com/@{}",
            "Twitch": "https://www.twitch.tv/{}",
            "Twitter": "https://twitter.com/{}",
            "YouTube": "https://www.youtube.com/{}",
        }

        username = input(f"{Fore.RED}[*] {Fore.GREEN}Enter Username to Track: ").strip().lower()
        print(f"\n{Fore.RED}[*]{Fore.GREEN} Scanning for Username '{username}'... Please Wait.\n")

        start_time = time.time()
        session = requests.Session()
        total_sites = len(sites)
        found_sites = []
        checked_sites = 0

        for site, url_template in sites.items():
            checked_sites += 1
            url = url_template.format(username)
            print(f"{Fore.MAGENTA}[{checked_sites:2}/{total_sites}] Checking {site:<12} |   ", end="")

            try:
                response = session.get(url, timeout=5)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    page_title = soup.title.string.lower() if soup.title else ""
                    if username in page_title or username in response.text.lower():
                        found_sites.append(f"{site}: {url}")
                        print(f"{Fore.GREEN}[+] Found: {url}")
                    else:
                        print(f"{Fore.RED}[x] Not found")
                else:
                    print(f"{Fore.RED}[x] Not found")
            except requests.RequestException as e:
                print(f"{Fore.RED}[!] Error: {e}")

        # Summary
        elapsed_time = time.time() - start_time
        print("\n" + "-" * 50)
        print(f"{Fore.CYAN}Scan Complete in {elapsed_time:.2f} Seconds.")
        print(f"{Fore.CYAN}Total Sites Checked: {Fore.YELLOW}{total_sites}")
        print(f"{Fore.CYAN}Total Sites Found: {Fore.GREEN}{len(found_sites)}")
        if found_sites:
            print(f"\n{Fore.RED}[+] {Fore.GREEN}Sites Username '{username}' Was Found:")
            for site in found_sites:
                print(f"  {Fore.RED}{site}")
        else:
            print(f"\n{Fore.RED}[-] No Sites Found With the Username '{username}'.")
        print("-" * 50)

    except Exception as e:
        print(f"{Fore.RED}[!] An Unexpected Error Occurred: {e}")

                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
if __name__ == "__main__":
    run()