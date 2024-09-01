import os
import sys
import time
import socket
import platform
import subprocess
import requests

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_effect(text, speed=0.01):
    for char in text:
        sys.stdout.write(f'\033[92m{char}\033[0m')  # Texte en vert
        sys.stdout.flush()
        time.sleep(speed)
    print()

def print_banner():
    banner = """
    ╔════════════════════════════════════════════════════════════════════════════╗
    ║                                                                            ║
    ║  ██████╗ ███████╗██╗     ██╗     ███████╗████████╗ ██████╗  ██████╗ ██╗     ║
    ║  ██╔══██╗██╔════╝██║     ██║     ██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     ║
    ║  ██████╔╝█████╗  ██║     ██║     █████╗     ██║   ██║   ██║██║   ██║██║     ║
    ║  ██╔═══╝ ██╔══╝  ██║     ██║     ██╔══╝     ██║   ██║   ██║██║   ██║██║     ║
    ║  ██║     ███████╗███████╗███████╗███████╗   ██║   ╚██████╔╝╚██████╔╝███████╗║
    ║  ╚═╝     ╚══════╝╚══════╝╚══════╝╚══════╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝║
    ║                                                                            ║
    ╚════════════════════════════════════════════════════════════════════════════╝
    """
    typewriter_effect(banner, speed=0.005)

def ip_pinger(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip]
    response = subprocess.run(command, stdout=subprocess.PIPE)
    if response.returncode == 0:
        typewriter_effect(f"\nL'IP {ip} est accessible.\n")
    else:
        typewriter_effect(f"\nL'IP {ip} est inaccessible.\n")

def port_scanner(ip, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    if open_ports:
        typewriter_effect(f"\nPorts ouverts sur {ip}: {', '.join(map(str, open_ports))}\n")
    else:
        typewriter_effect(f"\nAucun port ouvert trouvé sur {ip}.\n")

def ip_from_site(site):
    try:
        ip_address = socket.gethostbyname(site)
        typewriter_effect(f"\nL'adresse IP de {site} est {ip_address}\n")
    except socket.gaierror:
        typewriter_effect(f"\nLe site {site} est introuvable.\n")

def name_lookup(name):
    try:
        response = requests.get(f"https://api.name.com/v4/domains:search?query={name}")
        if response.status_code == 200:
            data = response.json()
            typewriter_effect(f"\nInformation sur {name}: {data}\n")
        else:
            typewriter_effect("\nErreur lors de la récupération des informations.\n")
    except Exception as e:
        typewriter_effect(f"\nUne erreur s'est produite: {e}\n")

def ip_lookup(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        if response.status_code == 200:
            data = response.json()
            typewriter_effect(f"\nInformation sur {ip}: {data}\n")
        else:
            typewriter_effect("\nErreur lors de la récupération des informations.\n")
    except Exception as e:
        typewriter_effect(f"\nUne erreur s'est produite: {e}\n")

def whois_lookup(domain):
    try:
        response = subprocess.run(['whois', domain], capture_output=True, text=True)
        typewriter_effect(f"\nWHOIS Information pour {domain}:\n")
        typewriter_effect(response.stdout)
    except Exception as e:
        typewriter_effect(f"\nUne erreur s'est produite: {e}\n")

def generate_password():
    import random
    import string
    length = int(input("\nEntrez la longueur du mot de passe: "))
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    typewriter_effect(f"\nVotre mot de passe généré: {password}\n")

def convert_text_base64():
    import base64
    text = input("\nEntrez le texte à convertir en Base64: ")
    encoded = base64.b64encode(text.encode())
    typewriter_effect(f"\nTexte en Base64: {encoded.decode()}\n")

def calculate_hash():
    import hashlib
    text = input("\nEntrez le texte à hasher: ")
    hash_type = input("Entrez le type de hash (md5/sha1/sha256): ").lower()

    if hash_type == 'md5':
        hash_object = hashlib.md5(text.encode())
    elif hash_type == 'sha1':
        hash_object = hashlib.sha1(text.encode())
    elif hash_type == 'sha256':
        hash_object = hashlib.sha256(text.encode())
    else:
        typewriter_effect("\nType de hash non supporté.")
        return

    typewriter_effect(f"\nHash {hash_type}: {hash_object.hexdigest()}\n")

def main_menu():
    while True:
        clear_screen()
        print_banner()

        menu = """
                            ─── MENU ───

        ┌───────────────────────────┬───────────────────────────┬───────────────────────────┐
        │        Réseaux            │        OSINT              │        Utilitaires        │
        ├───────────────────────────┼───────────────────────────┼───────────────────────────┤
        │ 1. IP Pinger              │ 4. Name Lookup            │ 7. Générer mot de passe   │
        │ 2. IP Port Scanner        │ 5. IP Lookup              │ 8. Convertir texte (Base64)│
        │ 3. Récupérer IP d'un site │ 6. WHOIS Lookup           │ 9. Calculer hash (MD5/SHA)│
        └───────────────────────────┴───────────────────────────┴───────────────────────────┘
        
                            0. Quitter
        """
        typewriter_effect(menu, speed=0.005)

        choice = input("\033[92mChoisissez une option: \033[0m")

        if choice == '1':
            ip = input("\nEntrez l'IP à pinger: ")
            ip_pinger(ip)
        elif choice == '2':
            ip = input("\nEntrez l'IP à scanner: ")
            ports = input("Entrez les ports à scanner (séparés par des virgules): ")
            port_list = list(map(int, ports.split(',')))
            port_scanner(ip, port_list)
        elif choice == '3':
            site = input("\nEntrez le site (ex: google.com): ")
            ip_from_site(site)
        elif choice == '4':
            name = input("\nEntrez le nom à rechercher: ")
            name_lookup(name)
        elif choice == '5':
            ip = input("\nEntrez l'IP à rechercher: ")
            ip_lookup(ip)
        elif choice == '6':
            site = input("\nEntrez le domaine pour WHOIS Lookup: ")
            whois_lookup(site)
        elif choice == '7':
            generate_password()
        elif choice == '8':
            convert_text_base64()
        elif choice == '9':
            calculate_hash()
        elif choice == '0':
            typewriter_effect("\nFermeture du programme...")
            break
        else:
            typewriter_effect("\nOption invalide. Veuillez réessayer.")

        input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main_menu()
