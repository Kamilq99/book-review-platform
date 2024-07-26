from flask import Flask, request, jsonify

app = Flask(__name__)
reviews = {}

@app.route('/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    review_id = len(reviews) + 1
    reviews[review_id] = data
    return jsonify({'message': 'Review added successfully', 'review_id': review_id}), 201

@app.route('/reviews/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = reviews.get(review_id)
    if not review:
        return jsonify({'message': 'Review not found'}), 404
    return jsonify(review), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)