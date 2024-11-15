import jwt
from flask import current_app

def create_token(user_id):
    payload = {"user_id": user_id}
    return jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")

def decode_token(token):
    return jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
