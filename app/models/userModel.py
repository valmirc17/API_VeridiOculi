from app import mongo

class User:
    @staticmethod
    def find_by_email(email):
        return mongo.db.users.find_one({"email": email})

    @staticmethod
    def insert_user(user_data):
        mongo.db.users.insert_one(user_data)