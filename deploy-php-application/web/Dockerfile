FROM centos

LABEL maintainer="NGINX Docker Maintainers <809155736@qq.com>"

RUN yum install -y wget

VOLUME ["/var/www/html"]

ENV PATH /opt/nginx/sbin:$PATH

EXPOSE 80

ENTRYPOINT ["nginx"]

CMD ["-g", "daemon off;"]
#ENTRYPOINT ["sh", "-c", "while true;do echo  hello;sleep 10;done"]
