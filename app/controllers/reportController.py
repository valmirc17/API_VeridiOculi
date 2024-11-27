from flask import Blueprint, request, jsonify
from app.services.reportService import generate_report, get_user_reports
from app.utils.jwtUtils import decode_token

report_bp = Blueprint("reports", __name__)

@report_bp.route("/", methods=["GET"])
def get_reports():
    user = decode_token(request.headers.get("Authorization"))
    reports = get_user_reports(user["_id"])
    return jsonify(reports)

@report_bp.route("/generate", methods=["POST"])
def create_report():
    user = decode_token(request.headers.get("Authorization"))
    analyses = request.json["analyses"]
    report = generate_report(user["_id"], analyses)
    return jsonify(report), 201
