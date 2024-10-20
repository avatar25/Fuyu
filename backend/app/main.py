# backend/app/main.py

from fastapi import FastAPI
from . import models
from .db import engine
from .endpoints import expenses, budgets, categories

app = FastAPI()

# Create tables
models.Base.metadata.create_all(bind=engine)

# Include routers for expenses, budgets, and categories
app.include_router(expenses.router, prefix="/api", tags=["Expenses"])
app.include_router(budgets.router, prefix="/api", tags=["Budgets"])
app.include_router(categories.router, prefix="/api", tags=["Categories"])
