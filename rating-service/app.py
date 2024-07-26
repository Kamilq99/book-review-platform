from flask import Flask, request, jsonify

app = Flask(__name__)
ratings = {}

@app.route('/ratings', methods=['POST'])
def add_rating():
    data = request.get_json()
    book_id = data.get('book_id')
    rating = data.get('rating')
    if book_id not in ratings:
        ratings[book_id] = []
    ratings[book_id].append(rating)
    return jsonify({'message': 'Rating added successfully'}), 201

@app.route('/ratings/<int:book_id>', methods=['GET'])
def get_rating(book_id):
    rating_list = ratings.get(book_id, [])
    if not rating_list:
        return jsonify({'message': 'No ratings found'}), 404
    average_rating = sum(rating_list) / len(rating_list)
    return jsonify({'average_rating': average_rating}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)