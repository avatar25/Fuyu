# backend/app/endpoints/budgets.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..db import get_db

router = APIRouter()

@router.post("/budgets/", response_model=schemas.Budget)
def create_budget(budget: schemas.BudgetCreate, db: Session = Depends(get_db)):
    return crud.create_budget(db=db, budget=budget)

@router.get("/budgets/", response_model=list[schemas.Budget])
def read_budgets(db: Session = Depends(get_db)):
    return crud.get_budgets(db=db)

@router.get("/budgets/{budget_id}", response_model=schemas.Budget)
def read_budget(budget_id: int, db: Session = Depends(get_db)):
    return crud.get_budget_by_id(db=db, budget_id=budget_id)

@router.put("/budgets/{budget_id}", response_model=schemas.Budget)
def update_budget(budget_id: int, budget_update: schemas.BudgetCreate, db: Session = Depends(get_db)):
    return crud.update_budget(db=db, budget_id=budget_id, budget_update=budget_update)

@router.delete("/budgets/{budget_id}")
def delete_budget(budget_id: int, db: Session = Depends(get_db)):
    return crud.delete_budget(db=db, budget_id=budget_id)
