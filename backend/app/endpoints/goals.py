from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..db import get_db

router = APIRouter()

@router.post("/goals/", response_model=schemas.SavingsGoal)
def create_goal(goal: schemas.SavingsGoalCreate, db: Session = Depends(get_db)):
    return crud.create_savings_goal(db=db, goal=goal)

@router.get("/goals/", response_model=list[schemas.SavingsGoal])
def read_goals(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_savings_goals(db=db, skip=skip, limit=limit)

@router.get("/goals/{goal_id}", response_model=schemas.SavingsGoal)
def read_goal(goal_id: int, db: Session = Depends(get_db)):
    return crud.get_savings_goal(db=db, goal_id=goal_id)

@router.put("/goals/{goal_id}", response_model=schemas.SavingsGoal)
def update_goal(goal_id: int, goal_update: schemas.SavingsGoalCreate, db: Session = Depends(get_db)):
    return crud.update_savings_goal(db=db, goal_id=goal_id, goal_update=goal_update)

@router.delete("/goals/{goal_id}")
def delete_goal(goal_id: int, db: Session = Depends(get_db)):
    return crud.delete_savings_goal(db=db, goal_id=goal_id)
