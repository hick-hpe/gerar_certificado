# Usa uma imagem base do Python
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Instala dependências do sistema e o wkhtmltopdf
RUN apt-get update && \
    apt-get install -y wkhtmltopdf libxrender1 libfontconfig1 libxext6 && \
    apt-get clean

# Copia requirements e instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante da aplicação
COPY . .

# Expõe a porta usada pelo Flask
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
