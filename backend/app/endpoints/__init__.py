from fastapi import APIRouter
from . import expenses, budgets, categories, goals


api_router = APIRouter()
api_router.include_router(expenses.router)
api_router.include_router(budgets.router)
api_router.include_router(categories.router)
api_router.include_router(goals.router)
