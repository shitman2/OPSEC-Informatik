import json
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/test', methods=['POST'])
def test():
    data = request.get_json()

    print("Raw Request Data:", request.data)  # Print raw request body
    print("Parsed JSON Data:", data)  # Print what Flask parses

    if not data:
        return {"error": "No JSON data received"}, 400

    image_data = data.get("image")

    if not image_data:
        return {"error": "Image data is missing"}, 400

    print("Received Image Data:", image_data[:100])  # Print first 100 chars of image data
    return {"message": "Image received successfully"}, 200


if __name__ == '__main__':
    app.run(debug=True)