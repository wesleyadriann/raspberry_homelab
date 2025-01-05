FROM ubuntu

RUN apt-get update && \ 
    apt-get install -y libsystemd-dev python3 python3-dev python3-pip

COPY ./requirements.txt /requirements.txt

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

WORKDIR /app

COPY ./main.py .

ENTRYPOINT python main.py