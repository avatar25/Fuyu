# backend/app/main.py

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .endpoints import expenses, budgets, categories
from .db import Base  # Import Base from db.py to avoid duplicate Base
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend's URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers for expenses, budgets, and categories
app.include_router(expenses.router, prefix="/api", tags=["Expenses"])
app.include_router(budgets.router, prefix="/api", tags=["Budgets"])
app.include_router(categories.router, prefix="/api", tags=["Categories"])
