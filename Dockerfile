FROM ubuntu:latest

MAINTAINER Bui Dinh Ngoc <buidinhngoc.aiti@gmail.com>

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
    apt-get -y clean

COPY . /usr/local/src/BruteforceHTTP

RUN cd /usr/local/src/BruteforceHTTP && \
    pip3 install -r requirements.txt && \
    python3 setup.py install

VOLUME ["/app"]
WORKDIR /app
ENTRYPOINT ["md2pdf"]