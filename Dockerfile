# استفاده از نسخه مورد نظر شما
FROM python:3.14-slim

# جلوگیری از تولید فایل‌های .pyc و فعال کردن buffering برای لاگ‌ها
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# تعیین دایرکتوری کاری
WORKDIR /code

# نصب وابستگی‌های سیستم برای PostgreSQL (مهم برای کتابخانه psycopg2)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# نصب وابستگی‌های پایتون
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن پروژه
COPY . /code/
