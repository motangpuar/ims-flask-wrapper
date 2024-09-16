# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
# COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Run the application with hot reloading
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]
