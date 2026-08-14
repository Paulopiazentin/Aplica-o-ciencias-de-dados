import sqlite3
import pandas as pd
import requests
import logging
from typing import Optional, List
from pydantic import BaseModel, Field, ValidationError
from Contrato import UsuariosAPISchema

def extrair_e_validar_dados_api(url_api: str):
    logging.info("Iniciando extração de dados da API")

    # dados fake da API 

    mock_api_response = [
        {"id": 1, "score_credito": 750.5, "status_ativo": True, "email": "ana.silva@example.com"},
        {"id": 2, "score_credito": 800.0, "status_ativo": False, "email": None},
        {"id": 3, "score_credito": MIL, "status_ativo": True, "email": "carla.lima@example.com"},
        {"id": 4, "score_credito": 600.0, "status_ativo": True, "email": "diego.costa@example.com"},
        {"id": 5, "score_credito": 1200.0, "status_ativo": True, "email": "elisa.martins@example.com"}
    ]

    dados_validos = []
    dados_quarentena = []

    for item in mock_api_response:
        try:
            registro_valido = UsuariosAPISchema(**item)
            dados_validos.append(registro_valido.model_dump())
        except ValidationError as e:
            logging.warning(f"Erro de validação para o item {item['id']}: {e}")
            item['erro'] = str(e)
            dados_quarentena.append(item)

    return pd.DataFrame(dados_validos), pd.DataFrame(dados_quarentena)