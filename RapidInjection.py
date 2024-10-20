import random
import time

bssid = None
protocol = None
cert_path = None
server_ip = None
server_port = None
payload = None
target_vulnerable = False
target_isp = None
target_ip = None

GREEN = "\033[92m"
RESET = "\033[0m"

def generate_random_bssid():
    return ':'.join(f'{random.randint(0, 255):02X}' for _ in range(6))

def clear_configuration():
    global bssid, protocol, cert_path, server_ip, server_port, payload, target_vulnerable, target_isp, target_ip
    bssid = None
    protocol = None
    cert_path = None
    server_ip = None
    server_port = None
    payload = None
    target_vulnerable = False
    target_isp = None
    target_ip = None

def configure_attack():
    global bssid, protocol, cert_path, server_ip, server_port, payload, target_vulnerable, target_isp, target_ip

    print("Scanning for nearby devices...")
    time.sleep(2)

    bssid_options = [generate_random_bssid() for _ in range(3)]
    
    print(f"Found the following BSSIDs: ")
    for i, option in enumerate(bssid_options, start=1):
        print(f"{i}) {option}")

    bssid_choice = input("Select the target BSSID: ")
    if bssid_choice in ["1", "2", "3"]:
        bssid = bssid_options[int(bssid_choice) - 1]
    else:
        print("Invalid selection. Try again.")
        configure_attack()

    protocol = input("Select protocol (HTTP/HTTPS): ").upper()

    if protocol == "HTTPS":
        cert_path = input("Enter certificate file path: ")

    server_ip = input("Enter server IP/hostname: ")
    server_port = input("Enter server port: ")

    print("Select payload option...")
    time.sleep(2)
    payload_options = ["FirmwareUpdate_v1.bin", "FakeUpdate_v2.bin", "RapidFirmwarePatch_v3.bin"]
    for i, payload_option in enumerate(payload_options, start=1):
        print(f"{i}) {payload_option}")

    payload_choice = input("Select the payload: ")
    if payload_choice in ["1", "2", "3"]:
        payload = payload_options[int(payload_choice) - 1]
    else:
        print("Invalid payload choice.")
        configure_attack()

    print("Checking target for vulnerabilities...")
    time.sleep(2)

    vulnerability_check = random.randint(0, 5)
    if vulnerability_check < 4:
        print(f"{GREEN}Target is vulnerable!{RESET}")
        target_vulnerable = True

        isps = ["AT&T", "Verizon", "Comcast", "Charter", "Spectrum", "T-Mobile"]
        target_isp = random.choice(isps)
        target_ip = f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}"

        print(f"ISP: {target_isp}")
        print(f"Target IP: {target_ip}")
        print(f"BSSID: {bssid}")
        print(f"Protocol: {protocol}")
        if protocol == "HTTPS":
            print(f"Certificate: {cert_path}")
        print(f"Server IP: {server_ip}")
        print(f"Server Port: {server_port}")
        print(f"Payload: {payload}")

        confirm = input("Confirm attack? (y/n): ").lower()
        if confirm == 'y':
            print(f"{GREEN}Confirmed! Proceeding to attack...{RESET}")
            time.sleep(2)
            launch_attack()  # Automatically start the attack after confirmation
        else:
            clear_configuration()
            show_menu()
    else:
        print("Target is not vulnerable.")
        clear_configuration()
        show_menu()

def launch_attack():
    global bssid, protocol, cert_path, server_ip, server_port, payload, target_vulnerable, target_isp, target_ip

    if not bssid or not server_ip or not server_port or not payload or not target_vulnerable:
        print("Attack not configured. Please configure the attack first.")
        time.sleep(2)
        show_menu()
    else:
        print(f"{GREEN}Attack starting on BSSID: {bssid}{RESET}")
        time.sleep(1)
        print(f"{GREEN}Sending payload: {payload}{RESET}")
        time.sleep(1)
        print(f"{GREEN}Connecting to C2 server {server_ip} on port {server_port}...{RESET}")
        
        # Fake packet transaction simulation
        print("Uploading firmware... ", end="")
        for _ in range(30):
            time.sleep(0.1)
            print("=", end="", flush=True)
        print(f" {GREEN}100%{RESET}")
        time.sleep(1)

        print("Active packet communication... ", end="")
        for _ in range(40):
            time.sleep(0.1)
            print("=", end="", flush=True)
        print(f" {GREEN}100%{RESET}")
        time.sleep(1)
        print(f"{GREEN}Attack Completed Successfully!{RESET}")
        print("Device exploited, added to C2 server!")
        print(f"Details:")
        print(f"BSSID: {bssid}")
        print(f"Target IP: {target_ip}")
        print(f"ISP: {target_isp}")
        print(f"Server IP: {server_ip}")
        print(f"Server Port: {server_port}")
        print(f"Payload: {payload}")
        time.sleep(2)
        input(f"\n{GREEN}Press Enter to return to the main menu...{RESET}")
        show_menu()

def show_menu():
    print("\n=== RapidInjection Menu ===")
    print("1. Configure Attack")
    print("2. Launch Attack")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        configure_attack()
    elif choice == "2":
        launch_attack()
    elif choice == "3":
        print("Exiting...")
        exit(0)
    else:
        print("Invalid option. Please try again.")
        show_menu()

if __name__ == "__main__":
    show_menu()
