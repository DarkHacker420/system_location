import socket
from rich.console import Console
import requests

# requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'


############################################
# Welcome message
############################################

def welcome_message():
    console = Console()
    python_logo = """
     _______    ______   _______   __    __        ______   __    __   ______   _______    ______   __       __ 
    |       \  /      \ |       \ |  \  /  \      /      \ |  \  |  \ /      \ |       \  /      \ |  \  _  |  \\
    | $$$$$$$\|  $$$$$$\| $$$$$$$\| $$ /  $$     |  $$$$$$\| $$  | $$|  $$$$$$\| $$$$$$$\|  $$$$$$\| $$ / \ | $$
    | $$  | $$| $$__| $$| $$__| $$| $$/  $$______| $$___\$$| $$__| $$| $$__| $$| $$  | $$| $$  | $$| $$/  $\| $$
    | $$  | $$| $$    $$| $$    $$| $$  $$|      \\$$    \ | $$    $$| $$    $$| $$  | $$| $$  | $$| $$  $$$\ $$
    | $$  | $$| $$$$$$$$| $$$$$$$\| $$$$$\ \$$$$$$_\$$$$$$\| $$$$$$$$| $$$$$$$$| $$  | $$| $$  | $$| $$ $$\$$\$$
    | $$__/ $$| $$  | $$| $$  | $$| $$ \$$\      |  \__| $$| $$  | $$| $$  | $$| $$__/ $$| $$__/ $$| $$$$  \$$$$
    | $$    $$| $$  | $$| $$  | $$| $$  \$$\      \$$    $$| $$  | $$| $$  | $$| $$    $$ \$$    $$| $$$    \$$$
     \$$$$$$$  \$$   \$$ \$$   \$$ \$$   \$$       \$$$$$$  \$$   \$$ \$$   \$$ \$$$$$$$   \$$$$$$  \$$      \$$
    """
    console.print(f"[bold magenta]{python_logo}[/bold magenta]")
    console.print("[cyan][bold]Welcome to the IP Information and Port Checker Tool![/bold][/cyan]\n")
    console.print("[cyan][bold]DARK SHADOW![/bold][/cyan]\n")
    console.print("[cyan][bold]telegram username: @darkshadow302[/bold][/cyan]\n")


welcome_message()

# Replace 'YOUR_ACCESS_TOKEN' with your actual access token from ipinfo.io
ACCESS_TOKEN = '5dd55632ede162'


def get_ip_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json?token={ACCESS_TOKEN}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)

        data = response.json()
        return data
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")

    return None


def get_ip_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json?token={ACCESS_TOKEN}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)

        data = response.json()
        return data
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")

    return None


def check_open_ports(ip_address):
    try:
        # Set the range of ports you want to check
        port_range = range(1, 1025)
        open_ports = []

        for port in port_range:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Adjust the timeout as needed
            result = sock.connect_ex((ip_address, port))

            if result == 0:
                open_ports.append(port)

            sock.close()

        return open_ports
    except socket.error as e:
        print(f"Error checking open ports: {e}")
        return None


def main():
    print("Welcome to the IP Information and Port Checker Tool.")

    option = input(
        "\nChoose an option:\n1. Find IP information for your own system\n2. Enter an IP address to find details and check open ports\nOption (1 or 2): ")

    if option == '1':
        # Fetch information about the system's IP address
        ip_info = get_ip_info('')
        print("\nYour System's IP Information:")
    elif option == '2':
        ip_address = input("Enter the IP address you want to track: ")
        ip_info = get_ip_info(ip_address)
        print(f"\nInformation for IP Address {ip_address}:")

        # Check for open ports
        open_ports = check_open_ports(ip_address)
        if open_ports:
            print(f"\nOpen Ports: {', '.join(map(str, open_ports))}")
        else:
            print("\nError checking open ports.")
            return
    else:
        print("Invalid option. Please choose either 1 or 2.")
        return

    if ip_info:
        print(f"IP Address: {ip_info.get('ip', 'N/A')}")
        print(
            f"Location: {ip_info.get('city', 'N/A')}, {ip_info.get('region', 'N/A')}, {ip_info.get('country', 'N/A')}")
        print(f"Latitude/Longitude: {ip_info.get('loc', 'N/A')}")
        print(f"ISP: {ip_info.get('org', 'N/A')}")
        print(f"AS: {ip_info.get('asn', 'N/A')}")
        print(f"Timezone: {ip_info.get('timezone', 'N/A')}")
        print(f"ZIP Code: {ip_info.get('postal', 'N/A')}")


if __name__ == "__main__":
    main()
