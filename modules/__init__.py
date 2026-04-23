"""
PyPen Modules Package
Initializes the directory as a Python package and 
aliases module functions for consistent access in main.py.
"""

# Import the 'run' function from each module and rename for the CLI
from .scanner import run as port_scanner
from .bruteforcer import run as ssh_bruter
from .grabber import run as banner_grabber
from .dirbuster import run as dir_buster

# Define the public interface for the modules package
__all__ = [
    'port_scanner', 
    'ssh_bruter', 
    'banner_grabber', 
    'dir_buster'
]