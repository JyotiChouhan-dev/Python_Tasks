from pydantic import BaseModel, EmailStr
from typing import Optional


# Schema for creating a new client (used in POST /add)
class ClientCreate(BaseModel):
    name: str
    email: EmailStr
    about: Optional[str] = None


# Schema for reading or returning client data
class ClientRead(BaseModel):
    id: int
    name: str
    email: EmailStr
    about: Optional[str] = None

    class Config:
        orm_mode = True
