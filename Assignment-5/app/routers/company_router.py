# app/routers/company_router.py
from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.company_schema import CompanyCreate, CompanyUpdate, CompanyRead
from app.crud import company_crud

router = APIRouter(prefix="/companies", tags=["Companies"])

# ---------- CREATE ----------
@router.post("/", response_model=CompanyRead)
async def create_company(company: CompanyCreate):
    return await company_crud.create_company(company)

# ---------- GET ALL ----------
@router.get("/", response_model=List[CompanyRead])
async def get_all_companies():
    return await company_crud.get_all_companies()

# ---------- GET BY ID ----------
@router.get("/{company_id}", response_model=CompanyRead)
async def get_company(company_id: int):
    return await company_crud.get_company_by_id(company_id)

# ---------- UPDATE ----------
@router.put("/{company_id}", response_model=CompanyRead)
async def update_company(company_id: int, company: CompanyUpdate):
    return await company_crud.update_company(company_id, company)

# ---------- DELETE ----------
@router.delete("/{company_id}")
async def delete_company(company_id: int):
    return await company_crud.delete_company(company_id)
