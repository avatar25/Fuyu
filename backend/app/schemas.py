# backend/app/schemas.py

from pydantic import BaseModel, Field, constr
from typing import Optional
import datetime

class ExpenseCreate(BaseModel):
    amount: float = Field(..., gt=0, description="Amount must be greater than zero")
    category: constr(strip_whitespace=True, min_length=1) = Field(..., description="Category cannot be empty")
    description: Optional[str] = Field(None, max_length=255)

class Expense(BaseModel):
    id: int
    amount: float
    category: str
    description: Optional[str] = None
    date: datetime.datetime

    class Config:
        from_attributes = True

class BudgetCreate(BaseModel):
    category: constr(strip_whitespace=True, min_length=1) = Field(..., description="Category name must be provided")
    amount: float = Field(..., gt=0, description="Budget amount must be greater than zero")

class Budget(BaseModel):
    id: int
    category: str
    amount: float

    class Config:
        from_attributes = True
