from .utils import *
from .categories import get_category_list
from constants import *

category_list =  get_category_list()

# get all books from all categories
def get_all_books():
    books = {}
    for category in category_list:
        books[category["id"]] = scrape_books_by_category(category)
    # save data on a json file for furhter processing
    save_data_to_json(books, "books", "data")
    return books

# get each book from the category
def scrape_books_by_category(category):
    books = []
    url = category['url']
    while url:
        soup = fetch_page(url)
        book_list = soup.find_all('article', class_='product_pod')
        for book in book_list:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').get_text()
            availability = book.find('p', class_='instock availability').get_text(strip=True)
            image_url = BASE_URL + book.find('img')['src'].replace('../', '')
            book_id = title.strip().lower().replace(" ", "_")

            books.append({
                "id": book_id,
                "title": title,
                "price": price,
                "availability": availability,
                "image_url": image_url,
            })
        
        # Handle pagination (if any)
        next_button = soup.find('li', class_='next')
        if next_button:
            next_url = next_button.find('a')['href']
            url = category['url'] + next_url
        else:
            url = None
    
    return books
