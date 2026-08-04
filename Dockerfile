# Base Image
FROM python:3.12-slim

# Working Directory
WORKDIR /app

# Copy Requirements File
COPY requirements.txt .

# Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Project Files
COPY . .

# Run Application
CMD ["python", "main.py"]