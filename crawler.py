import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

visited = set()

def crawl_site(urls, max_pages=30):
    pages = []

    def crawl(url):
        if url in visited or len(visited) >= max_pages:
            return

        visited.add(url)

        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                return

            soup = BeautifulSoup(response.text, "lxml")
            pages.append({
                "url": url,
                "content": soup
            })

            for link in soup.find_all("a", href=True):
                next_url = urljoin(url, link["href"])
                if urlparse(next_url).netloc == urlparse(url).netloc:
                    crawl(next_url)

        except Exception:
            return

    for u in urls:
        crawl(u)

    return pages
