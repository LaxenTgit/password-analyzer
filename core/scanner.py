import os
import time
from utils.colors import Colors

def local_wordlist_scan(password, wordlist_file):
    if not os.path.exists(wordlist_file):
        print(f"\n{Colors.YELLOW}⚠️ Warning: '{wordlist_file}' not found. Skipping database lookup...{Colors.RESET}")
        time.sleep(1.5)
        return False
    
    try:
        with open(wordlist_file, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                if password == line.strip():
                    return True
    except Exception as e:
        print(f"{Colors.RED}Error reading file: {e}{Colors.RESET}")
        return False
    return False
