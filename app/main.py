from fastapi import FastAPI
from app.routers import sales
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="iPhone Sales Tracker API")

app.include_router(sales.router)
