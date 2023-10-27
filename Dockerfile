FROM ubuntu:22.04

WORKDIR /workspace

RUN apt update && apt install -y python3 yosys python3-pip imagemagick netlistsvg
RUN python3 -m pip install requests

COPY . .