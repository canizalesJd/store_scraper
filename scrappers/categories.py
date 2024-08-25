from .utils import *
from constants import *

# Scraps the categories and returns a list of items with it's name and url
def getCategoryList():
    soup = fetch_page()
    categories = soup.find('div', class_='side_categories').find_all('a')
    category_list = []
    for category in categories:
        category_name = category.get_text().strip()
        category_id = category_name.strip().lower().replace(" ", "_")
        # Skip the root "Books" category
        if category_name == "Books":
            continue

        category_url = category.get('href')
        category_list.append({
            "id": category_id,
            "name": category_name,
            "url": BASE_URL + category_url
        })
    return category_list
