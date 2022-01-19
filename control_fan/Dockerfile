FROM woahbase/alpine-rpigpio:aarch64

COPY ./requirements.txt /requirements.txt

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

WORKDIR /app

COPY ./main.py .

ENTRYPOINT python main.py