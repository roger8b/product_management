#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
import os

from product_management.crew import ProductManagement

from .business import problem

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

from datetime import datetime

import json

def salvar_conteudo(conteudo, nome_base, extensao=".txt", caminho="./result/"):
    """
    Versão simplificada para salvar conteúdo em arquivo.
    
    Args:
        conteudo (str): Conteúdo a ser salvo
        nome_base (str): Nome base do arquivo
        extensao (str): Extensão do arquivo
        caminho (str): Caminho do diretório onde salvar
    
    Returns:
        str: Caminho completo do arquivo criado
    """
    try:
        # Cria o diretório se não existir
        os.makedirs(caminho, exist_ok=True)
        
        # Gera o nome do arquivo com timestamp
        nome_arquivo = f"{nome_base}_{datetime.now().strftime('%Y%m%d_%H%M%S')}{extensao}"
        
        # Caminho completo do arquivo
        caminho_completo = os.path.join(caminho, nome_arquivo)
        
        # Salva o arquivo
        with open(caminho_completo, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        
        print(f"Arquivo criado: {caminho_completo}")
        return caminho_completo
        
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")
        raise

def run():
    """
    Run the crew.
    """
    inputs = {
        'problem': problem
    }
    
    try:
        crew = ProductManagement().crew()
        crew_output = crew.kickoff(inputs=inputs)
        print(f"Crew output: {crew_output}")
        #salvar_conteudo(crew_output.json(), "product_requirement_document", ".json", "./result/")
        print(f"Crew usage metrics:")
        print(crew.usage_metrics)

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        ProductManagement().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
        

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ProductManagement().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        ProductManagement().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
