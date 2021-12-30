FROM node:17.2.0-alpine3.12

EXPOSE 8080

WORKDIR /opt/frontend

ADD . .

RUN npm install -g @quasar/cli && npm install

ENTRYPOINT ["quasar", "dev"]