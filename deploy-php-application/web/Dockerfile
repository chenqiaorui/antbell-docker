FROM nginx:stable

LABEL maintainer="NGINX Docker Maintainers <809155736@qq.com>"

#RUN apt-get update -y && apt-get install -y \
#        vim \
#        inetutils-ping \ 
#        procps \
#        iproute2 \
#        iftop \
#        net-tools

ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# modify group name
RUN groupmod -n nobody nogroup
COPY ./nginx.conf /etc/nginx/nginx.conf
RUN sed -i "s/user  www-data/user  nobody/" /etc/nginx/nginx.conf

# Define mountable directories.
#VOLUME ["/etc/nginx/conf.d", "/var/log/nginx", "/var/www/html"]

# Define working directory.
WORKDIR /etc/nginx/conf.d

EXPOSE 80

ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]
