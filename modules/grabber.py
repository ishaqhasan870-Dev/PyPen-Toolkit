import socket

def run(target, port):
    """Attempts to grab the service banner from an open port."""
    print(f"[*] Attempting to grab banner from {target}:{port}...")
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((target, port))
        
        # Send a basic probe to encourage a response
        s.send(b'Hello\r\n') 
        banner = s.recv(1024).decode(errors='ignore').strip()
        
        if banner:
            print(f"[+] Service Banner: {banner}")
            return banner
        else:
            print("[-] No banner returned (service may be silent).")
    except Exception as e:
        print(f"[!] Connection failed: {e}")
    finally:
        s.close()
    return None