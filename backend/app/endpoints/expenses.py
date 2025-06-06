# backend/app/endpoints/expenses.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..db import get_db

router = APIRouter()

@router.post("/expenses/", response_model=schemas.Expense)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db=db, expense=expense)

@router.get("/expenses/", response_model=list[schemas.Expense])
def read_expenses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_expenses(db=db, skip=skip, limit=limit)

@router.get("/expenses/{expense_id}", response_model=schemas.Expense)
def read_expense(expense_id: int, db: Session = Depends(get_db)):
    return crud.get_expense_by_id(db=db, expense_id=expense_id)

@router.put("/expenses/{expense_id}", response_model=schemas.Expense)
def update_expense(expense_id: int, expense_update: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return crud.update_expense(db=db, expense_id=expense_id, expense_update=expense_update)

@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    return crud.delete_expense(db=db, expense_id=expense_id)


@router.get("/expenses/{expense_id}/history", response_model=list[schemas.ExpenseHistory])
def read_expense_history(expense_id: int, db: Session = Depends(get_db)):
    return crud.get_expense_history(db=db, expense_id=expense_id)


@router.post("/expenses/generate_recurring", response_model=list[schemas.Expense])
def generate_recurring(confirm: bool = False, db: Session = Depends(get_db)):
    return crud.generate_recurring_expenses(db=db, confirm=confirm)

