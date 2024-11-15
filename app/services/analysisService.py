from app.models import Analysis

def get_user_analyses(user_id):
    return Analysis.find_by_user(user_id)
