from fastapi import APIRouter, HTTPException, Depends, Header
from db import users_collection, sessions_collection
from models import UserBase, Login, Token
from auth import verify_password, get_password_hash, create_access_token, decode_access_token, update_session, get_current_user
from datetime import timedelta

router = APIRouter()

@router.post("/register")
async def register(user: UserBase):
    existing_user = users_collection.find_one({"username": user.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    #users_collection.insert_one({"username": user.username, "hashed_password": hashed_password})
    #return {"message": "User created successfully"}
    user_in_db = {
        "username": user.username,
        "hashed_password": hashed_password,
        "saldo": 0.0,
    }
    result = users_collection.insert_one(user_in_db)
    if result.inserted_id:
        return {"message": "User created successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to create user")


@router.post("/login", response_model=Token)
async def login(login: Login):
    user = users_collection.find_one({"username": login.username})

    if not user or not verify_password(login.password, user['hashed_password']):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token_expires = timedelta(minutes=60)

    access_token = create_access_token(
        data={"sub": login.username}, expires_delta=access_token_expires
    )
    update_session(username=login.username, token=access_token)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/verify-token")
async def verify_token(token: str):
    try:
        decoded = decode_access_token(token)
        return {"token_data": decoded}
    except HTTPException:
        raise HTTPException(status_code=401, detail="Invalid token")
    
@router.get("/logout")
async def logout(authorization: str = Header(None)):
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=400, detail="Invalid authorization header")
    
    token = authorization[len("Bearer "):]
    
    # Revoga o token removendo a sessão
    result = sessions_collection.delete_one({"access_token": token})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Session not found")
    
    return {"message": "Logged out successfully"}
