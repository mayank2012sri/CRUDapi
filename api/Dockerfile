# Use the official Python image from Docker Hub as the base image
FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 9433


CMD ["python", "app.py"]
