# Fuyu
Personal wealth tracker

## Overview

Fuyu is a personal wealth tracking application that helps you monitor your financial assets, track expenses, and visualize your financial growth over time.

### Core Features
- **Recurring Expenses**: mark transactions as recurring and auto-generate them each month with confirmation.
- **Budget Rollover**: optionally carry forward unused budget amounts per category.
- **Edit History**: every change to an expense is stored, allowing you to view previous versions.

## Prerequisites

- Python 3.9+
- Node.js 16+ and npm
- PostgreSQL (optional, if using a local database)

## Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Start postgres service
    ```bash
    brew services start postgresql@14
    ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   Edit the `.env` file with your database credentials and other configuration.

5. Run database migrations:
   ```bash
   alembic upgrade head
   ```

## Running the Backend

Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000
API documentation is available at http://localhost:8000/docs

## Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   Edit the `.env` file with your API endpoint and other configuration.

## Running the Frontend

Start the development server:
```bash
npm run dev
```

The application will be available at http://localhost:3000

## Running with Docker (Optional)

If you prefer using Docker:

1. Copy environment variable files for both backend and frontend:
   ```bash
   cp backend/.env.example backend/.env
   cp frontend/.env.example frontend/.env
   ```
   Edit the `.env` files as needed for your configuration.

2. Build and start the containers:
   ```bash
   docker compose up --build -d
   ```

3. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API documentation: http://localhost:8000/docs

4. To stop the containers:
   ```bash
   docker compose down
   ```

## Development

- Backend API tests: `cd backend && pytest`
- Frontend tests: `cd frontend && npm test`
