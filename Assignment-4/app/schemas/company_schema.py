from pydantic import BaseModel

class CompanyBase(BaseModel):
    name: str
    location: str | None = None

class CompanyCreate(CompanyBase):
    pass

class CompanyResponse(CompanyBase):
    id: int

    class Config:
        orm_mode = True
