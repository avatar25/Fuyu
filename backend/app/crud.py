# backend/app/crud.py

from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas
import datetime

# CRUD for Expenses
def create_expense(db: Session, expense: schemas.ExpenseCreate):
    db_expense = models.Expense(**expense.dict())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_expenses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Expense).offset(skip).limit(limit).all()

def get_expense_by_id(db: Session, expense_id: int):
    expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

def update_expense(db: Session, expense_id: int, expense_update: schemas.ExpenseCreate):
    expense = get_expense_by_id(db, expense_id)

    # Save current state to history before updating
    history = models.ExpenseHistory(
        expense_id=expense.id,
        amount=expense.amount,
        category=expense.category,
        description=expense.description,
        date=expense.date,
    )
    db.add(history)

    for key, value in expense_update.dict().items():
        setattr(expense, key, value)

    db.commit()
    db.refresh(expense)
    return expense

def delete_expense(db: Session, expense_id: int):
    expense = get_expense_by_id(db, expense_id)
    db.delete(expense)
    db.commit()
    return {"detail": "Expense deleted successfully"}

def get_expense_history(db: Session, expense_id: int):
    get_expense_by_id(db, expense_id)  # Ensure expense exists
    return (
        db.query(models.ExpenseHistory)
        .filter(models.ExpenseHistory.expense_id == expense_id)
        .order_by(models.ExpenseHistory.changed_at.desc())
        .all()
    )

def generate_recurring_expenses(db: Session, confirm: bool = False):
    """Return upcoming recurring expenses. If confirm is True, create them."""
    next_month = datetime.datetime.utcnow().replace(day=1) + datetime.timedelta(days=32)
    next_month = next_month.replace(day=1)
    recurring = db.query(models.Expense).filter(models.Expense.is_recurring == True).all()

    generated = []
    for exp in recurring:
        new_expense = models.Expense(
            amount=exp.amount,
            category=exp.category,
            description=exp.description,
            date=next_month,
            is_recurring=True,
        )
        generated.append(new_expense)
        if confirm:
            db.add(new_expense)

    if confirm and generated:
        db.commit()
        for e in generated:
            db.refresh(e)
    return generated

# CRUD for Budgets
def create_budget(db: Session, budget: schemas.BudgetCreate):
    db_budget = models.Budget(**budget.dict())
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)
    return db_budget

def get_budgets(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Budget).offset(skip).limit(limit).all()

def get_budget_by_id(db: Session, budget_id: int):
    budget = db.query(models.Budget).filter(models.Budget.id == budget_id).first()
    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")
    return budget

def update_budget(db: Session, budget_id: int, budget_update: schemas.BudgetCreate):
    budget = get_budget_by_id(db, budget_id)
    for key, value in budget_update.dict().items():
        setattr(budget, key, value)
    db.commit()
    db.refresh(budget)
    return budget

def delete_budget(db: Session, budget_id: int):
    budget = get_budget_by_id(db, budget_id)
    db.delete(budget)
    db.commit()
    return {"detail": "Budget deleted successfully"}

# CRUD for Categories
def create_category(db: Session, category: str):
    db_category = models.Budget(category=category, amount=0)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db: Session, category: str):
    category_to_delete = db.query(models.Budget).filter(models.Budget.category == category).first()
    if not category_to_delete:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(category_to_delete)
    db.commit()
    return {"detail": "Category deleted successfully"}

def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Budget).offset(skip).limit(limit).all()

def get_category_by_id(db: Session, category_id: int):
    category = db.query(models.Budget).filter(models.Budget.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

def update_category(db: Session, category_id: int, category_update: str):
    category = get_category_by_id(db, category_id)
    category.category = category_update
    db.commit()
    db.refresh(category)
    return category

# CRUD for Savings Goals
def create_savings_goal(db: Session, goal: schemas.SavingsGoalCreate):
    db_goal = models.SavingsGoal(**goal.dict())
    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)
    return db_goal

def get_savings_goals(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.SavingsGoal).offset(skip).limit(limit).all()

def get_savings_goal(db: Session, goal_id: int):
    goal = db.query(models.SavingsGoal).filter(models.SavingsGoal.id == goal_id).first()
    if not goal:
        raise HTTPException(status_code=404, detail="Savings goal not found")
    return goal

def update_savings_goal(db: Session, goal_id: int, goal_update: schemas.SavingsGoalCreate):
    goal = get_savings_goal(db, goal_id)
    for key, value in goal_update.dict().items():
        setattr(goal, key, value)
    db.commit()
    db.refresh(goal)
    return goal

def delete_savings_goal(db: Session, goal_id: int):
    goal = get_savings_goal(db, goal_id)
    db.delete(goal)
    db.commit()
    return {"detail": "Savings goal deleted successfully"}


def expenses_by_month(db: Session):
    results = (
        db.query(
            models.Expense.date,
            models.Expense.amount,
        )
        .all()
    )
    summary = {}
    for date, amount in results:
        key = date.strftime("%Y-%m")
        summary[key] = summary.get(key, 0) + amount
    return summary


def expenses_by_category(db: Session):
    results = (
        db.query(models.Expense.category, models.Expense.amount).all()
    )
    summary = {}
    for category, amount in results:
        summary[category] = summary.get(category, 0) + amount
    return summary


def expenses_daily(db: Session):
    results = (
        db.query(models.Expense.date, models.Expense.amount).all()
    )
    summary = {}
    for date, amount in results:
        key = date.strftime("%Y-%m-%d")
        summary[key] = summary.get(key, 0) + amount
    return summary
