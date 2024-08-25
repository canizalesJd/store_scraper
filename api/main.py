import json
from flask import Flask, abort, jsonify, request

app = Flask(__name__)

# Loading JSON data
with open('../data/books.json') as f:
    data = json.load(f)

# Get all Books
@app.route('/books')
def get_books():
    return jsonify(data)

# Get Books by category name (id)
@app.route('/books/<category>', methods=['GET'])
def get_books_by_category(category):
    category = category.lower().replace(" ", "_")
    print(category)
    if category in data:
        return jsonify(data[category])
    else:
        abort(404, description="Category not found")
    
@app.route('/search', methods=['GET'])
def search_books():
    query = request.args.get('q', '').lower()
    if not query:
        abort(400, description="Search query not provided")
    
    results = []
    for _, books in data.items():
        # Filter books by the search query in the title
        results.extend([book for book in books if query in book['title'].lower()])
    
    if results:
        return jsonify(results)
    else:
        abort(404, description="No books found matching the query")

if __name__ == '__main__':
    app.run(debug=True)
