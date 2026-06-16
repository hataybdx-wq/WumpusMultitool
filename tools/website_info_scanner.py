import socket
import concurrent.futures
import requests
from urllib.parse import urlparse
import ssl
import urllib3
from requests.exceptions import RequestException
import time
import dns.resolver
from bs4 import BeautifulSoup
import whois
from colorama import Fore, init
                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
init(autoreset=True)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def current_time_hour():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def website_info_scanner(website_url):
    if not urlparse(website_url).scheme:
        website_url = "https://" + website_url

    print(f"{Fore.RED}[+] {Fore.GREEN}Scanning Website: {Fore.CYAN}{website_url}")

    def website_domain(website_url):
        parsed_url = urlparse(website_url)
        domain = parsed_url.netloc or website_url
        print(f"{Fore.RED}[+] {Fore.GREEN}Domain: {Fore.CYAN}{domain}")
        return domain

    def website_ip(domain):
        try:
            ip = socket.gethostbyname(domain)
            print(f"{Fore.RED}[+] {Fore.GREEN}IP: {Fore.CYAN}{ip}")
            return ip
        except socket.gaierror:
            print(f"{Fore.RED}[!] {Fore.YELLOW}Error: Unable to Resolve IP for {Fore.CYAN}{domain}")
            return None

    def ip_type(ip):
        if ':' in ip:
            ip_type = "IPv6"
        elif '.' in ip:
            ip_type = "IPv4"
        else:
            ip_type = "Unknown"
        print(f"{Fore.RED}[+] {Fore.GREEN}IP Type: {Fore.CYAN}{ip_type}")

    def website_secure(website_url):
        secure = website_url.startswith("https://")
        print(f"{Fore.RED}[+] {Fore.GREEN}Secure: {Fore.CYAN}{secure}")

    def website_status(website_url):
        try:
            response = requests.get(website_url, timeout=5, verify=False)
            status_code = response.status_code
            print(f"{Fore.RED}[+] {Fore.GREEN}Status Code: {Fore.CYAN}{status_code}")
        except RequestException as e:
            print(f"{Fore.RED}[!] {Fore.YELLOW}Error: Unable to get Status for {Fore.CYAN}{website_url} ({e})")

    def ip_info(ip):
        if not ip:
            return
        api_url = f"https://ipinfo.io/{ip}/json"
        try:
            response = requests.get(api_url, timeout=5)
            api = response.json()
            for key, value in api.items():
                print(f"{Fore.RED}[+] {Fore.GREEN}{key.capitalize()}: {Fore.CYAN}{value}")
        except RequestException as e:
            print(f"{Fore.RED}[!] {Fore.YELLOW}Error: Unable to get IP Info for {Fore.CYAN}{ip} ({e})")

    def website_port(ip):
        if not ip:
            return
        port_protocol_map = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 80: "HTTP", 443: "HTTPS"
        }
        port_list = [21, 22, 23, 25, 53, 80, 443]

        def scan_port(ip, port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    protocol = port_protocol_map.get(port, "Unknown")
                    print(f"{Fore.RED}[+] {Fore.GREEN}Port: {Fore.CYAN}{port} {Fore.GREEN}Status: {Fore.CYAN}Open {Fore.GREEN}Protocol: {Fore.CYAN}{protocol}")
                sock.close()
            except Exception:
                pass

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(lambda port: scan_port(ip, port), port_list)

    domain = website_domain(website_url)
    ip = website_ip(domain)
    if ip:
        ip_type(ip)
        website_secure(website_url)
        website_status(website_url)
        ip_info(ip)
        website_port(ip)

def run():
    website_url = input(f"{Fore.RED}[*] {Fore.GREEN}Enter Target Website/URL: {Fore.RESET}").strip()
    if not website_url:
        print(f"{Fore.RED}[!] {Fore.YELLOW}Invalid Website/URL. Exiting...")
        return
    website_info_scanner(website_url)

                                                                                                                                                                                                                                                                                                                         #                                                                                                                         --  PLEASE DO NOT REMOVE THIS LINE  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  DO NOT CHANGE CODE AND BRAND AS YOUR OWN WITHOUT GIVING CREDITS TO ORIGINAL  --  OFFICIAL REPO: https://github.com/RPxGoon/3TH1C4L-MultiTool  --  PLEASE DO NOT REMOVE THIS LINE  --
if __name__ == "__main__":
    run()