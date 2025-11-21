# Use official slim Python 3.11 image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only the files needed for installing dependencies
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Ensure Python outputs are unbuffered
ENV PYTHONUNBUFFERED=1

# Run the Flask app
CMD ["python", "src/app.py"]

# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "src/app.py"]
