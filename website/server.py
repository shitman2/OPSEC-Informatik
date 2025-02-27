from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/receive_message', methods=['POST'])
def receive_message():
    data = request.json
    print("data from js: ", data)
    return jsonify({'status':'we have recieved msg successfully'})

if __name__ == '__main__':
    app.run(host="localhost", port=8000)