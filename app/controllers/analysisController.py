from flask import Blueprint, request, jsonify
from app.services.analysisService import get_user_analysis
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
    analysis = get_user_analysis(ObjectId("user_id"))  # Use o campo correto do payload
    return jsonify(analysis), 200
