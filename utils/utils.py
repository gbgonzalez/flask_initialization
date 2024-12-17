import bcrypt


def password_encrypt(password):
    """
    Encrypts a plaintext password using the bcrypt hashing algorithm.

    Parameters:
    - password (str): The plaintext password to be encrypted.

    Returns:
    - bytes: The hashed and salted password as a byte string.
    """

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password