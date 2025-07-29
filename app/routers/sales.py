from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import schemas, crud
from typing import Optional

router = APIRouter(prefix="/sales", tags=["Sales"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.SaleCreate)
def create(sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    return crud.create_sale(db, sale)

@router.get("/", response_model=list[schemas.Sale])
def read_all(phone_model: Optional[str] = None, db: Session = Depends(get_db)):
    return crud.get_sales(db, phone_model)

@router.get("/stats", response_model=schemas.SaleStats)
def stats(db: Session = Depends(get_db)):
    return crud.get_sales_stats(db)

@router.get("/{sale_id}", response_model=schemas.Sale)
def read_one(sale_id: int, db: Session = Depends(get_db)):
    sale = crud.get_sale_by_id(db, sale_id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale

@router.put("/{sale_id}", response_model=schemas.Sale)
def update(sale_id: int, sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    updated = crud.update_sale(db, sale_id, sale)
    if not updated:
        raise HTTPException(status_code=404, detail="Sale not found")
    return updated

@router.delete("/{sale_id}")
def delete(sale_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_sale(db, sale_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Sale not found")
    return {"message": "Sale deleted successfully"}

