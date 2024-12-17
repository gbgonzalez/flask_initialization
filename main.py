from flask import Flask, request
from controllers import get_all_users, add_single_user

app = Flask(__name__)

@app.route('/get_users', methods=['GET'])
def get_users():
    return get_all_users()

@app.route('/add_users', methods=['POST'])
def add_user():
    data = request.get_json()
    return add_single_user(data)

if __name__ == '__main__':
    app.run(debug=True)