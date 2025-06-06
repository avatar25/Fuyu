# backend/app/models.py


from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .db import Base
import datetime

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    is_recurring = Column(Boolean, default=False)

    histories = relationship("ExpenseHistory", back_populates="expense", cascade="all, delete-orphan")

class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, unique=True, nullable=False)
    amount = Column(Float, nullable=False)
    rollover_enabled = Column(Boolean, default=False)

    categories = relationship("Category", back_populates="budget")

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    budget_id = Column(Integer, ForeignKey("budgets.id"))

    budget = relationship("Budget", back_populates="categories")


class ExpenseHistory(Base):
    __tablename__ = "expense_histories"

    id = Column(Integer, primary_key=True, index=True)
    expense_id = Column(Integer, ForeignKey("expenses.id"), nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=True)
    date = Column(DateTime, nullable=False)
    changed_at = Column(DateTime, default=datetime.datetime.utcnow)

    expense = relationship("Expense", back_populates="histories")


class SavingsGoal(Base):
    __tablename__ = "savings_goals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    target_amount = Column(Float, nullable=False)
    saved_amount = Column(Float, default=0)
    target_date = Column(DateTime, nullable=False)
