from fastapi import APIRouter, HTTPException, Depends, Header
from db import users_collection, sessions_collection
from auth import verify_password, get_password_hash, create_access_token, decode_access_token, update_session, get_current_user
from datetime import timedelta
from apis.brada import run
from models import CPFbrada

router = APIRouter()

@router.get("/info")
async def read_protected_route(current_user: dict = Depends(get_current_user)):
    user = users_collection.find_one({"username": current_user["sub"]})
    return {
        "username": user["username"],
        "saldo": user["saldo"]
    }