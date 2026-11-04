FROM debian:13-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=en_US.UTF-8

RUN apt-get update && apt-get install -y --no-install-recommends \
    apache2 \
    ca-certificates \
    composer \
    curl \
    gettext-base \
    git \
    libapache2-mod-php \
    locales \
    php \
    php-bcmath \
    php-cli \
    php-curl \
    php-gd \
    php-gmp \
    php-intl \
    php-mbstring \
    php-mysql \
    php-soap \
    php-xml \
    php-zip \
    unzip \
    wget \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && update-locale LANG=en_US.UTF-8

WORKDIR /usr/share/lms

RUN chown -R www-data:www-data /usr/share/lms /var/www

USER www-data

RUN APP_VERSION=`curl --silent "https://api.github.com/repositories/3524851/releases/latest" | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/'` \
    && wget -qO- https://github.com/chilek/lms/archive/refs/tags/${APP_VERSION}.tar.gz | tar -zx -f - -C /usr/share/lms --strip-components=1
# Composer 2.2+ blokuje wtyczki bez jawnej zgody; LMS wymaga tych dwóch
RUN composer config --no-plugins allow-plugins.composer/installers true \
    && composer config --no-plugins allow-plugins.oomphinc/composer-installers-extender true \
    && composer install --no-dev --no-interaction

USER root

RUN sed -i 's_DocumentRoot /var/www/html_DocumentRoot /usr/share/lms_' /etc/apache2/sites-available/000-default.conf \
    && mkdir /usr/share/lms/js/xajax_js/deferred \
    && chown -R 33:33 /usr/share/lms/js/xajax_js/deferred \
    && chmod -R 755 /usr/share/lms/js/xajax_js/deferred

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
