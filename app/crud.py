from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from app import models, schemas
from typing import Optional

def create_sale(db: Session, sale:schemas.SaleCreate):
    db_sale = models.IPhoneSale(**sale.dict())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

def get_sales(db: Session, phone_model: Optional[str] = None):
    if phone_model:
        return db.query(models.IPhoneSale).filter(models.IPhoneSale.phone_model == phone_model).all()
    return db.query(models.IPhoneSale).all()

def get_sale_by_id(db: Session, sale_id: int):
    return db.query(models.IPhoneSale).filter(models.IPhoneSale.id == sale_id).first()

def update_sale(db: Session, sale_id: int, sale_data: schemas.SaleCreate):
    sale = get_sale_by_id(db, sale_id)
    if not sale:
        return None
    for key, value in sale_data.dict().items():
        setattr(sale, key, value)
    db.commit()
    db.refresh(sale)
    return sale

def delete_sale(db: Session, sale_id: int):
    sale = get_sale_by_id(db, sale_id)
    if not sale:
        return None
    db.delete(sale)
    db.commit()
    return True

def get_sales_stats(db: Session):
    total_sales = db.query(func.count(models.IPhoneSale.id)).scalar()
    total_revenue = db.query(func.sum(models.IPhoneSale.price)).scalar() or 0
    most_popular_model = db.query(models.IPhoneSale.phone_model, func.count().label('cnt'))\
        .group_by(models.IPhoneSale.phone_model).order_by(desc('cnt')).first()
    average_price = db.query(func.avg(models.IPhoneSale.price)).scalar() or 0
    return schemas.SaleStats(
        total_sales=total_sales,
        total_revenue=float(total_revenue),
        most_popular_model=most_popular_model[0] if most_popular_model else "",
        average_price=float(average_price)
    )
