# app/crud/company_crud.py
from fastapi import HTTPException, status
from app.core.config import prisma
from app.schemas.company_schema import CompanyCreate, CompanyUpdate

# ---------------- CREATE ----------------
async def create_company(company_data: CompanyCreate):
    existing = await prisma.company.find_unique(where={"name": company_data.name})
    if existing:
        raise HTTPException(status_code=400, detail="Company already exists")
    return await prisma.company.create(data=company_data.dict())

# ---------------- READ ALL ----------------
async def get_all_companies():
    return await prisma.company.find_many()

# ---------------- READ BY ID ----------------
async def get_company_by_id(company_id: int):
    company = await prisma.company.find_unique(where={"id": company_id})
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company

# ---------------- UPDATE ----------------
async def update_company(company_id: int, company_data: CompanyUpdate):
    existing = await prisma.company.find_unique(where={"id": company_id})
    if not existing:
        raise HTTPException(status_code=404, detail="Company not found")

    update_data = company_data.dict(exclude_unset=True)
    return await prisma.company.update(where={"id": company_id}, data=update_data)

# ---------------- DELETE ----------------
async def delete_company(company_id: int):
    existing = await prisma.company.find_unique(where={"id": company_id})
    if not existing:
        raise HTTPException(status_code=404, detail="Company not found")
    await prisma.company.delete(where={"id": company_id})
    return {"message": "Company deleted successfully"}
