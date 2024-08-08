from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Hello, World!'

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(message='This is your API data!')

@app.route('/api/data', methods=['POST'])
def post_data():
    if request.is_json:
        data = request.get_json()
        return jsonify(received=data)
    else:
        return jsonify(error='Request must be JSON'), 400

if __name__ == '__main__':
    app.run(debug=True)
