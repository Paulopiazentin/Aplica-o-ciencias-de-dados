# IMPORTS

import sqlite3
import pandas as pd
import requests
import logging
from typing import Optional, List
from pydantic import BaseModel, Field, ValidationError

## CONFIGURAÇÃO DE LOGGING
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#setar banco de dados.

def preparar_banco_de_dados():
    """
    Função para preparar o banco de dados SQLite.
    Cria a tabela 'dados' se ela não existir.
    """
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS dados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                segmento TEXT NOT NULL);
        ''')

    #insere dados iniciais na tabela

    clientes_iniciais = [
        (1, 'Ana Silva', 'Premium'),
        (2, 'Bruno Souza', 'Standard'),
        (3, 'Carla Lima', 'Premium'),
        (4, 'Diego Costa', 'Standard'),
        (5, 'Elisa Martins', 'VIP')
    ]

    cursor.executemany('INSERT OR IGNORE INTO dados (id, nome, segmento) VALUES (?, ?, ?)', clientes_iniciais)
    conn.commit()
    conn.close()
    logging.info("Banco de dados preparado com sucesso.")