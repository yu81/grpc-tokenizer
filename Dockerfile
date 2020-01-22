FROM ubuntu:bionic

COPY requirements.txt /tmp/

RUN apt-get update && \
    apt-get install software-properties-common -y

RUN add-apt-repository ppa:deadsnakes/ppa -y && \
    apt-get update && \
    apt-get remove python3 python3-pip -y && \
    apt-get install python3.7 python3.7-dev git wget curl mecab libmecab-dev file sudo apt-utils build-essential -y && \
    apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* && \
    git clone https://github.com/neologd/mecab-ipadic-neologd.git && \
    mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -a -n -y && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python3.7 get-pip.py && \
    pip3.7 install pip -U && \
    pip3.7 install -r /tmp/requirements.txt --no-cache-dir \
    rm -f /tmp/requirements.txt

COPY src/app/* /opt/

RUN mkdir /opt/static

WORKDIR /opt

ENTRYPOINT ["python3.7", "server_grpc.py"]
