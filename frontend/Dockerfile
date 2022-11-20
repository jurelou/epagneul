FROM node:17.2.0-alpine3.12

EXPOSE 8080

WORKDIR /opt/frontend

ADD . .

RUN npm install -g @quasar/cli && \
    npm install && \
    chmod +x entrypoint.sh && \
    quasar build

ENTRYPOINT ["quasar", "dev"]