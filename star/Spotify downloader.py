try:
	import re, asyncio, aiohttp
	from bs4 import BeautifulSoup as bs
	from yt_dlp import YoutubeDL
except:
	import os
	os.system("pip install colorama, yt-dlp aiohttp beautifulsoup4")

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
async def main():
    u = input("Spotify URL: ")
    t = re.search(r'track/(\w+)', u).group(1)
    async with aiohttp.ClientSession() as s:
        async with s.get(f'https://open.spotify.com/track/{t}', headers={'User-Agent':'Mozilla/5.0'}) as r:
            soup = bs(await r.text(), 'html.parser')
            title_tag = soup.title.string
            if ' - title and lyrics by ' in title_tag:
                n, a = title_tag.split('song and lyrics by')
                a = a.split(' | Spotify')[0].strip()
            else:
                n = title_tag.split(' | Spotify')[0].strip()
                a = ''
    opts = {'format':'bestaudio', 'outtmpl':f'{n}.mp3', 'forcefilename':True}
    with YoutubeDL(opts) as ydl: ydl.download([f'ytsearch1:"{n} {a}"'])

asyncio.run(main())