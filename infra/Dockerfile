FROM python:3.10-slim-bullseye as builder

#RUN apt-get update -qq
#RUN apt-get install python3.10 python3-pip -y --no-install-recommends && rm -rf /var/lib/apt/lists_/*
RUN apt-get update --fix-missing && apt-get install -y --fix-missing build-essential

RUN pip install func-ai

COPY ./infinite_fn /app/infinite_fn
WORKDIR /appp

EXPOSE 9002

CMD ["python3", "/app/infinite_fn/main.py"]