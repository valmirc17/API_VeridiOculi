from flask import Blueprint, request, jsonify
from app.services.analysisService import get_user_analyses
from app.utils.jwtUtils import decode_token

analysis_bp = Blueprint("analyses", __name__)

@analysis_bp.route("/", methods=["GET"])
def get_analyses():
    user = decode_token(request.headers.get("Authorization"))
    analyses = get_user_analyses(str(user["_id"]))
    return jsonify(analyses)
