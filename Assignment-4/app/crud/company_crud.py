from sqlalchemy.orm import Session
from app.models.company import Company
from app.schemas.company_schema import CompanyCreate

def create_company(db: Session, company: CompanyCreate):
    db_company = Company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

def get_companies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Company).offset(skip).limit(limit).all()

def get_company_by_id(db: Session, company_id: int):
    return db.query(Company).filter(Company.id == company_id).first()

def get_company_by_name(db: Session, name: str):
    return db.query(Company).filter(Company.name == name).first()

def update_company(db: Session, company_id: int, updated_data: CompanyCreate):
    company = get_company_by_id(db, company_id)
    if not company:
        return None
    company.name = updated_data.name
    company.location = updated_data.location
    db.commit()
    db.refresh(company)
    return company

def delete_company(db: Session, company_id: int):
    company = get_company_by_id(db, company_id)
    if not company:
        return False
    db.delete(company)
    db.commit()
    return True
