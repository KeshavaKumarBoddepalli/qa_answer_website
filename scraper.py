import requests
from bs4 import BeautifulSoup
import re
from database import save_documentation

def fetch_website_content(url):
    """Fetch and clean text from help websites."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.extract()

        text = ' '.join(soup.stripped_strings)
        cleaned_text = re.sub(r'\s+', ' ', text)

        save_documentation(url, cleaned_text)
        return cleaned_text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
