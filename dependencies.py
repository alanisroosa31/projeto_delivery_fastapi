from models import db
from sqlalchemy.orm import sessionmaker

def pegar_sessao():
    try:
        session = sessionmaker(bind=db)
        sessao = session()
        yield sessao
    finally:
        sessao.close()


