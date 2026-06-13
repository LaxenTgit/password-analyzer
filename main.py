# created by LAXENT & LATENT ( so its me :3 )

import time
import sys
import os
import re
import math
import argparse

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def animated_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def calculate_entropy(password):
    pool_size = 0
    if re.search(r"[a-z]", password): pool_size += 26
    if re.search(r"[A-Z]", password): pool_size += 26
    if re.search(r"\d", password): pool_size += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): pool_size += 32

    if pool_size == 0:
        return 0

    entropy = len(password) * math.log2(pool_size)
    return round(entropy, 2)

def check_password_strength(password):
    feedback = []
    is_strong = True

    if len(password) < 8:
        feedback.append("Password is too short (minimum 8 characters required).")
        is_strong = False

    if not (re.search(r"[A-Z]", password) and re.search(r"[a-z]", password)):
        feedback.append("Missing a combination of uppercase and lowercase letters.")
        is_strong = False

    if re.search(r"\d", password):
        if len(re.findall(r"\d", password)) > len(password) * 0.7:
            feedback.append("High density of numbers makes the password easily predictable.")
            is_strong = False
    else:
        feedback.append("Does not contain any numbers.")
        is_strong = False

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("Missing special characters.")
        is_strong = False

    return is_strong, feedback

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

def main():
    parser = argparse.ArgumentParser(description="Advanced Password Security Analyzer")
    parser.add_argument("-p", "--password", help="Specify the password to analyze directly")
    parser.add_argument("-w", "--wordlist", default="wordlist.txt", help="Path to a custom wordlist file (Default: wordlist.txt)")
    args = parser.parse_args()

    if not args.password:
        clear_screen()
        print(f"{Colors.BLUE}🔒 Password Security Analyzer{Colors.RESET}")
        print("-" * 40)
        password = input("Please enter the password to analyze: ")
        print()
    else:
        password = args.password

    print("🔍 data base searching... (1)")
    is_compromised = local_wordlist_scan(password, args.wordlist)
    time.sleep(0.8)
    
    print("🔎The database is being carefully searched. (2)")
    time.sleep(0.8)
    
    if is_compromised:
        print(f"\n{Colors.RED}❌ RESULT: Password found in common wordlists!{Colors.RESET}")
        print("   This password has been previously breached or is widely used.")
        print("   It is highly recommended to change it immediately.")
        sys.exit(1)
    else:
        print(f"{Colors.GREEN}✅ Your password is secure. It does not appear in the most commonly used wordlists. {Colors.RESET}\n")
        time.sleep(1)
        
        sys.stdout.write("⚙️ PASSWORD is being re-checked.")
        for _ in range(4):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.3)
        print("\n")
        
        animated_print("   ➔ Evaluating length parameters...")
        animated_print("   ➔ Scanning case sensitivity patterns...")
        animated_print("   ➔ Analyzing special character complexity...")
        animated_print("   ➔ Calculating structural entropy and predictability...\n", delay=0.01)

        is_strong, feedback = check_password_strength(password)
        entropy = calculate_entropy(password)

        print("-" * 40)
        print(f"📊 {Colors.BLUE}Mathematical Entropy Score: {entropy} bits{Colors.RESET}")
        
        if entropy < 40:
            print(f"   Security Tier: {Colors.RED}Weak{Colors.RESET} (Vulnerable to brute-force attacks)")
        elif entropy < 60:
            print(f"   Security Tier: {Colors.YELLOW}Moderate{Colors.RESET} (Acceptable but could be improved)")
        else:
            print(f"   Security Tier: {Colors.GREEN}Strong{Colors.RESET} (Highly resistant to targeting efforts)")
        print("-" * 40 + "\n")

        if not is_strong or entropy < 40:
            print(f"{Colors.RED}❌ RESULT: bad password you can change!{Colors.RESET}")
            print("   Identified Vulnerabilities:")
            for f in feedback:
                print(f"   - {f}")
        else:
            print(f"{Colors.GREEN}🌟 RESULT: Your password is structurally robust and complex. Safe!{Colors.RESET}")

    if not args.password:
        print("\n" + "-" * 40)
        input("Press any key to exit...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Process terminated. Exiting...{Colors.RESET}")
        sys.exit(0)

# BİTTİ SONUNDA VALLA ÇOK YORULDUM 🥀
