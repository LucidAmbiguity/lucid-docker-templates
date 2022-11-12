FROM node:16-bullseye

RUN echo 'root:Docker!' | chpasswd
COPY .goodies/.bashrc /home/node/

WORKDIR /project/frontend

COPY src/package*.json ./
RUN chown -R node /project/frontend
USER node
RUN npm install

