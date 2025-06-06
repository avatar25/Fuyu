# backend/app/schemas.py

from pydantic import BaseModel, Field, constr
from typing import Optional
import datetime

class ExpenseCreate(BaseModel):
    amount: float = Field(..., gt=0, description="Amount must be greater than zero")
    category: constr(strip_whitespace=True, min_length=1) = Field(..., description="Category cannot be empty")
    description: Optional[str] = Field(None, max_length=255)
    is_recurring: bool = False

class Expense(BaseModel):
    id: int
    amount: float
    category: str
    description: Optional[str] = None
    date: datetime.datetime
    is_recurring: bool

    class Config:
        from_attributes = True

class BudgetCreate(BaseModel):
    category: constr(strip_whitespace=True, min_length=1) = Field(..., description="Category name must be provided")
    amount: float = Field(..., gt=0, description="Budget amount must be greater than zero")
    rollover_enabled: bool = False

class Budget(BaseModel):
    id: int
    category: str
    amount: float
    rollover_enabled: bool

    class Config:
        from_attributes = True


class ExpenseHistory(BaseModel):
    id: int
    expense_id: int
    amount: float
    category: str
    description: Optional[str] = None
    date: datetime.datetime
    changed_at: datetime.datetime

    class Config:
        from_attributes = True
