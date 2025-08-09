# security_multitool
# 🔐 Security Multitool CLI

**Security Multitool CLI** is a lightweight, command-line toolkit that consolidates multiple cybersecurity and reconnaissance utilities into a single package.  
Ideal for ethical hackers, penetration testers, sysadmins, and network engineers, it offers a fast and intuitive menu-driven interface for essential security checks.

---

## 🚀 Features
- **Port Scanner** – Scan a host for open ports.
- **Whois Lookup** – Retrieve domain registration information.
- **HTTP Header Analyzer** – View server HTTP headers for security insights.
- **DNS Lookup** – Fetch DNS records for a given domain.
- **IP Geolocation** – Identify the location and ISP of an IP address.

---

## 📦 Installation

Clone the repository and install the package:
```bash
git clone https://github.com/callmejay17/security-multitool.git
cd security-multitool
pip install .
```

You can also install it in editable mode for development:
```bash
pip install -e .
```

---

## 📌 Usage

Run the multitool from your terminal:
```bash
security-multitool
```
Select a tool from the menu and follow the prompts.

Example:
```
1. Port Scanner
2. Whois Lookup
3. HTTP Header Analyzer
4. DNS Lookup
5. IP Geolocation
Enter your choice: 1
Target IP/Domain: example.com
```

---

## 🛠 Requirements
- Python 3.7+
- Internet connection (for certain features like Whois, Geolocation)

---

## ⚠️ Disclaimer
This tool is intended for **educational and authorized security testing purposes only**.  
The author is not responsible for any misuse of this software.

---

**Tagline:** *Your pocket-sized cybersecurity toolkit, right in the terminal.*
