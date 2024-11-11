# Use Python 3.9 image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install required packages
RUN pip install -r requirements.txt

# Expose the application port
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
