# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables
ENV FLASK_APP=boards_listing_tool.main
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5050

# Expose port 5000 for the Flask app
EXPOSE 5050



# Run the Flask app with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5050", "boards_listing_tool.main:app"]