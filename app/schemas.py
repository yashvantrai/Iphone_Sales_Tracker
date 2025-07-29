from pydantic import BaseModel
from datetime import date,datetime
from typing import Optional
from decimal import Decimal

class SaleCreate(BaseModel):
    customer_name: str
    phone_model: str
    color: str
    storage_gb: int
    price: Decimal
    sale_date: date
    store_location: str

class Sale(SaleCreate):
    id: int
    created_at: Optional[datetime ]

    model_config = {
        "from_attributes": True
    }
class SaleStats(BaseModel):
    total_sales: int
    total_revenue: Decimal
    most_popular_model: str
    average_price: Decimal
