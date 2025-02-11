# Utiliser l'image de base officielle de Python
FROM python:3.12-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances Flask
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code dans le conteneur
COPY . .

# Spécifier le port sur lequel l'application Flask écoute
EXPOSE 5000

# Exécuter l'application Flask
CMD ["python", "app.py"]
