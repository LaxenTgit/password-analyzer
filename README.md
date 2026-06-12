# Password Security Analyzer

A lightweight Python tool that analyzes password strength using entropy scoring and detects commonly used passwords through a local wordlist database.

It is designed for educational and security awareness purposes.

---

## Features

* Wordlist-based compromised password detection
* Entropy-based strength evaluation
* Structural password analysis (length, patterns, character diversity)
* Cross-platform support (Windows, Linux, macOS)
* No external dependencies required
* Fully local execution (no password transmission)

---

## Project Structure

```text
password-analyzer/
│
├─ main.py
├─ core/
│   ├─ analyzer.py
│   ├─ entropy.py
│   ├─ scanner.py
│
├─ wordlists/
│   └─ wordlists.txt
│
├─ utils/
│   └─ colors.py
│
└─ README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/LaxenTgit/password-analyzer.git
cd password-analyzer
```

Make sure Python 3.8+ is installed.

No external libraries are required.

---

## Usage

### Interactive Mode

```bash
python main.py
```

The program will prompt you to enter a password.

---

### CLI Mode

```bash
python main.py -p "YourPassword123!"
```

---

## How It Works

### 1. Wordlist Scan

The password is checked against a local database of commonly used passwords.

If a match is found, the password is considered compromised.

---

### 2. Entropy Calculation

Password strength is measured using entropy:

* Lowercase letters
* Uppercase letters
* Numbers
* Special characters

Higher entropy = stronger password resistance against brute-force attacks.

---

### 3. Strength Analysis

The tool evaluates:

* Password length
* Character variety
* Numeric density
* Special character usage
* Predictable patterns

---

## Example Output

### Wordlist Match Found

```text
🔍 SCANNING DATABASE... (1)
🔎 SEARCHING DATABASE THOROUGHLY... (2)

❌ RESULT: Your password was FOUND in the most popular wordlist files!
   This password has been previously exposed or is too common.
   You should choose a different password immediately.
```

---

### Strong Password

```text
📊 Entropy: 62.4 bits
Level: Strong

🌟 RESULT: Your password looks strong and structurally complex. You are safe.
```

---

## Notes

* All processing is done locally
* No passwords are stored or sent externally
* Wordlist file can be customized for stronger testing
* Designed for educational cybersecurity learning

---

## Security Disclaimer

This tool is for educational and awareness purposes only.
It does not guarantee real-world cryptographic security.

---

## License

MIT License
