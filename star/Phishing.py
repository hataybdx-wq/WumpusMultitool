import os
import urllib.request
import re
from urllib.parse import urljoin
from html import escape
import socket
import colorama
from colorama import Fore
import os
import subprocess
import time
import webbrowser
import os
import urllib.request
import re
from urllib.parse import urljoin
import html
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
    return time.strftime("%H:%M:%S")


def ErrorModule(e):
    print(f"Error in module: {e}")


def ErrorUrl(status=None):
    if status:
        print(f"Error: Unable to retrieve the URL. HTTP Status Code: {status}")
    else:
        print("Error: Unable to retrieve the URL.")


def Continue():
    input("Press Enter to continue...")

def Reset():
    print("Resetting...")

def css_and_js(html_content, base_url):
    soup = html.unescape(html_content)
    css_links = re.findall(r'<link\s+rel="stylesheet"\s+href="([^"]+)"', soup)
    all_css = ""
    
    for link in css_links:
        css_url = urljoin(base_url, link)
        try:
            with urllib.request.urlopen(css_url) as response:
                css_data = response.read().decode('utf-8')
                all_css += css_data + "\n"
        except:
            print("Error retrieving CSS.")

    if all_css:
        soup = re.sub(r'(<head.*?>)', r'\1<style>' + html.escape(all_css) + '</style>', soup, flags=re.DOTALL)

    script_links = re.findall(r'<script\s+src="([^"]+)"', soup)
    all_js = ""
    
    for script in script_links:
        js_url = urljoin(base_url, script)
        try:
            with urllib.request.urlopen(js_url) as response:
                js_data = response.read().decode('utf-8')
                all_js += js_data + "\n"
        except:
            print("Error retrieving JavaScript.")

    if all_js:
        soup = re.sub(r'(<body.*?>)', r'\1<script>' + html.escape(all_js) + '</script>', soup, flags=re.DOTALL)

    return soup


def phishing_attack():

    website_url = input(f"\n{current_time_hour()} Input Website Url -> ")
    
    if "https://" not in website_url and "http://" not in website_url:
        website_url = "https://" + website_url

    print(f"{current_time_hour()} Retrieving HTML content...")
    try:
        with urllib.request.urlopen(website_url) as response:
            html_content = response.read().decode('utf-8')
            file_name = re.sub(r'[\\/:*?"<>|]', '-', re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE).group(1) if re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE) else 'Phishing')


            output_dir = os.path.join(os.getcwd(), "PhishingAttack")
            os.makedirs(output_dir, exist_ok=True)
            file_html = os.path.join(output_dir, f"{file_name}.html")


            final_html = css_and_js(html_content, website_url)


            with open(file_html, 'w', encoding='utf-8') as file:
                file.write(final_html)

            print(f"{current_time_hour()} Phishing attack successful. The file is located at: {file_html}")
            Continue()
            Reset()

    except urllib.error.HTTPError as e:
        ErrorUrl(e.code)
    except Exception as e:
        ErrorModule(e)


if __name__ == "__main__":
    try:
        phishing_attack()
    except Exception as e:
        ErrorModule(e)

