from .page import fetchPage
from constants import *

# Scraps the categories and returns a list of items with it's name and url
def getCategoryList():
    soup = fetchPage()
    categories = soup.find('div', class_='side_categories').find_all('a')
    category_list = []
    for index, category in enumerate(categories):
        category_name = category.get_text().strip()
        category_url = category.get('href')
        item = {
            "id": index,
            "name": category_name,
            "url": BASE_URL + category_url
        }
        category_list.append(item)
    return category_list