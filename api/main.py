import json
from flask import Flask, abort, jsonify

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

if __name__ == '__main__':
    app.run(debug=True)
