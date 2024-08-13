from fastapi import FastAPI, Depends
from routers import auth_router,logado,admin_router,checkers
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from auth import get_current_user

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Substitua pelo domínio do seu front-end
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

app.include_router(auth_router.router, prefix="/auth")
app.include_router(logado.router, prefix="/user")
app.include_router(admin_router.router, prefix="/admin-side")
app.include_router(checkers.router, prefix="/checkers")

@app.get("/protected")
async def read_protected_route(current_user: dict = Depends(get_current_user)):
    return {"msg": "You have access to this route!", "user": current_user}