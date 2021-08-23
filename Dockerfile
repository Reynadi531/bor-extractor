FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN apt-get update
RUN apt-get install default-jre -y
RUN pip install -r requirements.txt

COPY src/ .

CMD ["python", "main.py"]