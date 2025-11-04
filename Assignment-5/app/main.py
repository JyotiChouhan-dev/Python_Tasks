# app/main.py
from fastapi import FastAPI
from app.core.config import connect_db, disconnect_db
from app.routers import company_router, product_router
import logging

# -----------------------------------------------
# Basic Logging Setup
# -----------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app.main")

# -----------------------------------------------
# FastAPI App Initialization
# -----------------------------------------------
app = FastAPI(
    title="Product Management API (Prisma + FastAPI)",
    version="1.0.0",
    description="API for managing companies and products with search and pagination."
)

# -----------------------------------------------
# Routers Registration
# -----------------------------------------------
app.include_router(company_router.router)
app.include_router(product_router.router)

# -----------------------------------------------
# Startup & Shutdown Events (DB connect/disconnect)
# -----------------------------------------------
@app.on_event("startup")
async def on_startup():
    logger.info("Starting FastAPI app...")
    await connect_db()

@app.on_event("shutdown")
async def on_shutdown():
    logger.info("Shutting down FastAPI app...")
    await disconnect_db()

# -----------------------------------------------
# Root Endpoint
# -----------------------------------------------
@app.get("/")
def root():
    return {"message": "🚀 Product Management API with Prisma is running!"}
