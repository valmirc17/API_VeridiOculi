from bson import ObjectId
from app import mongo

class Analysis:
    @staticmethod
    def get_all(user_id):
        """ Retorna todas as análises de um usuário específico """
        try:
            analysis = mongo.db.analysis.find({"user_id": ObjectId(user_id)})
            return [analysis for analysis in analysis]
        except Exception as e:
            raise ValueError(f"Erro ao buscar análises: {str(e)}")

    @staticmethod
    def find_one(_id):
        """ Retorna uma análise específica usando o ID da análise """
        try:
            analysis = mongo.db.analyses.find_one({"_id": ObjectId(_id)})
            if analysis:
                return analysis
            else:
                raise ValueError("Análise não encontrada")
        except Exception as e:
            raise ValueError(f"Erro ao buscar análise: {str(e)}")
