# Imagen base de Python
FROM python:3.12-slim

# Establece el directorio donde trabajará Docker dentro del contenedor
WORKDIR /app

# Copia las dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia el resto del código fuente
COPY . .

# Expone el puerto que usa FastAPI
EXPOSE 8000

# Comando por defecto al iniciar el contenedor
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
