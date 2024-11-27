from bson import ObjectId
from app import mongo

class Analysis:
    @staticmethod
    def get_all(user_id):
        print(user_id)
        try:
            analyses = mongo.db.analysis.find(user_id)
            analysis = [str(analysis['_id']) for analysis in analyses]
            return analysis
        
        except Exception as e:
            raise ValueError(f"Erro ao buscar análises: {str(e)}")

    @staticmethod
    def find_one(_id):
        try:
            if isinstance(_id, str):
                _id = ObjectId(_id)
            analysis = mongo.db.analysis.find_one({"_id": _id})

            def convert_objectid_to_str(doc):
                if doc and '_id' in doc:
                    doc['_id'] = str(doc['_id'])
                return doc

            analysis = convert_objectid_to_str(analysis)

            if analysis:
                return analysis
            else:
                raise ValueError("Análise não encontrada")

        except Exception as e:
            raise ValueError(f"Erro ao buscar análise: {str(e)}")

