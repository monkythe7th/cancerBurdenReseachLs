# Set base image (host OS)
FROM python:3.10-alpine

# working directory
WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# By default, listen to port 5000
EXPOSE 5000/tcp

CMD ["flask","run","--debug","-h","0.0.0.0"]