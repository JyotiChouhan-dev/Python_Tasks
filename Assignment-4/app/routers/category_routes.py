from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas import category_schema as schemas
from app.crud import category_crud
from app.utils.logger import logger

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.post("/", response_model=schemas.CategoryResponse)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating category: {category.name}")
    existing = category_crud.get_category_by_name(db, category.name)
    if existing:
        raise HTTPException(status_code=400, detail="Category already exists")
    new_category = category_crud.create_category(db, category)
    return new_category

@router.get("/", response_model=list[schemas.CategoryResponse])
def get_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return category_crud.get_categories(db, skip, limit)

@router.get("/{category_id}", response_model=schemas.CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = category_crud.get_category_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.put("/{category_id}", response_model=schemas.CategoryResponse)
def update_category(category_id: int, updated_data: schemas.CategoryCreate, db: Session = Depends(get_db)):
    category = category_crud.update_category(db, category_id, updated_data)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    logger.info(f"Updated category: {category.name}")
    return category

@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    success = category_crud.delete_category(db, category_id)
    if not success:
        raise HTTPException(status_code=404, detail="Category not found")
    logger.info(f"Deleted category with id {category_id}")
    return {"message": "Category deleted successfully"}
