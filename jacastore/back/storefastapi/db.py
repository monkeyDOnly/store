from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env


# Obtenha a URI do MongoDB e o nome do banco de dados das variáveis de ambiente
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

# Verifique se o nome do banco de dados é uma string
if not isinstance(DB_NAME, str):
    raise ValueError(f"DB_NAME must be a string, but got {type(DB_NAME).__name__}")

# Conecte-se ao MongoDB e selecione o banco de dados
client = MongoClient(MONGO_URI)
db = client[DB_NAME]  # Use o nome do banco de dados
users_collection = db.users
sessions_collection = db.sessions
cc_collection = db.market_cc
trilha_collection = db.market_trilha
gg_collection = db.market_gg

users_collection.create_index("username", unique=True)

def add_usuario(usuario_data):
    """Adiciona um usuário ao MongoDB"""
    result = users_collection.insert_one(usuario_data.dict())
    return result.inserted_id
