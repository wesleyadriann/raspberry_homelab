FROM nginx:1.21-alpine

RUN \
  echo "UPDATING SYSTEM" && \
  apk update && \
  apk add --update

RUN rm /etc/nginx/conf.d/default.conf

COPY ./conf/archi_steam_farm.conf /etc/nginx/conf.d
COPY ./conf/nginx.conf /etc/nginx

EXPOSE 80

ENTRYPOINT ["nginx", "-g", "daemon off;"]