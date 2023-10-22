FROM continuumio/anaconda3:2021.11

ADD . /code

WORKDIR /code

ENTRYPOINT ["python", "birthday/main.py"]


