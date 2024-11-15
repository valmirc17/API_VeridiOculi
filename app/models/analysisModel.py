from app import mongo

class Analysis:
    @staticmethod
    def find_by_user(user_id):
        return list(mongo.db.analyses.find({"user_id": user_id}))
