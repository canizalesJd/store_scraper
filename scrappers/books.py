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
    update_books(books)
    save_data_to_json(books, "books", "data")
    return books

# add more details to each book
def update_books(books):
    for category in books:
        for book in books[category]:
            details = get_book_details(book['book_url'])
            book.update(details)
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
            price = book.find('p', class_='price_color').get_text().replace('', '£')
            availability = book.find('p', class_='instock availability').get_text(strip=True)
            book_id = title.strip().lower().replace(' ', '_')
            book_url = f"{BASE_URL}catalogue/{book.h3.a['href'].replace('../', '')}"
            books.append({
                "id": book_id,
                "title": title,
                "availability": availability,
                "price": price,
                "book_url": book_url,
            })
        
        # Handle pagination (if any)
        next_button = soup.find('li', class_='next')
        if next_button:
            next_url = next_button.find('a')['href']
            url = category['url'] + next_url
        else:
            url = None
    return books

# get each book details
def get_book_details(book_url):
    soup = fetch_page(book_url) 
    description = soup.find('meta', {'name': 'description'})['content'].strip()
    upc = soup.find('table', {'class': 'table table-striped'}).find_all('tr')[0].find('td').text
    image_url = soup.find('div', {'id': 'product_gallery'}).find('img')['src']
    image_url = BASE_URL + image_url.lstrip('/')
    
    return {
        'description': description,
        'upc': upc,
        'image_url': image_url
    }
