from flask import Blueprint, request, jsonify
from app.services.analysisService import *
from app.utils.jwtUtils import decode_token
from bson import ObjectId

analysis_bp = Blueprint("analysis", __name__)

@analysis_bp.route("/", methods=["GET"])
def get_analysis():
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return jsonify({"error": "Authorization header is missing"}), 401

    # Valida e remove o prefixo 'Bearer ' do token
    if not auth_header.startswith("Bearer "):
        return jsonify({"error": "Invalid Authorization header format"}), 401

    token = auth_header.split(" ")[1]  # Extrai o token após 'Bearer '

    try:
        user = decode_token(token)  # Decodifica o token JWT
    except Exception as e:
        return jsonify({"error": f"Invalid token: {str(e)}"}), 401

    # Busca análises do usuário
    analysis = get_user_analysis(user)  # Use o campo correto do payload
    return jsonify(analysis), 200

@analysis_bp.route("/<_id>", methods=["GET"])
def get_one_analysis(_id):
    print(_id)
    try:
        # Chamando a função 'find_one' do modelo
        analysis = get_analysis_by_id(_id)
        # Retornando a análise como um JSON
        return jsonify(analysis), 200
    except ValueError as e:
        # Caso a análise não seja encontrada ou ocorra erro
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        # Qualquer outro erro genérico
        return jsonify({"error": f"Erro interno: {str(e)}"}), 500
