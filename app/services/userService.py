import bcrypt
from app.models.userModel import User
from app.utils.jwtUtils import *

def authenticate_user(email, password):
    """
    Autentica o usuário e retorna o token JWT se as credenciais forem válidas.
    """
    user = User.find_by_email(email)

    if user and bcrypt.checkpw(password.encode(), user["password"]):
        # Gera o token JWT com o ID do usuário
        return create_token(str(user["_id"]))
    
    return None

def register_user(email, password):
    """
    Registra um novo usuário com senha criptografada.
    """
    if User.find_by_email(email):
        raise ValueError("User already exists")
    
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    User.insert_user({"email": email, "password": hashed_password})
