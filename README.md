# Web Security Scanner 🔍

A modern web-based vulnerability scanner built with **Python, Flask, and Bootstrap**.  
This tool performs basic security checks on web applications and displays results in a modern dashboard.

---

## Features

- URL crawling to discover multiple pages
- Security header analysis
- Directory discovery
- Vulnerability severity classification (High / Medium / Low)
- Interactive dashboard UI
- Scan history tracking
- CSV report export
- Real-time scanning interface

---

## Tech Stack

- Python
- Flask
- Requests
- BeautifulSoup
- Pandas
- Bootstrap (UI)

---

## Project Structure

```
web-security-scanner/
│
├── app.py
├── scanner.py
├── wordlist.txt
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/viikas-singhh/Web-Security-Scanner.git
cd Web-Security-Scanner
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python3 app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## Usage

1. Enter a target URL.
2. Click **Start Scan**.
3. View vulnerabilities in the dashboard.
4. Export results as CSV if needed.

---

## Disclaimer

This tool is intended **for educational purposes only**.  
Only scan systems you own or have permission to test.

---

## Author

Vikas Singh  
Cybersecurity Student | SOC Analyst | Pentesting Enthusiast
