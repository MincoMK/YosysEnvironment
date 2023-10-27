FROM node:19

WORKDIR /workspace

RUN apt update && apt install -y python3 yosys python3-pip imagemagick gsfonts
RUN python3 -m pip install requests
RUN npm i -g netlistsvg

COPY . .