# passcheck.py by LAXENT ( so its me )
# wordlist + entropy based password analysis
# TODO: add hibp api someday

import sys
import os
import re
import math
import argparse
import time

R = '\033[0m'
G = '\033[92m'
RD = '\033[91m'
Y = '\033[93m'
B = '\033[94m'

def entropy(pw):
    pool = 0
    if re.search(r"[a-z]", pw): pool += 26
    if re.search(r"[A-Z]", pw): pool += 26
    if re.search(r"\d", pw):    pool += 10
    if re.search(r"[!@#$%^&*()\-_=+\[\]{};:'\",.<>?/\\|`~]", pw): pool += 33
    if pool == 0:
        return 0
    return round(len(pw) * math.log2(pool), 2)

def scan(pw, wl):
    if not os.path.exists(wl):
        print(f"{Y}[!] wordlist not found: {wl}{R}")
        return False
    with open(wl, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if pw == line.strip():
                return True
    return False

def check(pw):
    problems = []
    if len(pw) < 8:
        problems.append("too short (min 8)")
    if not re.search(r"[A-Z]", pw):
        problems.append("no uppercase")
    if not re.search(r"[a-z]", pw):
        problems.append("no lowercase")
    if not re.search(r"\d", pw):
        problems.append("no digits")
    if not re.search(r"[!@#$%^&*()\-_=+]", pw):
        problems.append("no special chars")
    # too many digits is suspicious — 0.7 because it usually means pin-like stuff
    digits = re.findall(r"\d", pw)
    if len(digits) > len(pw) * 0.7:
        problems.append("too many digits, easily guessable")
    return problems

def main():
    parser = argparse.ArgumentParser(prog="passcheck")
    parser.add_argument("-p", "--password")
    parser.add_argument("-w", "--wordlist", default="wordlist.txt")
    args = parser.parse_args()

    pw = args.password
    if not pw:
        pw = input("password: ")

    print(f"\n{B}[*]{R} scanning wordlist...")
    found = scan(pw, args.wordlist)
    
    if found:
        print(f"{RD}[!] password found in wordlist, don't use it{R}")
        sys.exit(1)

    print(f"{G}[+]{R} not in wordlist\n")

    e = entropy(pw)
    problems = check(pw)

    print(f"entropy: {B}{e} bits{R}")
    if e < 40:
        print(f"  tier: {RD}weak{R}")
    elif e < 60:
        print(f"  tier: {Y}medium{R}")
    else:
        print(f"  tier: {G}strong{R}")

    print()

    if problems:
        print(f"{RD}[!] issues:{R}")
        for p in problems:
            print(f"  - {p}")
        print(f"\n{RD}result: bad password{R}")
    else:
        print(f"{G}result: looks good{R}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Y}exiting{R}")
        sys.exit(0)
