# FROM python:3.10-bullseye
FROM php:8.0-apache-bullseye

# Install MariaDB client
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
  && apt-get install -y mariadb-client  libpq-dev git zip unzip \
  && apt-get clean -y \
  && rm -rf /var/lib/apt/lists/*

# Install php-postgres driver
RUN docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql 

COPY .goodies/install_composer.sh ./

RUN docker-php-ext-install pdo \
  && docker-php-ext-install pdo_mysql \
  && docker-php-ext-install bcmath  \
  && docker-php-ext-install ctype  \
  && docker-php-ext-install fileinfo \
  && /bin/sh install_composer.sh \
  && mv composer.phar /usr/local/bin/composer

RUN echo 'root:Docker!' | chpasswd

RUN useradd -ms /bin/bash backdev

COPY .goodies/.bashrc /home/backdev/
WORKDIR /project/backend

COPY src ./

USER backdev

CMD [ "php","-m" ]
