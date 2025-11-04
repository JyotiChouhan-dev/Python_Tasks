from pydantic import BaseModel
from app.schemas.company_schema import CompanyResponse

class ProductBase(BaseModel):
    name: str
    price: float
    stock: int = 0
    company_id: int
    category_id: int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    # company: CompanyResponse | None = None

    class Config:
        orm_mode = True
