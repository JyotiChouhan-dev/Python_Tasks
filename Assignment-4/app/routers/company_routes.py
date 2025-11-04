from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.utils.logger import logger
from app.schemas import company_schema as schemas
from app.crud import company_crud

router = APIRouter(
    prefix="/companies",
    tags=["Companies"]
)

# CREATE Company
@router.post("/", response_model=schemas.CompanyResponse)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating company: {company.name}")
    existing = company_crud.get_company_by_name(db, company.name)
    if existing:
        raise HTTPException(status_code=400, detail="Company already exists")

    new_company = company_crud.create_company(db, company)
    return new_company


# READ all Companies
@router.get("/", response_model=list[schemas.CompanyResponse])
def get_companies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return company_crud.get_companies(db, skip, limit)


# READ Company by ID
@router.get("/{company_id}", response_model=schemas.CompanyResponse)
def get_company(company_id: int, db: Session = Depends(get_db)):
    company = company_crud.get_company_by_id(db, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


# UPDATE Company
@router.put("/{company_id}", response_model=schemas.CompanyResponse)
def update_company(company_id: int, updated_data: schemas.CompanyCreate, db: Session = Depends(get_db)):
    company = company_crud.update_company(db, company_id, updated_data)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    logger.info(f"Updated company: {company.name}")
    return company


# DELETE Company
@router.delete("/{company_id}")
def delete_company(company_id: int, db: Session = Depends(get_db)):
    success = company_crud.delete_company(db, company_id)
    if not success:
        raise HTTPException(status_code=404, detail="Company not found")
    logger.info(f"Deleted company with id {company_id}")
    return {"message": "Company deleted successfully"}
