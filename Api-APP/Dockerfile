# Stage 1: Builder
# Use a slim Python image for the build stage to install dependencies
FROM python:3.9-slim-buster AS builder

# Set working directory in the container
WORKDIR /app

# Install necessary build tools for Python packages that require compilation
# This includes build-essential for C/C++ compilers and python3-dev for Python header files.
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements.txt first to leverage Docker layer caching.
# This ensures that if only the application code changes, pip install doesn't rerun.
COPY src/requirements.txt ./requirements.txt


# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt

# Copy the rest of the application code
COPY src/ /app/

RUN ls
# Stage 2: Runner
# Use a very minimal image for the final production container
FROM python:3.9-slim-buster AS runner

# Create a non-root user and group for enhanced security
RUN groupadd --system appuser && useradd --system --gid appuser appuser

# Set working directory for the application
WORKDIR /app

# Copy only the installed Python packages from the builder stage
COPY --from=builder /usr/local /usr/local

# Copy the application code into the runner stage
# This ensures only the necessary application files are in the final image.
COPY --from=builder /app/app.py /app/app.py

# Expose the port the application listens on
# This is for documentation and container linking; it doesn't actually publish the port
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PORT=5000  

# Switch to the non-root user
USER appuser

# Command to run the Flask application directly
# Flask's built-in server is used here. For production, Gunicorn is generally preferred,
# but this Dockerfile is designed to run without it as per your initial request.
CMD ["flask", "run"]
