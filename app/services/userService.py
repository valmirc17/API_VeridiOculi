import bcrypt
from app.models.userModel import User
from app.utils.jwtUtils import create_token

def authenticate_user(email, password):
    user = User.find_by_email(email)
    if user and bcrypt.checkpw(password.encode(), user["password"]):
        return create_token(str(user["_id"]))
    return None

def register_user(email, password):
    if User.find_by_email(email):
        raise ValueError("User already exists")
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    User.insert_user({"email": email, "password": hashed_password})
