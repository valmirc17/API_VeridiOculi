from dotenv import load_dotenv
import os
import openai


def generate_report_from_analysis(analysis_data, image_url):
    try:
        prompt = f"""
        Crie um relatório detalhado de inventário florestal com base nos seguintes dados:
        
        Dados da análise: {analysis_data}
        
        A análise deve seguir o seguinte modelo:
        - ID da Análise
        - Data da Análise
        - Localização (com latitude e longitude)
        - Resumo das identificações (com alta, média e baixa confiança)
        - Detalhes dos pontos de identificação (com coordenadas e confiança)
        - Imagem associada: {image_url}
        
        Siga o formato JSON com base no modelo do relatório já definido.
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente especializado em criação de relatórios."},
                {"role": "user", "content": prompt}
            ]
        )
        # Retorna o conteúdo gerado pelo modelo
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Erro ao gerar relatório: {e}")
        return None