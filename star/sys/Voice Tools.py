import os
import time
import asyncio
import json
import random
from time import sleep
from json import loads, dumps
from websocket import WebSocket
from concurrent.futures import ThreadPoolExecutor
import websockets
from pystyle import Center, Colorate, Colors, Anime
import colorama
import requests
import subprocess

os.system('cls' if os.name == 'nt' else 'clear')
print(Colorate.Vertical(Colors.yellow_to_red,"""
                                                                    
                    (       (                   )\\ )         (     
                     ( )\\    ( )\\  (  (  (     )  (()/(   ) (   )\\ )  
                    )((_)  ))((_)))\\ )\\))( ( /(   /(_)| /( )\\ (()/(  
                   ((_)_  /((_) /((_|(_))\\ )(_)) (_)) )(_)|(_) ((_)) 
                    | _ )(_))| (_))( (()(_|(_)_  | _ ((_)_ (_) _| |  
                    | _ \\/ -_) | || / _ |/ _ | |   / _ || / _ |  
                    |___/\\___|_|\\_,_\\__, |\\__,_| |_|_\\__,_||_\\__,_|  
                                     |___/     
                                               
                ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                ┃ Author : Ace | Adwares      ┃
                ┃ Discord: .gg/leak-internet  ┃
                ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛     
                        
"""))

input_folder = 'input'
tokens_path = os.path.join(input_folder, 'tokens.txt')

if not os.path.exists(tokens_path):
    print(f"[ERREUR] Le fichier '{tokens_path}' est introuvable. Assurez-vous qu'il existe.")
    exit()

with open(tokens_path, 'r') as f:
    tokens = [line.strip() for line in f if line.strip()]

if not tokens:
    print("[ERREUR] Aucun token trouvé dans le fichier.")
    exit()

print("1 - Join voice")
print("2 - Voice spam")
print("3 - Loop mute/cam/stream toggle")
print("4 - Loop mute/cam/stream toggle with leave/join")
print("5 - Custom")
print("6 - Exit")
choice = int(input("\nChoice: "))

if choice == 1:
    server_id = input("Server ID: ")
    channel_id = input("Channel ID: ")

    async def connect(token):
        async with websockets.connect('wss://gateway.discord.gg/?v=9&encoding=json') as websocket:
            hello = await websocket.recv()
            hello_json = json.loads(hello)
            heartbeat_interval = hello_json['d']['heartbeat_interval']
            await websocket.send(json.dumps({
                'op': 2,
                'd': {
                    'token': token,
                    'properties': {'os': 'windows', 'browser': 'Discord', 'device': 'desktop'}
                }
            }))
            await websocket.send(json.dumps({
                'op': 4,
                'd': {
                    'guild_id': server_id,
                    'channel_id': channel_id,
                    'self_mute': False,
                    'self_deaf': False
                }
            }))
            while True:
                await asyncio.sleep(heartbeat_interval / 1000)
                try:
                    await websocket.send(json.dumps({'op': 1, 'd': None}))
                except Exception:
                    break

    async def main():
        tasks = [asyncio.create_task(connect(token)) for token in tokens]
        await asyncio.gather(*tasks)

    asyncio.run(main())

elif choice == 2:
    server = input("Server ID: ")
    channel = input("Channel ID: ")
    default_values = {}

    for field in ['Deaf', 'Mute', 'Stream', 'Video']:
        val = input(f"{field}: (y/n) ")
        default_values[field.lower()] = val.lower() == 'y'

    executor = ThreadPoolExecutor(max_workers=1000)

    def run(token):
        ws = WebSocket()
        ws.connect('wss://gateway.discord.gg/?v=8&encoding=json')
        hello = loads(ws.recv())
        heartbeat_interval = hello['d']['heartbeat_interval']

        ws.send(dumps({
            'op': 2,
            'd': {
                'token': token,
                'properties': {'os': 'windows', 'browser': 'Discord', 'device': 'desktop'}
            }
        }))
        ws.send(dumps({
            'op': 4,
            'd': {
                'guild_id': server,
                'channel_id': channel,
                'self_mute': default_values['mute'],
                'self_deaf': default_values['deaf'],
                'self_stream': default_values['stream'],
                'self_video': default_values['video']
            }
        }))

        while True:
            sleep(1)
            ws.send(dumps({
                'op': 4,
                'd': {
                    'guild_id': server,
                    'channel_id': None,
                    'self_mute': default_values['mute'],
                    'self_deaf': default_values['deaf'],
                    'self_stream': default_values['stream'],
                    'self_video': default_values['video']
                }
            }))
            sleep(1)
            ws.send(dumps({
                'op': 4,
                'd': {
                    'guild_id': server,
                    'channel_id': channel,
                    'self_mute': default_values['mute'],
                    'self_deaf': default_values['deaf'],
                    'self_stream': default_values['stream'],
                    'self_video': default_values['video']
                }
            }))

    print(f"Total Tokens: {len(tokens)}")
    for token in tokens:
        executor.submit(run, token)
        print("[+] Joined voice channel")
        sleep(random.uniform(0.1, 0.1))

