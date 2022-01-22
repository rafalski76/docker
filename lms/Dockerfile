FROM debian:10-slim as builder

ENV DEBIAN_FRONTEND noninteractive
ENV LANG en_US.UTF-8

RUN apt-get update && apt-get install -y \
    apache2 \
    curl \
    composer \
    gettext-base \
    locales \
    php7.3 \
    php7.3-bcmath \
    php7.3-gd \
    php7.3-gmp \
    php7.3-soap \
    php7.3-xml \
    php7.3-zip \
    php-mysql \
    wget \
	&& apt-get -s clean && apt-get autoremove 
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && update-locale LANG=en_US.UTF-8

WORKDIR /usr/share/lms

RUN chown -R www-data:www-data /usr/share/lms /var/www

USER www-data

RUN APP_VERSION=`curl --silent "https://api.github.com/repositories/3524851/releases/latest" | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/'` \
    && wget -qO- https://github.com/chilek/lms/archive/refs/tags/${APP_VERSION}.tar.gz | tar -zx -f - -C /usr/share/lms --strip-components=1
RUN composer install

USER root

RUN sed -i 's_DocumentRoot /var/www/html_DocumentRoot /usr/share/lms_' /etc/apache2/sites-available/000-default.conf \
    && mkdir /usr/share/lms/js/xajax_js/deferred \
    && chown -R 33:33 /usr/share/lms/js/xajax_js/deferred \
    && chmod -R 755 /usr/share/lms/js/xajax_js/deferred

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]