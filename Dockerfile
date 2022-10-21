FROM ubuntu:latest
WORKDIR /app
COPY api.py .
COPY requirements.txt .
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3 -y
RUN apt-get install pip -y
RUN pip install -r requirements.txt
#ENTRYPOINT /bin/bash



