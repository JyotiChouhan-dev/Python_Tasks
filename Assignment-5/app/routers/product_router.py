from fastapi import APIRouter, Query
from typing import List, Optional
from app.schemas.product_schema import ProductCreate, ProductUpdate, ProductRead
from app.crud import product_crud
from app.core.config import prisma

router = APIRouter(prefix="/products", tags=["Products"])

# ---------- CREATE ----------
@router.post("/", response_model=ProductRead)
async def create_product(product: ProductCreate):
    return await product_crud.create_product(product)

# ---------- GET ALL ----------
@router.get("/", response_model=List[ProductRead])
async def get_all_products():
    return await product_crud.get_all_products()

# ---------- GET BY ID ----------
@router.get("/{product_id}", response_model=ProductRead)
async def get_product(product_id: int):
    return await product_crud.get_product_by_id(product_id)

# ---------- UPDATE ----------
@router.put("/{product_id}", response_model=ProductRead)
async def update_product(product_id: int, product: ProductUpdate):
    return await product_crud.update_product(product_id, product)

# ---------- DELETE ----------
@router.delete("/{product_id}")
async def delete_product(product_id: int):
    return await product_crud.delete_product(product_id)

# ---------- SEARCH ----------
@router.get("/search/", response_model=List[ProductRead])
async def search_products(
    q: Optional[str] = Query(None, description="Search term (name/price)"),
    company_id: Optional[int] = Query(None, description="Filter by company ID"),
    skip: int = 0,
    limit: int = 10
):
    filters = {}
    if q:
        filters["OR"] = [
            {"name": {"contains": q, "mode": "insensitive"}},
            {"price": {"equals": float(q) if q.replace('.', '', 1).isdigit() else None}},
        ]
    if company_id:
        filters["company_id"] = company_id

    results = await prisma.product.find_many(
        where=filters or None,
        skip=skip,
        take=limit,
        include={"company": True}
    )
    return results
