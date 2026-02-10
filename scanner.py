import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def crawl_links(url):
    links = set()
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        for a in soup.find_all("a", href=True):
            link = urljoin(url, a["href"])
            if url in link:
                links.add(link)

    except:
        pass

    return list(links)


def check_headers(url):
    findings = []
    try:
        response = requests.get(url, timeout=5)

        headers = [
            "X-Frame-Options",
            "Content-Security-Policy",
            "X-XSS-Protection"
        ]

        for h in headers:
            if h not in response.headers:
                findings.append({
                    "type": "Missing Security Header",
                    "severity": "Medium",
                    "detail": f"{h} missing on {url}"
                })
    except:
        pass

    return findings


def directory_scan(url):
    findings = []
    wordlist = ["admin", "login", "backup", "dashboard"]

    for word in wordlist:
        try:
            test_url = f"{url.rstrip('/')}/{word}"
            r = requests.get(test_url, timeout=3)
            if r.status_code == 200:
                findings.append({
                    "type": "Directory Found",
                    "severity": "Low",
                    "detail": test_url
                })
        except:
            pass

    return findings


def run_scan(url):
    results = []

    urls_to_scan = [url]
    crawled = crawl_links(url)

    urls_to_scan.extend(crawled[:5])

    for target in urls_to_scan:
        results.extend(check_headers(target))
        results.extend(directory_scan(target))

    return results
