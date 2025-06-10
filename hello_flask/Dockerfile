FROM python:3.8-slim

WORKDIR /app

COPY . .

# ✅ Install system-level dependencies needed by mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && pip install Flask mysqlclient

EXPOSE 5000

CMD ["python", "app.py"]
