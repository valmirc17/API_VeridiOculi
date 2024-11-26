from app.models.analysisModel import Analysis
from bson import ObjectId

def get_user_analysis(user_id):
    return Analysis.get_all(user_id)
