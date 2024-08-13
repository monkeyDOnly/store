from fastapi import APIRouter, HTTPException, Depends
from db import users_collection, sessions_collection
from auth import verify_password, get_password_hash, create_access_token, decode_access_token, update_session, get_current_user
from functions import binValues
from models import UpdateSaldo, abastecimento
from datetime import timedelta
import json

router = APIRouter()

@router.post("/users/saldo/add")
async def read_protected_route(update_saldo: UpdateSaldo, current_user: dict = Depends(get_current_user)):
    user = users_collection.find_one({"username": update_saldo.username})
    if user:
        new_saldo = user.get("saldo", 0) + update_saldo.adicional
        users_collection.update_one({"username": update_saldo.username}, {"$set": {"saldo": new_saldo}})
        return {"saldo": new_saldo}
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
@router.post("/users/saldo/remover")
async def read_protected_route(update_saldo: UpdateSaldo, current_user: dict = Depends(get_current_user)):
    user = users_collection.find_one({"username": update_saldo.username})
    if user:
        new_saldo = user.get("saldo", 0) - update_saldo.adicional
        if new_saldo < 0:
            new_saldo = 0
        users_collection.update_one({"username": update_saldo.username}, {"$set": {"saldo": new_saldo}})
        return {"saldo": new_saldo}
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router.post("/card/add")
async def read_protected_route(infos: abastecimento, current_user: dict = Depends(get_current_user)):
    print(infos.card)
    
    lista = infos.card.split("\n")[0]

    infos.valor = int(binValues(lista))
    
    #user = users_collection.find_one({"username": current_user["sub"]})
    return infos