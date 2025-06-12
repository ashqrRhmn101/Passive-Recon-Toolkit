import whois
import socket
import dns.resolver
import requests
from colorama import Fore, Style

def get_whois(domain):
    print(f"{Fore.GREEN}[+] WHOIS Information:{Style.RESET_ALL}")
    try:
        info = whois.whois(domain)
        for key, value in info.items():
            print(f"{Fore.YELLOW}{key}: {Style.RESET_ALL}{value}")
    except Exception as e:
        print(f"{Fore.RED}WHOIS error: {e}{Style.RESET_ALL}")

def get_dns(domain):
    print(f"\n{Fore.GREEN}[+] DNS Records:{Style.RESET_ALL}")
    record_types = ['A', 'NS', 'MX']
    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            print(f"{Fore.CYAN}{record} Records:{Style.RESET_ALL}")
            for rdata in answers:
                print(f" - {rdata.to_text()}")
        except Exception as e:
            print(f" - {record} record not found.")

def get_ip_info(domain):
    print(f"\n{Fore.GREEN}[+] IP & Host Info:{Style.RESET_ALL}")
    try:
        ip = socket.gethostbyname(domain)
        print(f"{Fore.YELLOW}IP Address:{Style.RESET_ALL} {ip}")
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        for key in ['city', 'region', 'country', 'org', 'loc']:
            print(f"{Fore.CYAN}{key.title()}: {Style.RESET_ALL}{data.get(key)}")
    except Exception as e:
        print(f"{Fore.RED}IP lookup failed: {e}{Style.RESET_ALL}")

def whatweb(domain):
    print(f"\n{Fore.GREEN}[+] Technology Fingerprinting:{Style.RESET_ALL}")
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(f"http://{domain}", headers=headers, timeout=5)
        server = resp.headers.get('Server', 'Unknown')
        print(f"{Fore.YELLOW}Server Header:{Style.RESET_ALL} {server}")
    except:
        print(f"{Fore.RED}Could not fingerprint the site.{Style.RESET_ALL}")

def main():
    print(f"{Fore.CYAN}🛰️ WHOIS Information v1 — Passive Recon Toolkit 🛰️\n=> Developed By HackA.R {Style.RESET_ALL}")
    domain = input(f"{Fore.BLUE}Enter a domain (e.g. HackAR.com): {Style.RESET_ALL}").strip()
    print("\n")
    get_whois(domain)
    get_dns(domain)
    get_ip_info(domain)
    whatweb(domain)

if __name__ == "__main__":
    main()
