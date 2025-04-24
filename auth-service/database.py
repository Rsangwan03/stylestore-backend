from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os
import ssl
from dotenv import load_dotenv

load_dotenv()

# Use the base connection string (without ?sslmode=require)
DATABASE_URL = os.getenv("DATABASE_URL")

# Create an SSL context for asyncpg
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = True
ssl_context.verify_mode = ssl.CERT_REQUIRED

# Create the engine with SSL config
engine = create_async_engine(
    DATABASE_URL,  # keep it clean, no ?sslmode=require
    echo=True,
    future=True,
    connect_args={"ssl": ssl_context}
)

SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    async with SessionLocal() as session:
        yield session