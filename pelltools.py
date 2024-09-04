import os
import sys
import time
import socket
import platform
import subprocess
import shutil
import qrcode

# Color Definitions
BLUE = '\033[94m'
WHITE = '\033[97m'
RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def center_text(text, width):
    return text.center(width)

def print_banner():
    banner = """
    ██████╗ ███████╗██╗     ██╗     ███████╗████████╗ ██████╗  ██████╗ ██╗     
    ██╔══██╗██╔════╝██║     ██║     ██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     
    ██████╔╝█████╗  ██║     ██║     █████╗     ██║   ██║   ██║██║   ██║██║     
    ██╔═══╝ ██╔══╝  ██║     ██║     ██╔══╝     ██║   ██║   ██║██║   ██║██║     
    ██║     ███████╗███████╗███████╗███████╗   ██║   ╚██████╔╝╚██████╔╝███████╗
    ╚═╝     ╚══════╝╚══════╝╚══════╝╚══════╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                  Dev by Rell                                  
    """
    width = shutil.get_terminal_size().columns
    centered_banner = "\n".join([center_text(line, width) for line in banner.split("\n")])
    print(f'{BLUE}{centered_banner}{RESET}')

def print_menu():
    width = shutil.get_terminal_size().columns
    column_width = 45  # Adjusted for longer option names
    padding = 2

    categories = [
        ("Network Tools", [
            "1.1. IP Pinger",
            "1.2. Port Scanner",
            "1.3. Retrieve IP from Site",
            "1.4. Traceroute",
            "1.5. MAC Address Lookup",
            "1.6. DNS Lookup",
            "1.7. SSL Certificate Checker",  # New option
        ]),
        ("Security Tools", [
            "2.1. WHOIS Lookup",
            "2.2. IP Geolocation",
            "2.3. Packet Sniffer",
            "2.4. Domain Typo-Squatting",
            "2.5. Reverse DNS Lookup",
            "2.6. Vulnerability Scanner",
            "2.7. Brute Force Attack Simulator",  # New option
        ]),
        ("Encoding/Decoding Tools", [
            "3.1. Convert to Base64",
            "3.2. Hash Generator",
            "3.3. URL Encoder/Decoder",
            "3.4. JWT Decoder",  # New option
            "3.5. ROT13 Encoder/Decoder",  # New option
            "3.6. Morse Code Translator",  # New option
        ]),
        ("System Information", [
            "4.1. System Info",
            "4.2. Network Speed Test",
            "4.3. Encrypted File Transfer",
            "4.4. Social Engineering Risk Analyzer",
            "4.5. Active Directory Enumeration",  # New option
            "4.6. Docker Container Manager",  # New option
            "4.7. Virtual Machine Monitor",  # New option
        ]),
        ("Advanced Tools", [
            "5.1. Generate Password",
            "5.2. Clear Screen",
            "5.3. Generate QR Code",
            "5.4. Blockchain Analysis",
            "5.5. IoT Device Manager",
            "5.6. Data Anonymization Tool",  # New option
            "5.7. Dark Web Scraper",  # New option
        ]),
        ("0. Exit", [])
    ]

    max_rows = max(len(items) for _, items in categories)
    
    menu_str = ""

    for row in range(max_rows):
        line = ""
        for (title, items) in categories:
            if row < len(items):
                line += f"{BLUE}{items[row]:<{column_width}}{RESET}"
            else:
                line += " " * column_width
        menu_str += line.rstrip() + "\n"
    
    menu_str = f"{BLUE}Menu:{RESET}\n{menu_str}".strip()
    print_boxed_text(menu_str, width)

def print_boxed_text(text, width):
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    box_width = max_len + 4  # 2 spaces on each side

    top_border = '┌' + '─' * (box_width - 2) + '┐'
    bottom_border = '└' + '─' * (box_width - 2) + '┘'

    print(center_text(f"{BLUE}{top_border}{RESET}", width))
    for line in lines:
        print(center_text(f"│ {BLUE}{line.ljust(max_len)}{RESET} │", width))
    print(center_text(f"{BLUE}{bottom_border}{RESET}", width))

# Unified Menu and Tools

