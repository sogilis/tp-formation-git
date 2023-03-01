FROM debian:bullseye-slim
RUN apt update -y && \
    apt install -y python3 && \
    ln /usr/bin/python3 /usr/bin/py && \
    apt install -y git && \
    apt install -y vim
RUN adduser gituser
WORKDIR /home/gituser
USER gituser
ENV EDITOR=vim
