from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def notify():
    data = request.get_json()
    # Here you would integrate with an email service to send the notification
    return jsonify({'message': 'Notification sent successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)