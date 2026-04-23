import requests

def run(target_url, wordlist):
    """Checks for hidden directories on a web server."""
    print(f"[*] Starting Directory Buster on {target_url}...")
    found_dirs = []
    
    for word in wordlist:
        word = word.strip()
        if not word: continue
        
        url = f"{target_url}/{word}"
        try:
            # Using a short timeout to keep the scan moving
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                print(f"[+] Found: {url} (Status: 200)")
                found_dirs.append(url)
        except Exception:
            pass
            
    print(f"[*] Search complete. Found {len(found_dirs)} directories.")
    return found_dirs