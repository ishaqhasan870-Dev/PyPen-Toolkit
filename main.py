import sys
import utils
from modules import port_scanner, ssh_bruter, banner_grabber, dir_buster

def main():
    while True:
        utils.clear_screen()
        utils.print_banner("Main Menu")
        
        print("1. Multithreaded Port Scanner")
        print("2. SSH Brute Forcer")
        print("3. Service Banner Grabber")
        print("4. Web Directory Buster")
        print("5. Exit")
        
        choice = input("\nSelect an option: ")
        
        if choice == '1':
            target = input("[?] Target IP: ")
            if utils.validate_ip(target):
                port_scanner(target, range(1, 1025), thread_count=100)
            input("\nPress Enter to return...")

        elif choice == '2':
            target = input("[?] Target IP: ")
            user = input("[?] Username: ")
            wordlist = input("[?] Path to wordlist: ")
            try:
                with open(wordlist, 'r') as f:
                    ssh_bruter(target, user, f.readlines())
            except FileNotFoundError: 
                print("[!] File not found.")
            input("\nPress Enter to return...")

        elif choice == '3':
            target = input("[?] Target IP: ")
            port = int(input("[?] Port: "))
            banner_grabber(target, port)
            input("\nPress Enter to return...")

        elif choice == '4':
            target_url = input("[?] Target URL (e.g., http://127.0.0.1:8080): ")
            wordlist_path = input("[?] Path to directory wordlist: ")
            try:
                with open(wordlist_path, 'r') as f:
                    dir_buster(target_url, f.readlines())
            except FileNotFoundError: 
                print("[!] File not found.")
            input("\nPress Enter to return...")

        elif choice == '5':
            print("Exiting...")
            sys.exit()
            
        else:
            print("[!] Invalid selection.")
            input("\nPress Enter to try again...")

# --- CRITICAL: THE TRIGGER BLOCK ---
if __name__ == "__main__":
    main()