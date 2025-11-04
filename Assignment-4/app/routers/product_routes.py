from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas import product_schema as schemas
from app.crud import product_crud
from app.utils.logger import logger

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


# CREATE Product
@router.post("/add", response_model=schemas.ProductResponse)
def create_product_endpoint(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating product: {product.name}")
    new_product = product_crud.create_product(db, product)
    return new_product


# READ all Products
@router.get("/", response_model=list[schemas.ProductResponse])
def get_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return product_crud.get_products(db, skip, limit)


# READ single Product
@router.get("/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = product_crud.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# UPDATE Product
@router.put("/{product_id}", response_model=schemas.ProductResponse)
def update_product(product_id: int, updated_data: schemas.ProductCreate, db: Session = Depends(get_db)):
    product = product_crud.update_product(db, product_id, updated_data)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    logger.info(f"Updated product: {updated_data.name}")
    return product


# DELETE Product
@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted = product_crud.delete_product(db, product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    logger.info(f"Deleted product with id {product_id}")
    return {"message": "Product deleted successfully"}


# SEARCH Products
@router.get("/search/", response_model=list[schemas.ProductResponse])
def search_products(
        q: str = Query("", description="Search query for name or price"),
        company_id: int | None = Query(None, description="Optional filter by company ID"),
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db)
):
    products = product_crud.search_products(db, q, company_id, skip, limit)
    if not products:
        raise HTTPException(status_code=404, detail="No matching products found")
    logger.info(f"Searched products with query='{q}', company_id={company_id}")
    return products
