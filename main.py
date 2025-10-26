import socket
import time
import os

ascii_art = [
    " ____   ___  ____ _____   ____   ____    _    _   _ _   _ _____ ____  ",
    "|  _ \\ / _ \\|  _ \\_   _| / ___| / ___|  / \\  | \\ | | \\ | | ____|  _ \\ ",
    "| |_) | | | | |_) || |   \\___ \\| |     / _ \\ |  \\| |  \\| |  _| | |_) |",
    "|  __/| |_| |  _ < | |    ___) | |___ / ___ \\| |\\  | |\\  | |___|  _ < ",
    "|_|    \\___/|_| \\_\\|_|   |____/ \\____/_/   \\_\\_| \\_|_| \\_|_____|_| \\_\\"
]

options = [
    "1. Scan by IP Address",
    "2. Scan by Hostname",
    "3. Custom Port Range Scan",
    "4. Exit"
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def spell_out_art(lines, delay=0.1):
    for line in lines:
        print(line)
        time.sleep(delay)

def scan_ports(target, start_port=1, end_port=1024):
    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((target, port))
                if result == 0:
                    print(f"\033[92m[OPEN] Port {port}\033[0m")
                else:
                    print(f"\033[91m[CLOSED] Port {port}\033[0m")
        except Exception as e:
            print(f"\033[93m[ERROR] Port {port}: {e}\033[0m")

def menu():
    while True:
        clear()
        spell_out_art(ascii_art)
        print("\n                   Author: Shane Green (ShaneYLad)\n")
        time.sleep(0.5)

        print("Select Scan Type:\n")
        for option in options:
            print(option)
            time.sleep(0.1)

        input_choice = input("\nEnter choice (1-4): ")

        if input_choice == "1":
            targetIp = input("\nEnter Target IP Address: ")
            scan_ports(targetIp)
        elif input_choice == "2":
            targetHostName = input("\nEnter Target Hostname: ")
            try:
                targetIp = socket.gethostbyname(targetHostName)
                print(f"\nResolved {targetHostName} to {targetIp}")
                scan_ports(targetIp)
            except socket.gaierror:
                print("\nCould not resolve hostname.")
        elif input_choice == "3":
            targetIp = input("\nEnter Target IP Address: ")
            try:
                startPort = int(input("Enter Start Port: "))
                endPort = int(input("Enter End Port: "))
                if 1 <= startPort <= 65535 and 1 <= endPort <= 65535 and startPort <= endPort:
                    scan_ports(targetIp, startPort, endPort)
                else:
                    print("\nInvalid port range.")
            except ValueError:
                print("\nPorts must be integers.")
        elif input_choice == "4":
            print("\nExiting...")
            time.sleep(1)
            break
        else:
            print("\nInvalid choice. Try again.")
            time.sleep(1)

        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    menu()