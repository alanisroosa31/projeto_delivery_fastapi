# importando as bibliotecas, APIRouter cria o roteador fora do main, o models importa a classe e instancia Usuario do db, e o sessionmaker serve para conversas temporárias com o banco de dados
from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependencies import pegar_sessao
from main import bcrypt_context
from schemas import UsuarioSchema
from sqlalchemy.orm import Session


# prefixo auth em todos os endpoints e organiza a documentação na tag AUTH
auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get("/")
async def home():
    return {"mensagem": "você acessou a rota padrão de autenticação", "autenticado": False}


@auth_router.post("/criar_conta")

# função assincrona que pega os prefixos que precisamos para a criação da conta e inicia uma conversa temporaria com o banco de dados
async def criar_conta( usuario_schema: UsuarioSchema, session: Session = Depends(pegar_sessao)):

#o session faz uma query na instancia usuario da nossa clase para ver se ja existe algum usuario com esse email
    usuario = session.query(Usuario).filter(Usuario.email == usuario_schema.email).first()

# se tiver um email igual ja cadastrado, o sistema retorna uma mensagem
    if usuario:
        raise HTTPException(status_code=400, detail="Email do usuário ja cadastrado")

# se nao existir entao criamos um usuario com os parametros definidos
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email ,senha_criptografada, usuario_schema.ativo, usuario_schema.admin)
        # o session adiciona um novo usuario no banco
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": f"usuário criado com sucesso {usuario_schema.email}"}