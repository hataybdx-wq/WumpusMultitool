import requests
from colorama import Fore, init
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
init(autoreset=True)

def run():
    ip_address = input(f"{Fore.RED}[*] {Fore.GREEN}Enter Target IP Address: {Fore.RESET}")
    print()
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        data = response.json()
        
        for key, value in data.items():
            print(f"{Fore.RED}[+] {Fore.GREEN}{key.capitalize():<12}: {Fore.RED}{value}")
            
    except Exception as e:
        print(f"{Fore.RED}[!] {Fore.YELLOW}Error Fetching IP Information: {e}")

                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
if __name__ == "__main__":
    run()