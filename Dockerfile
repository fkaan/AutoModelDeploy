# Use an official Python image as the base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY app/ /app/app
COPY models/ /app/models
COPY requirements.txt /app

# install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# port 
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
