from pydantic import BaseModel

class PedidoCreate(BaseModel):
    id_cliente: int

class ItemPedidoCreate(BaseModel):
    id_produto: int
    quantidade: int

class PedidoResponse(BaseModel):
    id: int
    valor_total: float
    id_cliente: int
    status: str

    class Config:
        from_attributes = True