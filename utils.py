import re
import os
import sys
from datetime import datetime

def print_banner(tool_name):
    """Prints a stylized ASCII banner for the toolkit."""
    banner = f"""
    ====================================
    PyPen Toolkit: {tool_name}
    Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    ====================================
    """
    print(banner)

def validate_ip(ip):
    """Validates if the input is a properly formatted IPv4 address."""
    # Simple Regex for IPv4 validation
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    if re.match(pattern, ip):
        return True
    return False

def log_result(module_name, message):
    """Logs findings to a text file for reporting."""
    with open("scan_results.txt", "a") as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"[{timestamp}] [{module_name}] {message}\n")

def clear_screen():
    """Clears the terminal screen based on the OS."""
    os.system('cls' if os.name == 'nt' else 'clear')