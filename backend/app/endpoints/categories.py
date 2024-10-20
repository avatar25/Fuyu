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
