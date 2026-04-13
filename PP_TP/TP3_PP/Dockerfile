FROM python:3.12-slim

WORKDIR /app

# RUN pip install flask
RUN pip install flask mysql-connector-python

COPY . /app/

EXPOSE 5000

CMD ["python", "app.py"]

# lignes de commandes : `docker build -t mon-app .` suivi de : `docker run -p 4900:5000 mon-app`