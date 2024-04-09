FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/
Run pip install  -r requirements.txt

COPY . /app

CMD ["python", "app.py"]