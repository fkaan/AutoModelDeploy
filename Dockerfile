# Resmi Python image'ını kullan
FROM python:3.9-slim

# Çalışma dizinini oluştur ve ayarla
WORKDIR /app

# Gereken dosyaları kopyala
COPY requirements.txt /app/

# Gerekli bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını kopyala
COPY . /app/

# Sunucuyu başlatmak için komut
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
