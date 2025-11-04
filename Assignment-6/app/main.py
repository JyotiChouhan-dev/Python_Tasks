from fastapi import FastAPI
from app.core.startup import setup_lifecycle
from app.routers.client_router import router as client_router

# Initialize FastAPI app
app = FastAPI(
    title="File Handling and Data Operations API",
    version="1.0.0",
    description="API for CSV upload, manual data entry, and export using Prisma ORM"
)

# Setup database connect/disconnect lifecycle
setup_lifecycle(app)

# Register routers
app.include_router(client_router)


# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the File Handling and Data Operations API!"}
