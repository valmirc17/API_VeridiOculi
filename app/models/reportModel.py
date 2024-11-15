from app import mongo

class Report:
    @staticmethod
    def find_by_user(user_id):
        return list(mongo.db.reports.find({"user_id": user_id}))

    @staticmethod
    def insert_report(report_data):
        mongo.db.reports.insert_one(report_data)
