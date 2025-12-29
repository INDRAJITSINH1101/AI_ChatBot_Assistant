import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def crawl(start_url, max_pages=20):
    visited = set()
    pages = []
    domain = urlparse(start_url).netloc

    def _crawl(url):
        if url in visited or len(pages) >= max_pages:
            return

        visited.add(url)

        try:
            r = requests.get(url, timeout=10)
            soup = BeautifulSoup(r.text, "html.parser")

            # Remove unwanted tags
            for tag in soup(["script", "style", "nav", "footer", "header"]):
                tag.decompose()

            text = soup.get_text(separator=" ")
            pages.append(text)

            for link in soup.find_all("a"):
                href = link.get("href")
                if not href:
                    continue

                full_url = urljoin(url, href)

                if urlparse(full_url).netloc == domain:
                    _crawl(full_url)

        except Exception as e:
            print("Crawl error:", e)

    _crawl(start_url)
    return pages
