from bson import ObjectId
from app import mongo

class Analysis:
    @staticmethod
    def get_all(user_id):
        print(user_id)
        """ Retorna todos os IDs das análises de um usuário específico """
        try:
            # Consultando todas as análises do usuário com o user_id fornecido
            analyses = mongo.db.analysis.find(user_id)
            #print(f"Documentos encontrados: {list(analyses)}")
            # Criando uma lista com todos os IDs dos documentos encontrados
            analysis = [str(analysis['_id']) for analysis in analyses]
            return analysis
        
        except Exception as e:
            raise ValueError(f"Erro ao buscar análises: {str(e)}")

    @staticmethod
    def find_one(_id):
        """ Retorna uma análise específica usando o ID da análise """
        try:
            # Verifica se o _id recebido é uma string e converte para ObjectId
            if isinstance(_id, str):
                _id = ObjectId(_id)  # Converte a string para ObjectId
                
            # Realiza a consulta no MongoDB utilizando o _id como ObjectId
            analysis = mongo.db.analysis.find_one({"_id": _id})

            def convert_objectid_to_str(doc):
                if doc and '_id' in doc:
                    doc['_id'] = str(doc['_id'])  # Converte o ObjectId para string
                return doc

            analysis = convert_objectid_to_str(analysis)

            # Imprime o resultado da consulta para depuração
            print(f"Documentos encontrados: {analysis}")

            # Verifica se uma análise foi encontrada
            if analysis:
                return analysis
            else:
                raise ValueError("Análise não encontrada")

        except Exception as e:
            raise ValueError(f"Erro ao buscar análise: {str(e)}")

