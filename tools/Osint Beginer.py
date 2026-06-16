import os
import time
import fade
from colorama import Fore, Style
try:
    from googlesearch import search
except ImportError:
    print("[ERROR] Le module 'googlesearch' n'est pas installé. Installez-le avec: pip install google-search-results")
    exit(1)

class Color:
    RED = Fore.RED + Style.BRIGHT
    GREEN = Fore.GREEN + Style.BRIGHT
    WHITE = Fore.WHITE + Style.BRIGHT
    RESET = Fore.RESET + Style.RESET_ALL

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ret():
    input(Color.WHITE + f'\n[*] Press {Color.RED}ENTER{Color.WHITE} to return: ' + Color.RESET)
    main()

def error(text):
    print(Color.WHITE + f'\n[*] Error {Color.RED}OSINT{Color.WHITE}: ' + Color.RED + text + Color.RESET)
    ret()

def fetch_top_search_results(query, num_results=10):
    search_results = []
    try:
        for result in search(query, num_results=num_results):
            search_results.append(result)
    except Exception as e:
        print(f"{Color.RED}Error : {e}{Color.RESET}")
    return search_results

def main():
    clear()
    title = '''                                       
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
                          
'''
    print(fade.fire(title))

    search_query = input(Color.WHITE + "  [*] Search: " + Color.RESET).strip()
    if not search_query:
        print(f"{Color.RED}  [*] Error{Color.RESET}")
        ret()
        return

    print('\n')
    top_results = fetch_top_search_results(search_query, num_results=10)

    if not top_results:
        print(f"{Color.RED}  [*] No result(s) or error.{Color.RESET}")
    else:
        print(Color.WHITE + "  [*] Result: " + '\n')
        for idx, result in enumerate(top_results, 1):
            print(f"{Color.GREEN}  [{Color.WHITE}{idx}{Color.GREEN}] {result}{Color.RESET}")

    ret()

if __name__ == '__main__':
    main()
