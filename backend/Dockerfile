# Backend Dockerfile
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS backend

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Install dependencies with uv
RUN uv sync --frozen

# Expose port
EXPOSE 8000

# Default command (can be overridden by docker-compose)
CMD ["make", "dev"]
