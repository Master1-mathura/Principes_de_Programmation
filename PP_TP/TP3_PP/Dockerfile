FROM python:3.12-slim

WORKDIR /app

# RUN pip install flask
RUN pip install flask mysql-connector-python

COPY . /app/

EXPOSE 5001

CMD ["python", "app.py"]