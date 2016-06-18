FROM python:3.5-alpine
RUN pip3 install 'connexion>=1.0,<1.0.99999'
COPY . /app
WORKDIR /app
CMD ["python", "app.py"]
