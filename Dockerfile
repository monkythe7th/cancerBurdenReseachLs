# Set base image (host OS)
FROM python:3.9-alpine

# By default, listen to port 5000
EXPOSE 5000/tcp

# working directory
WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python","./app.py"]