from models import User
from DB.connect import database_connect
from flask import jsonify
from utils.utils import password_encrypt

def get_all_users():
    """
    This function retrieves all users from the database and returns their details in JSON format.

    Response Format:
    ----------------
    The function returns a list of all users in the database. Each user is represented as a dictionary with the following fields:
    - id (int): The unique identifier of the user.
    - name (str): The name of the user.
    - email (str): The email address of the user.
    - password (str): The user password.

    Response Codes:
    ---------------
    - 200: Successfully retrieved all users. Returns the user data in JSON format.
    """

    session = database_connect("flask_initialization")

    users = session.query(User).all()

    return jsonify([user.to_dict() for user in users]), 200

def add_single_user(data):
    """
    This function handles the creation of a new user in the system.
    It receives user data in JSON format, validates the required fields,
    encrypts the password, and saves the new user in the database.

    Input Parameters:
    -----------------
    - name (str): The name of the user (required).
    - email (str): The email of the user (required, must be unique).
    - password (str): The user's password (required, will be stored encrypted).

    Expected Input Format (JSON):
    -----------------------------
    {
        "name": "User's Name",
        "email": "user@example.com",
        "password": "secure_password"
    }

    Response Codes:
    ---------------
    - 201: User created successfully. Returns user details in JSON format.
    - 400: Validation error, one or more required fields are missing in the request.
    - 500: Internal server error while attempting to save the user in the database.
    """

    session = database_connect("flask_initialization")

    if not data or not data.get('name') or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Name, email and password are required'}), 400

    password = password_encrypt(data.get("password"))

    new_user = User(name=data['name'], email=data['email'], password=password)

    try:
        session.add(new_user)
        session.commit()
        return jsonify(new_user.to_dict()), 201
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
