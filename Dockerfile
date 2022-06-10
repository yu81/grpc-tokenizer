FROM python:3.9.13-bullseye

ENV CC clang
ENV CXX clang++

COPY requirements.txt /tmp/

RUN apt-get update && \
    apt-get install software-properties-common -y

RUN apt-get update && \
    apt-get install clang git wget curl mecab libmecab-dev file sudo apt-utils build-essential swig -y && \
    apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* && \
    git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git && \
    mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -a -n -y && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    pip install pip -U && \
    pip install -r /tmp/requirements.txt --no-cache-dir \
    rm -f /tmp/requirements.txt

COPY src/app/* /opt/

RUN mkdir /opt/static

WORKDIR /opt

ENTRYPOINT ["python", "server_grpc.py"]
