FROM ubuntu:14.04

# Install.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y byobu curl git man unzip vim wget && \
  apt-get -y install python3-pip && \
  apt-get update && \
  python3 -m pip install gunicorn && \
  rm -rf /var/lib/apt/lists/*

RUN mkdir /workspace && mkdir /workspace/data
COPY src/* /workspace/
COPY data/* /workspace/data/

ENV HOME /root
WORKDIR /workspace

CMD ["gunicorn" "-w" "4" "main:app"]
