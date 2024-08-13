from fastapi import APIRouter, HTTPException, Depends
from db import users_collection, sessions_collection, cc_collection
from models import UpdateSaldo, abastecimento
from datetime import timedelta

def binValues(card: str) -> str:
    if card[0:6] == "480209":
        nivel = "BUSINESS"

    if nivel == "BUSINESS":
        valor = 30
    return valor