elif choice == 3:
    server = input("Server ID: ")
    channel = input("Channel ID: ")
    executor = ThreadPoolExecutor(max_workers=1000)

    def toggle_all(token):
        ws = WebSocket()
        ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')
        hello = loads(ws.recv())
        ws.send(dumps({
            'op': 2,
            'd': {
                'token': token,
                'properties': {'os': 'windows', 'browser': 'Discord', 'device': 'desktop'}
            }
        }))

        mute = False
        cam = False
        stream = False

        while True:
            if random.random() > 0.5:
                mute = not mute
            if random.random() > 0.5:
                cam = not cam
            if random.random() > 0.5:
                stream = not stream

            ws.send(dumps({
                'op': 4,
                'd': {
                    'guild_id': server,
                    'channel_id': channel,
                    'self_mute': mute,
                    'self_deaf': False,
                    'self_stream': stream,
                    'self_video': cam
                }
            }))

            print(f"[{token[:5]}...] Mute: {mute} | Cam: {cam} | Stream: {stream}")
            sleep(random.uniform(1, 3)) 

    for token in tokens:
        executor.submit(toggle_all, token)

elif choice == 4:
    server = input("Server ID: ")
    channel = input("Channel ID: ")
    executor = ThreadPoolExecutor(max_workers=1000)

    def toggle_all_with_leave_and_join(token):
        ws = WebSocket()
        ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')
        hello = loads(ws.recv())
        ws.send(dumps({
            'op': 2,
            'd': {
                'token': token,
                'properties': {'os': 'windows', 'browser': 'Discord', 'device': 'desktop'}
            }
        }))

        mute = False
        cam = False
        stream = False

        while True:

            if random.random() > 0.5:
                mute = not mute
            if random.random() > 0.5:
                cam = not cam
            if random.random() > 0.5:
                stream = not stream

            ws.send(dumps({
                'op': 4,
                'd': {
                    'guild_id': server,
                    'channel_id': channel,  
                    'self_mute': mute,
                    'self_deaf': False,
                    'self_stream': stream,
                    'self_video': cam
                }
            }))
            print(f"[{token[:5]}...] Rejoined Channel - Mute: {mute} | Cam: {cam} | Stream: {stream}")
            sleep(random.uniform(1, 3))  

            ws.send(dumps({
                'op': 4,
                'd': {
                    'guild_id': server,
                    'channel_id': None, 
                    'self_mute': mute,
                    'self_deaf': False,
                    'self_stream': stream,
                    'self_video': cam
                }
            }))
            print(f"[{token[:5]}...] Left Channel - Mute: {mute} | Cam: {cam} | Stream: {stream}")
            sleep(random.uniform(1, 3))  

    for token in tokens:
        executor.submit(toggle_all_with_leave_and_join, token)

elif choice == 5:
    import threading

    server_id = input("Server ID: ")
    channel_id = input("Channel ID: ")

    try:
        count = int(input(f"How many tokens to use? (max {len(tokens)}): "))
        if count > len(tokens):
            raise ValueError
    except ValueError:
        print("Invalid number.")
        exit()

    def yesno(prompt):
        return input(prompt + " (y/n): ").strip().lower() == 'y'

    mute = yesno("Mute?")
    cam = yesno("Enable Camera?")
    stream = yesno("Enable Streaming?")
    refresh_delay = int(input("Refresh every X seconds (ex: 10): "))

    selected_tokens = random.sample(tokens, count)
    executor = ThreadPoolExecutor(max_workers=1000)

    def custom_join_and_refresh(token):
        try:
            ws = WebSocket()
            ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')
            hello = loads(ws.recv())
            ws.send(dumps({
                'op': 2,
                'd': {
                    'token': token,
                    'properties': {'os': 'windows', 'browser': 'Discord', 'device': 'desktop'}
                }
            }))
            ws.send(dumps({
                'op': 4,
                'd': {
                    'guild_id': server_id,
                    'channel_id': channel_id,
                    'self_mute': mute,
                    'self_deaf': False,
                    'self_stream': stream,
                    'self_video': cam
                }
            }))
            print(f"[{token[:5]}...] Joined voice with mute={mute}, cam={cam}, stream={stream}")

            while True:
                sleep(refresh_delay)
                ws.send(dumps({
                    'op': 4,
                    'd': {
                        'guild_id': server_id,
                        'channel_id': channel_id,
                        'self_mute': mute,
                        'self_deaf': False,
                        'self_stream': stream,
                        'self_video': cam
                    }
                }))
                print(f"[{token[:5]}...] Refreshed cam/stream/mute state")
        except Exception as e:
            print(f"[{token[:5]}...] Erreur: {str(e)}")

    for token in selected_tokens:
        executor.submit(custom_join_and_refresh, token)
        sleep(0.2)

elif choice == 6:
    print("Goodbye!")
    exit()

else:
    print("Invalid input. Please try again.")
