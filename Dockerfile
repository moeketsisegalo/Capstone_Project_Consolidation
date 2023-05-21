# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install virtualenv
RUN pip install virtualenv

# Create and activate a virtual environment
RUN virtualenv /env
ENV PATH="/env/bin:$PATH"

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Install Django, Sphinx, and Sphinx RTD Theme
RUN pip install --no-cache-dir Django sphinx sphinx-rtd-theme

# Expose the port that the Django application will run on
EXPOSE 8000

# Define the command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

