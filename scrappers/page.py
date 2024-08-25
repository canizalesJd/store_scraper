import requests
from bs4 import BeautifulSoup
from constants import *

# Fetches a page (BASE URL by default) and returns soup
def fetchPage(url=BASE_URL):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        return soup
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error fetching the page: {e}")
