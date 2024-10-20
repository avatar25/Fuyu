# Unit Tests for CRUD Operations in Fuyu App
# Using `pytest` to test the CRUD functionality for the backend

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.app.db import Base, get_db
from backend.app.models import Expense, Budget
from backend.app.crud import create_expense, get_expenses, create_budget, get_budgets
from backend.app.schemas import ExpenseCreate, BudgetCreate

# Create an in-memory SQLite database for testing purposes
test_engine = create_engine("sqlite:///:memory:")
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

# Setting up and tearing down the test database
@pytest.fixture(scope="module")
def test_db():
    # Create all tables in the in-memory test database
    Base.metadata.create_all(bind=test_engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        # Drop all tables after the test session ends
        Base.metadata.drop_all(bind=test_engine)

# Test for creating and retrieving expenses
def test_create_and_get_expenses(test_db):
    # Arrange: Create an expense object
    expense_data = ExpenseCreate(amount=150.0, category="Utilities", description="Electricity bill")
    
    # Act: Add the expense to the database
    created_expense = create_expense(test_db, expense_data)
    
    # Assert: Check if the expense has been added correctly
    assert created_expense.id is not None
    assert created_expense.amount == 150.0
    assert created_expense.category == "Utilities"
    
    # Act: Retrieve all expenses from the database
    expenses = get_expenses(test_db)
    
    # Assert: Check if the retrieved expenses match what was added
    assert len(expenses) == 1
    assert expenses[0].category == "Utilities"
    assert expenses[0].amount == 150.0

# Test for creating and retrieving budgets
def test_create_and_get_budgets(test_db):
    # Arrange: Create a budget object
    budget_data = BudgetCreate(category="Groceries", amount=500.0)
    
    # Act: Add the budget to the database
    created_budget = create_budget(test_db, budget_data)
    
    # Assert: Check if the budget has been added correctly
    assert created_budget.id is not None
    assert created_budget.category == "Groceries"
    assert created_budget.amount == 500.0
    
    # Act: Retrieve all budgets from the database
    budgets = get_budgets(test_db)
    
    # Assert: Check if the retrieved budgets match what was added
    assert len(budgets) == 1
    assert budgets[0].category == "Groceries"
    assert budgets[0].amount == 500.0

if __name__ == "__main__":
    pytest.main()
