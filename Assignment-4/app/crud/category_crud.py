from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category_schema import CategoryCreate

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Category).offset(skip).limit(limit).all()

def get_category_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def get_category_by_name(db: Session, name: str):
    return db.query(Category).filter(Category.name == name).first()

def update_category(db: Session, category_id: int, updated_data: CategoryCreate):
    category = get_category_by_id(db, category_id)
    if not category:
        return None
    category.name = updated_data.name
    # category.description = updated_data.description
    db.commit()
    db.refresh(category)
    return category

def delete_category(db: Session, category_id: int):
    category = get_category_by_id(db, category_id)
    if category:
        db.delete(category)
        db.commit()
        return True
    return False
