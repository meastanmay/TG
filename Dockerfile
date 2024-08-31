# Use the official Python base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app.py file to the container
COPY app.py .

# Copy the static files to the container
COPY Template static

# Expose the port that the Flask app will run on
EXPOSE 5000

# Start the Flask app when the container starts
CMD ["python", "app.py"]