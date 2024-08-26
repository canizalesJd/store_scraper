import os
import json
from flask import Flask, abort, jsonify, request

app = Flask(__name__)

# Loading JSON data
def get_data():
    file_path = '../data/books.json'
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    try:
        with open(file_path) as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON data.")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {str(e)}")

# Load data
try:
    data = get_data()
except (FileNotFoundError, ValueError, RuntimeError) as e:
    app.logger.error(str(e))
    data = {}

# Get all Books
@app.route('/books')
def get_books():
    return jsonify(data)

# Get Books by category name (id)
@app.route('/books/<category>', methods=['GET'])
def get_books_by_category(category):
    category = category.lower().replace(" ", "_")
    if category in data:
        return jsonify(data[category])
    else:
        abort(404, description="Category not found")

# Search books by title
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
