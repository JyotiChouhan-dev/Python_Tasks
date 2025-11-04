# app/schemas/company_schema.py
from pydantic import BaseModel
from typing import Optional

# Base schema for shared fields
class CompanyBase(BaseModel):
    name: str
    location: str

# For creating a company (POST)
class CompanyCreate(CompanyBase):
    pass

# For updating a company (PUT/PATCH)
class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None

# For reading a company (GET)
class CompanyRead(CompanyBase):
    id: int

    class Config:
        orm_mode = True
