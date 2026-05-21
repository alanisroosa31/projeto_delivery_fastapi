from pydantic import BaseModel
from typing import Optional

# classe que define oque um usuario precisa
class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]

    class ItemPedidoSchema(BaseModel):
        sabor: str
        tamanho: str
        preco_unitario: float
        quantidade: int


    class Config:
        from_attributes = True

class PedidoSchema(BaseModel):
    id_usuario: int

    class Config:
        from_attributes = True