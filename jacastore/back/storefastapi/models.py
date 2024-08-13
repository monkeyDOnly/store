from pydantic import BaseModel, Field,field_validator
from typing import Optional, List
import re

class UserBase(BaseModel):
    username: str = Field(..., min_length=4, description="The username must be at least 4 characters long.")
    password: str = Field(..., min_length=4, description="The password must be at least 4 characters long.")

class UserInDB(UserBase):
    username: str
    hashed_password: str
    saldo: float = Field(default=0.0, ge=0)

class Token(BaseModel):
    access_token: str
    token_type: str

class Login(BaseModel):
    username: str
    password: str

class UpdateSaldo(BaseModel):
    username: str
    adicional: float

    @field_validator('adicional', mode='before')
    def check_adicional(cls, v):
        if v < 0:
            raise ValueError('O valor do saldo não pode ser negativo.')
        return v

class Market_cc(BaseModel):
    card: str
    valor: float
    card_token: str

class listacc(BaseModel):
    lista: str
    lines: List[str] = []

    @field_validator('lines', mode='before')
    def split_lines(cls, v, values):
        raw_data = values.get('lista', '')
        return raw_data.split('\n')
    
class abastecimento(BaseModel):
    card: str
    valor: float = Field(default=0.0, ge=0)
    tipo: str

    @field_validator('valor', mode='before')
    def check_valor(cls, v):
        if v <= 0:
            raise ValueError('O valor do saldo não pode ser negativo.')
        return v

    @field_validator('tipo', mode='before')
    def check_tipo(cls, v):
        if v != "market_cc" and v != "market_gg" and v != "market_trilha":
            raise ValueError('Tipo de info invalida, aceitas no momento apenas market_cc, market_gg, market_trilha')
        return v
    
class CPFbrada(BaseModel):
    cpf: str

    @field_validator('cpf', mode='before')
    def validate_and_format_cpf(cls, v):
        # Remover caracteres não numéricos
        cleaned_cpf = re.sub(r'\D', '', v)
        
        # Verificar se o CPF tem exatamente 11 dígitos
        if len(cleaned_cpf) != 11:
            raise ValueError('O CPF deve conter exatamente 11 dígitos.')
        
        return cleaned_cpf