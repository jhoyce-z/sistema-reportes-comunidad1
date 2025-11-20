FROM python:3.10-slim

WORKDIR /app

# Instalar dependencias del sistema (para mysqlclient)
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código
COPY . .

# Exponer puerto
EXPOSE 8000

# Comando para ejecutar
CMD ["python", "backend/manage.py", "runserver", "0.0.0.0:8000"]