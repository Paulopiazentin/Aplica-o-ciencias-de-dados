import sqlite3
import pandas as pd
import requests
import logging
from typing import Optional, List
from pydantic import BaseModel, Field, ValidationError

class UsuariosAPISchema(BaseModel):
    id: int
    score_credito: float = Field(..., ge= 0.0, le= 1000.00, description="Score de crédito do usuário, entre 0.0 e 1000.00")
    status_ativo: bool = Field(..., description="Indica se o usuário está ativo ou não")
    email: Optional[str] = Field(None, description="Email do usuário, caso disponível")