FROM ubuntu:bionic
MAINTAINER  RickyChen <809155736@qq.com>

# BLOCK : Make PHP works
RUN apt-get update
RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:ondrej/php
# FIN BLOCK

RUN apt-get -y update && apt-get install -y \
    php7.3 \
    php7.3-fpm \
    php7.3-mysql \
    php7.3-json \
    php7.3-curl \
    php7.3-sqlite3 \
    php7.3-xml \
    php7.3-bcmath \
    php7.3-zip \
    php7.3-mbstring \
    php-xdebug \
    php-ast \
    curl \
    vim \
    iputils-ping \
    php7.3-imap \
    php7.3-gd

# basic config
#RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php/7.2/cli/php.ini
#RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php/7.2/fpm/php.ini
RUN sed -i "s/display_errors = Off/display_errors = On/" /etc/php/7.3/fpm/php.ini
RUN sed -i "s/upload_max_filesize = .*/upload_max_filesize = 10M/" /etc/php/7.3/fpm/php.ini
RUN sed -i "s/post_max_size = .*/post_max_size = 10M/" /etc/php/7.3/fpm/php.ini
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php/7.3/fpm/php.ini

# make it docker findaly and runable by docker-compose
RUN sed -i -e "s/pid =.*/pid = \/var\/run\/php7.3-fpm.pid/" /etc/php/7.3/fpm/php-fpm.conf
RUN sed -i -e "s/error_log =.*/error_log = \/proc\/self\/fd\/2/" /etc/php/7.3/fpm/php-fpm.conf
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.3/fpm/php-fpm.conf
RUN sed -i "s/listen = .*/listen = 9000/" /etc/php/7.3/fpm/pool.d/www.conf
RUN sed -i "s/;catch_workers_output = .*/catch_workers_output = yes/" /etc/php/7.3/fpm/pool.d/www.conf


# install composer
RUN curl https://getcomposer.org/installer > composer-setup.php && php composer-setup.php && mv composer.phar /usr/local/bin/composer && rm composer-setup.php

# global config
RUN composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/

# clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && apt-get autoremove

# volumn
RUN mkdir -p /var/www/html && chown -R www-data:www-data /var/www/html
VOLUME ["/var/www/html"]
WORKDIR /var/www/html

# port
EXPOSE 9000

# entry point
CMD ["php-fpm7.3"]

#ENTRYPOINT ["sh", "-c", "while true;do echo  hello;sleep 10;done"]
