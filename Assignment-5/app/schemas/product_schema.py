from pydantic import BaseModel
from typing import Optional
from .company_schema import CompanyRead

class ProductBase(BaseModel):
    name: str
    price: float
    stock: int
    company_id: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    company_id: Optional[int] = None

class ProductRead(ProductBase):
    id: int
    company: Optional[CompanyRead] = None

    class Config:
        from_attributes = True
