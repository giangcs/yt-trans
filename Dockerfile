# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install dependencies (if requirements.txt exists)
RUN pip install --no-cache-dir youtube-transcript-api

# Command to run the Python app
CMD ["python", "app.py"]