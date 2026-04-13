
FROM python:3.12-slim

WORKDIR /app

RUN pip install flask

COPY . /app/

# On expose le port du serveur_student.py
EXPOSE 5000

CMD ["python", "serveur_student.py"]

# lignes de commandes : `docker build -t mon-app-tp2 .` suivi de : `docker run -p 4900:5000 mon-app-tp2`

# Une fois que les logs du serveur apparaissent, pour vérifier que l'API fonctionne : `http://localhost:4900`.