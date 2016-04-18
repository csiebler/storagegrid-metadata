FROM ubuntu:14.04

RUN apt-get update && apt-get install -y \
    python \
    python-pip

RUN pip install boto3
RUN pip install elasticsearch
RUN pip install tailer
RUN pip install requests --upgrade

RUN mkdir /indexer
COPY indexer.py /indexer/
