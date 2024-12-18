# Usar uma imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos de requisitos e instalar as dependências
COPY backend/requirements.txt .
RUN pip install -r requirements.txt

# Copiar o restante do código
COPY backend/ .

# Expor a porta que o Flask usará
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]