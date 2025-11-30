import argparse
import json
import re
import socket
import requests
import dns.resolver
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

CONFIG_FILE = "config.json"

def load_config():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def print_banner():
    print(Fore.CYAN + r"""
    =====================================================
     _  ___   _ _   _ _        _    ___ _____ 
    | |/ / | | | | | | |      / \  |_ _|  ___|
    | ' /| |_| | |_| | |     / _ \  | || |_   
    | . \|  _  |  _  | |___ / ___ \ | ||  _|  
    |_|\_\_| |_|_| |_|_____/_/   \_\___|_|    
                                                  
         _____  ___   ___  _     
        |_   _|/ _ \ / _ \| |    
          | | | | | | | | | |    
          | | | |_| | |_| | |___ 
          |_|  \___/ \___/|_____|
    =====================================================
          KHULAIF TOOL - Advanced Email OSINT
    =====================================================
    """)

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

def get_dns_info(domain):
    print(Fore.YELLOW + f"[*] Getting DNS Records for {domain}...")
    try:
        # MX Records
        mx_records = dns.resolver.resolve(domain, 'MX')
        print(Fore.GREEN + "[+] MX Records:")
        for mx in mx_records:
            print(f"    - {mx.exchange} (Priority: {mx.preference})")
    except Exception as e:
        print(Fore.RED + f"[-] Could not get MX records: {e}")

    try:
        # A Records
        a_records = dns.resolver.resolve(domain, 'A')
        print(Fore.GREEN + "[+] A Records (IPs):")
        for a in a_records:
            print(f"    - {a.address}")
    except Exception as e:
        print(Fore.RED + f"[-] Could not get A records: {e}")

    try:
        # TXT Records
        txt_records = dns.resolver.resolve(domain, 'TXT')
        print(Fore.GREEN + "[+] TXT Records:")
        for txt in txt_records:
            print(f"    - {txt.to_text()}")
    except Exception as e:
        print(Fore.RED + f"[-] Could not get TXT records: {e}")

def check_hibp(email, api_key):
    if not api_key:
        print(Fore.YELLOW + "[!] Skipping HIBP check (No API Key found in config.json)")
        return

    print(Fore.YELLOW + f"[*] Checking HaveIBeenPwned for {email}...")
    headers = {
        'hibp-api-key': api_key,
        'user-agent': 'KHULAIF-TOOL'
    }
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=false"
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            breaches = response.json()
            print(Fore.RED + f"[!] Found {len(breaches)} breaches:")
            for breach in breaches:
                print(f"    - {breach['Name']} ({breach['BreachDate']})")
        elif response.status_code == 404:
            print(Fore.GREEN + "[+] No breaches found.")
        else:
            print(Fore.RED + f"[-] HIBP API Error: {response.status_code}")
    except Exception as e:
        print(Fore.RED + f"[-] Error connecting to HIBP: {e}")

def check_social_media(username):
    print(Fore.YELLOW + f"[*] Checking potential social media accounts for username '{username}'...")
    # Basic check - just checking if profile page returns 200. 
    # Note: This is prone to false positives/negatives depending on the site's behavior.
    sites = {
        "GitHub": f"https://github.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "Twitter": f"https://twitter.com/{username}"
    }

    for site, url in sites.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Found potential {site} profile: {url}")
            else:
                print(Fore.LIGHTBLACK_EX + f"[-] {site}: Not found (Status {response.status_code})")
        except Exception:
            print(Fore.RED + f"[-] Error checking {site}")

def google_dorks(email):
    print(Fore.YELLOW + "[*] Generating Google Dorks...")
    dorks = [
        f'site:pastebin.com "{email}"',
        f'site:linkedin.com "{email}"',
        f'intext:"{email}"',
        f'filetype:pdf "{email}"',
        f'filetype:txt "{email}"'
    ]
    for dork in dorks:
        print(f"    - https://www.google.com/search?q={requests.utils.quote(dork)}")

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="KHULAIF TOOL: Advanced Email OSINT Tool")
    parser.add_argument("-e", "--email", help="Target email address", required=True)
    args = parser.parse_args()

    email = args.email
    if not validate_email(email):
        print(Fore.RED + "[-] Invalid email format.")
        return

    username, domain = email.split('@')
    config = load_config()

    print(Fore.CYAN + f"Target: {email}")
    print(Fore.CYAN + "=" * 30)

    get_dns_info(domain)
    check_hibp(email, config.get("hibp_api_key"))
    check_social_media(username)
    google_dorks(email)

if __name__ == "__main__":
    main()
