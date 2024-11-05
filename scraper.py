import requests
from bs4 import BeautifulSoup

def scrape(url, output_type="Headers"):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to load the page")

    soup = BeautifulSoup(response.content, "html.parser")
    data = []

    if output_type == "Headers":
        for header in soup.find_all(['h1', 'h2', 'h3']):
            data.append(header.get_text())
    elif output_type == "Links":
        for link in soup.find_all('a', href=True):
            data.append(link['href'])

    return data
