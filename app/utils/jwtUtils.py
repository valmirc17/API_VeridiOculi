import jwt
import base64
from flask import current_app

def get_secret_key():
    """
    Decodifica a chave secreta configurada em Base64, se necessário.
    """
    secret_key = current_app.config["SECRET_KEY"]
    try:
        # Decodifica a chave secreta em Base64, se estiver codificada
        return base64.b64decode(secret_key)
    except base64.binascii.Error:
        # Se a chave não for Base64, retorna como está
        return secret_key

def create_token(user_id):
    """
    Gera um token JWT para o usuário.
    """
    payload = {"user_id": user_id}
    secret_key = get_secret_key()
    return jwt.encode(payload, secret_key, algorithm="HS256")

def decode_token(token):
    """
    Decodifica e valida um token JWT.
    """
    secret_key = get_secret_key()
    return jwt.decode(token, secret_key, algorithms=["HS256"])
