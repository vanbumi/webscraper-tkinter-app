import requests
from bs4 import BeautifulSoup

def scrape(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to load the page")

    soup = BeautifulSoup(response.content, "html.parser")
    headers = []

    for header in soup.find_all(['h1', 'h2', 'h3']):
        headers.append(header.get_text())

    return headers
