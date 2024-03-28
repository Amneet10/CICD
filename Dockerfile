# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and other dependencies
RUN pip install Flask

# Expose the port Flask runs on
EXPOSE 5000

# Define the command to run your Flask application
CMD ["python", "app.py"]
