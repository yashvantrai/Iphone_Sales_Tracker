from pydantic import BaseModel
from datetime import date
from typing import Optional

class SaleCreate(BaseModel):
    customer_name: str
    phone_model: str
    color: str
    storage_gb: int
    price: float
    sale_date: date
    store_location: str

class Sale(SaleCreate):
    id: int
    created_at: Optional[str]

    class Config:
        orm_mode = True

class SaleStats(BaseModel):
    total_sales: int
    total_revenue: float
    most_popular_model: str
    average_price: float
