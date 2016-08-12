FROM python:2.7.12-alpine

MAINTAINER Mateusz Moneta <mateuszmoneta@gmail.com>

RUN apk --no-cache add \
        linux-headers \
        build-base \
    && pip install diamond==4.0.451 statsd==3.2.1 \
    && apk del \
        build-base \
        linux-headers \
    && rm -rf /var/cache/apk/*

ENV HANDLERS=diamond.handler.stats_d.StatsdHandler \
    GRAPHITE_HOST=127.0.0.1 \
    GRAPHITE_PORT=2003 \
    STATSD_HOST=127.0.0.1 \
    STATSD_PORT=8125 \
    INTERVAL=10 \
    DIAMOND_CONF=/etc/diamond/diamond.conf

COPY diamond.conf $DIAMOND_CONF
COPY entrypoint.py /entrypoint.py

RUN adduser -S diamond \
    && mkdir -p \
        /usr/local/share/diamond/collectors \
        /usr/local/share/diamond/handlers \
        /etc/diamond/collectors \
        /etc/diamond/handlers \
    && chown -R diamond /usr/local/share/diamond /etc/diamond


USER diamond
ENTRYPOINT ["/entrypoint.py"]
