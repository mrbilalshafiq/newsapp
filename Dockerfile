# Use the official Python image as the base for our image
FROM python:3.8-slim

# Set the working directory for the application
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code and data into the container
COPY app.py templates/ ./

# Set the default command to run when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]

