from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    response = requests.post('http://user-service:5000/register', json={'username': username, 'password': password})
    if response.status_code == 201:
        return redirect(url_for('index'))
    else:
        return "Registration failed", response.status_code

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    response = requests.post('http://user-service:5000/login', json={'username': username, 'password': password})
    if response.status_code == 200:
        return redirect(url_for('index'))
    else:
        return "Login failed", response.status_code

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    response = requests.post('http://book-service:5001/books', json={'title': title, 'author': author})
    if response.status_code == 201:
        return redirect(url_for('index'))
    else:
        return "Adding book failed", response.status_code

@app.route('/add_review', methods=['POST'])
def add_review():
    book_id = request.form['book_id']
    review = request.form['review']
    response = requests.post('http://review-service:5002/reviews', json={'book_id': book_id, 'review': review})
    if response.status_code == 201:
        return redirect(url_for('index'))
    else:
        return "Adding review failed", response.status_code

@app.route('/add_rating', methods=['POST'])
def add_rating():
    book_id = request.form['book_id']
    rating = request.form['rating']
    response = requests.post('http://rating-service:5003/ratings', json={'book_id': book_id, 'rating': rating})
    if response.status_code == 201:
        return redirect(url_for('index'))
    else:
        return "Adding rating failed", response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
