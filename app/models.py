from sqlalchemy import Column, Integer, String, Date, DECIMAL, TIMESTAMP, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from decimal import Decimal
from datetime import datetime
from datetime import date

from app.database import Base  

class IPhoneSale(Base):
    __tablename__ = "iphone_sales"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    customer_name: Mapped[str] = mapped_column(String(100), nullable=False)
    phone_model: Mapped[str] = mapped_column(String(50), nullable=False)
    color: Mapped[str] = mapped_column(String(30), nullable=False)
    storage_gb: Mapped[int] = mapped_column(nullable=False)
    price: Mapped[Decimal] = mapped_column(DECIMAL(10, 2), nullable=False)
    sale_date: Mapped[date] = mapped_column(Date, nullable=False)
    store_location: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())

