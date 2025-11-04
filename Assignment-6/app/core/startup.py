# from app.core.config import db
#
# async def connect_db():
#     await db.connect()
#
# async def disconnect_db():
#     await db.disconnect()
#


from fastapi import FastAPI
from app.core.config import db

# Function to run when app starts
async def connect_to_database():
    try:
        await db.connect()
        print(" Database connected successfully.")
    except Exception as e:
        print(" Database connection failed:", e)


# Function to run when app shuts down
async def disconnect_from_database():
    try:
        await db.disconnect()
        print(" Database disconnected.")
    except Exception as e:
        print("️ Error while disconnecting database:", e)


# Function to include startup and shutdown events in FastAPI app
def setup_lifecycle(app: FastAPI):
    @app.on_event("startup")
    async def startup():
        await connect_to_database()

    @app.on_event("shutdown")
    async def shutdown():
        await disconnect_from_database()
