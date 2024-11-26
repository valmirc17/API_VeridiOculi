from flask import Blueprint, request, jsonify
from app.services.userService import *
from app.models.userModel import *


user_bp = Blueprint("users", __name__)

@user_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    print(data)
    try:
        register_user(data["email"], data["password"])
        return jsonify({"message": "Usuário registrado com sucesso!"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@user_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    token = authenticate_user(data["email"], data["password"])
    user = User.find_by_email(data['email'])

    if token:
        return jsonify({
            'message': 'Login realizado com sucesso',
            'token': token,  # Retornando o token JWT gerado
            'user': {
                'nome': user['nome'],
                'email': user['email']
            }
        }), 200

    return jsonify({"error": "Credenciais inválidas!"}), 401

