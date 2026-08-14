import sqlite3
import pandas as pd
import requests
import logging
from typing import Optional, List
from pydantic import BaseModel, Field, ValidationError
from preparar_banco_de_dados import preparar_banco_de_dados
from extrair_e_validar_dados_api import extrair_e_validar_dados_api

def executar_pipeline():
    #passo 1
    preparar_banco_de_dados()

    #passo 2
    df_api_validos, df_api_quarentena = extrair_e_validar_dados_api("https://api.fake")

    if not df_api_validos.empty:
        logging.error("Existem dados válidos para serem processados.")
        return
    # passo 3 ingestão de dados SQL
    conn = sqlite3.connect('empresa.db')
    df_sql = pd.read_sql_query("SELECT * FROM clientes", conn)

    # passo 4 fusão de dados heterogenea
    logging.info("Iniciando fusão de dados heterogênea")
    df_consolidado = pd.merge(df_sql, df_api_validos, left_on='id_usuario', right_on='id', how='inner').drop(columns=['id'])

    # passo 5 carga de dados
    df_consolidado.to_sql('base_gold_ia', conn, index=False)
    conn.close()


    # Relatorio

    print("Relatório de execução do pipeline:")
    total = len(df_api_validos) + len(df_api_quarentena)
    print("registros totais processados:", total)
    print("registros válidos:", len(df_api_validos))
    print("registros em quarentena:", len(df_api_quarentena))

if __name__ == "__main__":
    logging.info("Iniciando execução do pipeline")
    executar_pipeline()
    logging.info("Execução do pipeline finalizada")