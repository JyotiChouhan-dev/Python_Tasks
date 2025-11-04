from fastapi import FastAPI
from app.database.database import Base, engine
from app.utils.logger import logger
from app.core.config import settings
from app.models import company, product, category
from app.routers import company_routes, product_routes, category_routes

# Initialize FastAPI app
app = FastAPI(title=settings.APP_NAME)

# Log startup
logger.info(" Starting FastAPI Application...")

# Create all database tables
Base.metadata.create_all(bind=engine)
logger.info(" All database tables created successfully.")

# Include routers
app.include_router(company_routes.router)
app.include_router(product_routes.router)
app.include_router(category_routes.router)

@app.get("/")
def root():
    logger.info(" Root endpoint accessed.")
    return {"message": "Welcome to FastAPI Inventory System!"}
