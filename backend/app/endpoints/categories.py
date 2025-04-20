# backend/app/endpoints/categories.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud
from ..db import get_db

router = APIRouter()

@router.post("/categories/")
def create_category(category: str, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)

@router.delete("/categories/{category}")
def delete_category(category: str, db: Session = Depends(get_db)):
    return crud.delete_category(db=db, category=category)

@router.get("/categories/", response_model=list)
def get_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db=db)

@router.get("/categories/{category_id}")
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    return crud.get_category_by_id(db=db, category_id=category_id)

@router.put("/categories/{category_id}")
def update_category(category_id: int, category_update: str, db: Session = Depends(get_db)):
    return crud.update_category(db=db, category_id=category_id, category_update=category_update)