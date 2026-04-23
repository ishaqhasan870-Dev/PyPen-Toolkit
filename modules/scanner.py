import socket
from concurrent.futures import ThreadPoolExecutor

def check_port(target, port):
    """Worker function to check a single port."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0) # Slightly longer timeout for reliability
    
    try:
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
            return port
    except Exception:
        pass
    finally:
        s.close()
    return None

def run(target, ports, thread_count=100):
    """Scans ports using a thread pool."""
    print(f"[*] Starting Multithreaded Scan on {target} using {thread_count} threads...")
    open_ports = []

    # ThreadPoolExecutor manages the threads for us
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        # Submit all port checks to the executor
        results = executor.map(lambda p: check_port(target, p), ports)
        
        # Collect results as they finish
        for port in results:
            if port:
                open_ports.append(port)

    print(f"[*] Scan complete. Found {len(open_ports)} open ports.")
    return open_ports