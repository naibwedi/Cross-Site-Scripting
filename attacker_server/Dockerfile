# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /attacker_server

# Copy requirements file into the container
COPY requirements.txt /attacker_server/

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . /attacker_server/

# Command to run the attacker server
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
