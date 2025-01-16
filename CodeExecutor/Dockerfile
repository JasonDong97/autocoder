# Base image: python:3.10-slim
FROM python:3.10-slim

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Mount host code directory
WORKDIR /usr/src/app
RUN mkdir -p host_code

# Copy app code
COPY app/ ./app/

# Expose FastAPI port
EXPOSE 1234

# Run FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "1234"]