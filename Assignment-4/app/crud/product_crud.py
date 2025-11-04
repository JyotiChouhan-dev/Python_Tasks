from sqlalchemy.orm import Session
from sqlalchemy import or_, String
from fastapi import HTTPException
from app.models.product import Product
from app.schemas.product_schema import ProductCreate

def create_product(db: Session, product: ProductCreate):
    existing = db.query(Product).filter(
        Product.name == product.name
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Product already exists for this company")

    db_product = Product(
        name=product.name,
        price=product.price,
        stock=product.stock,
        company_id=product.company_id,
        category_id=product.category_id
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Product).offset(skip).limit(limit).all()


def get_product_by_id(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    return product


def update_product(db: Session, product_id: int, updated_data: ProductCreate):
    product = get_product_by_id(db, product_id)
    if not product:
        return None
    product.name = updated_data.name
    product.price = updated_data.price
    product.stock = updated_data.stock
    product.company_id = updated_data.company_id
    product.category_id = updated_data.category_id
    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product_id: int):
    product = get_product_by_id(db, product_id)
    if not product:
        return False
    db.delete(product)
    db.commit()
    return True


def search_products(db: Session, q: str = "", company_id: int | None = None, skip: int = 0, limit: int = 10):
    query = db.query(Product)

    if company_id:
        query = query.filter(Product.company_id == company_id)

    if q:
        query = query.filter(
            or_(
                Product.name.ilike(f"%{q}%"),
                Product.price.cast(String).ilike(f"%{q}%")
            )
        )

    return query.offset(skip).limit(limit).all()
