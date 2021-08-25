FROM node:14-alpine

WORKDIR /app

COPY . .

RUN npm install --silent
RUN npm run build

EXPOSE 4200

CMD [ "npm", "run", "server" ]