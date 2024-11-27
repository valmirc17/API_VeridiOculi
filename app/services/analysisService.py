from app.models.analysisModel import Analysis

def get_user_analysis(user_id):
    return Analysis.get_all(user_id)

def get_analysis_by_id(_id):
    return Analysis.find_one(_id)
