import os
from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv

load_dotenv()

# pegando a variavel que esta no arquivo .env
SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

# cria o algoritmo para criptografar a senha, e faz com que algoritmos antigos sejam marcados como insguros automaticamente
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#importando os dois arquivos de autenticação e pedidos
from auth_routes import auth_router
from order_routes import order_router

# rodar esse codigo no terminal - uvicorn main:app --reload

app.include_router(auth_router)
app.include_router(order_router)






