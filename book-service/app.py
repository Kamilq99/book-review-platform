from flask import Flask, request, jsonify

app = Flask(__name__)
books = {}

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    book_id = len(books) + 1
    books[book_id] = data
    return jsonify({'message': 'Book added successfully', 'book_id': book_id}), 201

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = books.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    return jsonify(book), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)