from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from database import init_db, add_user

app = Flask(__name__, static_url_path='', static_folder='../frontend')
CORS(app)

# Initialize the database when the app starts
init_db()

@app.route('/')
def serve_index():
    return send_from_directory('../frontend', 'index.html')

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    user_id = add_user(name, age)
    return jsonify({'id': user_id, 'name': name, 'age': age}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
