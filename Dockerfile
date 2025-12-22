# Hungry-Hippo Production Container
# Emergency Modernism - Monaco Electric Construction Services

FROM node:20-slim AS tailwind-builder

WORKDIR /build

# Copy Tailwind configuration and source
COPY package.json package-lock.json* tailwind.config.js ./
COPY app/static/css/input.css ./app/static/css/
COPY app/templates ./app/templates

# Install dependencies and build CSS
RUN npm install && npm run build

# Python production image
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy Python requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

# Copy built Tailwind CSS from builder
COPY --from=tailwind-builder /build/app/static/css/output.css ./app/static/css/

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
