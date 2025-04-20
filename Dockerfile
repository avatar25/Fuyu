FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Copy requirements (if you have requirements.txt)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY backend/app ./app

# Expose port
EXPOSE 8000

# Set environment variables (optional)
ENV PYTHONUNBUFFERED=1

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
