import os
from dotenv import load_dotenv
from prisma import Prisma

# Load environment variables from .env
load_dotenv()

# Initialize Prisma database client
db = Prisma()

# Environment variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# You can use these to form a connection string if needed (Prisma uses schema.prisma instead)
DATABASE_URL = (
    f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
