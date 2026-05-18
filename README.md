# 🛵 Projeto Delivery - FastAPI

API REST de um sistema de delivery desenvolvida com FastAPI e Python.

## 📋 Sobre o projeto
Sistema que permite o cadastro de usuários e criação de pedidos,
com senhas criptografadas e banco de dados SQLite.

## 🚀 Tecnologias utilizadas
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Alembic
- Passlib (bcrypt)

## 📁 Estrutura do projeto
- `main.py` — ponto de entrada da aplicação
- `models.py` — tabelas do banco de dados
- `schemas.py` — validação dos dados
- `auth_routes.py` — rotas de autenticação
- `order_routes.py` — rotas de pedidos
- `dependencies.py` — conexão com o banco

## ⚙️ Como rodar o projeto
```bash
uvicorn main:app --reload
```
Acesse a documentação em: http://127.0.0.1:8000/docs