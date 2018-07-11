FROM node:8.10.0-alpine as builder

WORKDIR /usr/src/app

COPY . .

RUN yarn install && \
    yarn build

###

FROM nginx:1.12.2-alpine

COPY --from=builder /usr/src/app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
