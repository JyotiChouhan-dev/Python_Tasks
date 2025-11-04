from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.core.config import prisma
from app.schemas.product_schema import ProductCreate, ProductUpdate

# ---------------- CREATE PRODUCT ----------------
async def create_product(data: ProductCreate):
    try:
        # Check if company exists
        company = await prisma.company.find_unique(where={"id": data.company_id})
        if not company:
            raise HTTPException(status_code=404, detail="Company not found")

         # Create product
        product = await prisma.product.create(
            data={
                "name": data.name,
                "price": data.price,
                "stock": data.stock,
                "company_id": data.company_id,
            },
            include={"company": True}
        )
        return jsonable_encoder(product)

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ---------------- GET ALL PRODUCTS ----------------
async def get_all_products():
    try:
        products = await prisma.product.find_many(include={"company": True})
        return jsonable_encoder(products)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ---------------- GET PRODUCT BY ID ----------------
async def get_product_by_id(product_id: int):
    try:
        product = await prisma.product.find_unique(
            where={"id": product_id},
            include={"company": True}
        )
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return jsonable_encoder(product)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ---------------- UPDATE PRODUCT ----------------
async def update_product(product_id: int, data: ProductUpdate):
    try:
        existing_product = await prisma.product.find_unique(where={"id": product_id})
        if not existing_product:
            raise HTTPException(status_code=404, detail="Product not found")

        updated_product = await prisma.product.update(
            where={"id": product_id},
            data=data.model_dump(exclude_unset=True),
            include={"company": True}
        )
        return jsonable_encoder(updated_product)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ---------------- DELETE PRODUCT ----------------
async def delete_product(product_id: int):
    try:
        existing_product = await prisma.product.find_unique(where={"id": product_id})
        if not existing_product:
            raise HTTPException(status_code=404, detail="Product not found")

        await prisma.product.delete(where={"id": product_id})
        return {"message": f"Product with ID {product_id} deleted successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
