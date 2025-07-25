# Unit Tests for CRUD Operations in Fuyu App
# Using `pytest` to test the CRUD functionality for the backend

import os
import pytest
from sqlalchemy import create_engine
import datetime
from sqlalchemy.orm import sessionmaker

os.environ["DATABASE_URL"] = "sqlite:///:memory:"
from backend.app.db import Base, get_db
from backend.app.models import Expense, Budget, ExpenseHistory, SavingsGoal
from backend.app.crud import (
    create_expense,
    get_expenses,
    create_budget,
    get_budgets,
    update_expense,
    get_expense_history,
    generate_recurring_expenses,
    create_savings_goal,
    get_savings_goals,
)
from backend.app.schemas import ExpenseCreate, BudgetCreate, SavingsGoalCreate

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

    # Update the expense and verify history is created
    update_data = ExpenseCreate(amount=200.0, category="Utilities", description="Electricity bill updated", is_recurring=False)
    updated = update_expense(test_db, created_expense.id, update_data)
    history = get_expense_history(test_db, created_expense.id)
    assert updated.amount == 200.0
    assert len(history) == 1
    assert history[0].amount == 150.0

# Test for creating and retrieving budgets
def test_create_and_get_budgets(test_db):
    # Arrange: Create a budget object
    budget_data = BudgetCreate(category="Groceries", amount=500.0, rollover_enabled=True)
    
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
    assert budgets[0].rollover_enabled is True

def test_generate_recurring_expenses(test_db):
    expense = ExpenseCreate(amount=50.0, category="Subscription", description="Music", is_recurring=True)
    created = create_expense(test_db, expense)
    generated = generate_recurring_expenses(test_db, confirm=True)
    assert len(generated) == 1
    assert generated[0].id is not None


def test_create_savings_goal(test_db):
    goal_data = SavingsGoalCreate(name="Trip", target_amount=1000.0, saved_amount=200.0, target_date=datetime.datetime.utcnow())
    goal = create_savings_goal(test_db, goal_data)
    goals = get_savings_goals(test_db)
    assert goal.id is not None
    assert len(goals) == 1

if __name__ == "__main__":
    pytest.main()