def main_menu():
    while True:
        clear_screen()
        print_banner()
        print_menu()
        
        width = shutil.get_terminal_size().columns
        username_pc = os.getlogin()  # Get the current username
        menu_number = '1'  # You can set this dynamically if needed

        choice = input(f"""{BLUE}┌───({WHITE}{username_pc}@pelltols)─{BLUE}[{WHITE}~/pell tools/Menu-{menu_number}]{BLUE}
└──{WHITE}$ {RESET}""").strip()

        if choice == '1.1':
            ip = input(center_text("Enter IP to ping: ", width))
            ip_pinger(ip)
        elif choice == '1.2':
            ip = input(center_text("Enter IP to scan: ", width))
            ports = input(center_text("Enter ports (comma-separated): ", width))
            port_list = list(map(int, ports.split(',')))
            port_scanner(ip, port_list)
        elif choice == '1.3':
            site = input(center_text("Enter site to retrieve IP: ", width))
            ip_from_site(site)
        elif choice == '1.4':
            ip = input(center_text("Enter IP for traceroute: ", width))
            traceroute(ip)
        elif choice == '1.5':
            ip = input(center_text("Enter IP for MAC address lookup: ", width))
            mac_address_lookup(ip)
        elif choice == '1.6':
            domain = input(center_text("Enter domain for DNS lookup: ", width))
            dns_lookup(domain)
        elif choice == '1.7':
            domain = input(center_text("Enter domain for SSL Certificate check: ", width))
            ssl_certificate_checker(domain)
        elif choice == '2.1':
            domain = input(center_text("Enter domain for WHOIS Lookup: ", width))
            whois_lookup(domain)
        elif choice == '2.2':
            ip = input(center_text("Enter IP for geolocation: ", width))
            ip_geolocation(ip)
        elif choice == '2.3':
            interface = input(center_text("Enter network interface for packet sniffing: ", width))
            packet_sniffer(interface)
        elif choice == '2.4':
            domain = input(center_text("Enter domain for typo-squatting check: ", width))
            domain_typo_squatting(domain)
        elif choice == '2.5':
            ip = input(center_text("Enter IP for reverse DNS lookup: ", width))
            reverse_dns_lookup(ip)
        elif choice == '2.6':
            ip = input(center_text("Enter IP for vulnerability scanning: ", width))
            scan_for_vulnerabilities(ip)
        elif choice == '2.7':
            url = input(center_text("Enter URL for brute force attack simulation: ", width))
            brute_force_attack_simulator(url)
        elif choice == '3.1':
            convert_text_base64()
        elif choice == '3.2':
            calculate_hash()
        elif choice == '3.3':
            url_encoder_decoder()
        elif choice == '3.4':
            jwt_decoder()
        elif choice == '3.5':
            rot13_encoder_decoder()
        elif choice == '3.6':
            morse_code_translator()
        elif choice == '4.1':
            system_info()
        elif choice == '4.2':
            network_speed_test()
        elif choice == '4.3':
            encrypted_file_transfer()
        elif choice == '4.4':
            social_engineering_analyzer()
        elif choice == '4.5':
            active_directory_enumeration()
        elif choice == '4.6':
            docker_container_manager()
        elif choice == '4.7':
            virtual_machine_monitor()
        elif choice == '5.1':
            generate_password()
        elif choice == '5.2':
            clear_screen()
        elif choice == '5.3':
            data = input(center_text("Enter data for QR code: ", width))
            generate_qr_code(data)
        elif choice == '5.4':
            blockchain_analysis()
        elif choice == '5.5':
            iot_device_manager()
        elif choice == '5.6':
            data_anonymization_tool()
        elif choice == '5.7':
            dark_web_scraper()
        elif choice == '0':
            print(center_text("Goodbye!", width))
            sys.exit()
        else:
            print(center_text("Invalid option, please try again.", width))
            time.sleep(2)

# Example placeholder function implementations
def ip_pinger(ip):
    width = shutil.get_terminal_size().columns
    print_boxed_text(f"Pinging {ip}...", width)
    response = os.system(f"ping -c 4 {ip}")
    if response == 0:
        print_boxed_text(f"{ip} is reachable", width)
    else:
        print_boxed_text(f"{ip} is not reachable", width)
    input(center_text("Press Enter to continue...", width))

def generate_qr_code(data):
    img = qrcode.make(data)
    img.save("qr_code.png")
    width = shutil.get_terminal_size().columns
    print(center_text(f"{BLUE}\nQR Code generated and saved as qr_code.png\n{RESET}", width))

def vulnerability_scanner(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"{BLUE}Port {port}: Open{RESET}")
        else:
            print(f"{BLUE}Port {port}: Closed{RESET}")
        sock.close()
    except Exception as e:
        print(f"{BLUE}Could not scan port {port}: {e}{RESET}")

def scan_for_vulnerabilities(ip):
    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3389]
    width = shutil.get_terminal_size().columns
    print_boxed_text(f"{BLUE}Scanning {ip} for common vulnerabilities...{RESET}", width)
    for port in common_ports:
        vulnerability_scanner(ip, port)
    print(center_text(f"{BLUE}\nScanning completed.{RESET}", width))

# Placeholder for the new functions
def encrypted_file_transfer():
    pass

def social_engineering_analyzer():
    pass

def blockchain_analysis():
    pass

def iot_device_manager():
    pass

def port_scanner(ip, ports):
    pass

def ip_from_site(site):
    pass

def traceroute(ip):
    pass

def mac_address_lookup(ip):
    pass

def dns_lookup(domain):
    pass

def whois_lookup(domain):
    pass

def ip_geolocation(ip):
    pass

def packet_sniffer(interface):
    pass

def domain_typo_squatting(domain):
    pass

def reverse_dns_lookup(ip):
    pass

def convert_text_base64():
    pass

def calculate_hash():
    pass

def url_encoder_decoder():
    pass

def system_info():
    pass

def network_speed_test():
    pass

def generate_password():
    pass

def ssl_certificate_checker(domain):
    pass

def brute_force_attack_simulator(url):
    pass

def jwt_decoder():
    pass

def rot13_encoder_decoder():
    pass

def morse_code_translator():
    pass

def active_directory_enumeration():
    pass

def docker_container_manager():
    pass

def virtual_machine_monitor():
    pass

def data_anonymization_tool():
    pass

def dark_web_scraper():
    pass

if __name__ == "__main__":
    main_menu()

