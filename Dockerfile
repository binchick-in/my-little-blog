FROM ubuntu:18.04
RUN apt-get update && apt-get install -y \
    dumb-init \
    build-essential \
    git \
    vim \
    lsof \
    python3.7 \
    python3.7-dev \
    python3-pip && \
    apt-get clean

RUN mkdir /database
ADD requirements.txt /code/
RUN /usr/bin/python3.7 -m pip install -r /code/requirements.txt
ADD . /code
WORKDIR /code
RUN chown -R nobody /database
USER nobody
EXPOSE 8888
ENTRYPOINT ["/usr/local/bin/uwsgi", "--ini", "/code/uwsgi.ini"]
