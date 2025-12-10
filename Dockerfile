# Use a slim Python image as a base
FROM python:3.12-slim-bookworm AS builder

# Set the working directory
WORKDIR /app

# Install uv
RUN pip install uv

# Copy the dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv pip install --system --no-cache .

# Use a slim Python image for the final image
FROM python:3.12-slim-bookworm

# Set the working directory
WORKDIR /app

# Copy the installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy the application code
COPY src/ /app/src

# Create a non-root user
RUN useradd -m myuser
USER myuser

# Expose the port the app runs on
EXPOSE 8000

# Set the command to run the application
CMD ["uvicorn", "src.ethicslab.main:app", "--host", "0.0.0.0", "--port", "8000"]