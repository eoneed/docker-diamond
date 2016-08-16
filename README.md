# docker-diamond

Minimal image based on `python:2.7.12-alpine` with Diamond daemon running.
It is designed to collect metric from other containers over network.

## Base usage ##
```
docker run --rm -e STATSD_HOST=some.statsd.net mateuszm/docker
```

## Configuration ##
Base config is done via environment variables:

```
HANDLERS               Diamond handlers to use, defaults to diamond.handler.stats_d.StatsdHandler.
GRAPHITE_HOST          address of your graphite instance, defaults to 127.0.0.1.
GRAPHITE_PORT          port on which your graphite listens on, default to 2003.
STATSD_HOST            address of your StatsD daemon, defaults to 127.0.0.1.
STATSD_PORT            port on which StatsD listens on, default to 8125.
INTERVAL               the interval at which you wish to send metrics, defaults to 10.
PATH_PREFIX            prefix to all metrics processed by Diamond, defaults to ''
DIAMOND_CONF           path to diamond config, defaults to /etc/diamond/diamond.conf.
COLLECTORS_CONF_DIR    path to diamond collectors config dir, defaults to /etc/diamond/collectors.
COLLECTORS_DIR         path to additional diamond collectors, defaults to /use/local/share/diamond/collectors.
HANDLERS_CONF_DIR      path to diamond handlers config dir, defaults to /etc/diamond/handlers.
HANDLERS_DIR         path to additional diamond handlers, defaults to /use/local/share/diamond/handlers.
```

For more sophisticated cases you can copy your own diamond config:
```
COPY diamond.conf $DIAMOND_CONF
```

Config files (`diamond.conf` and everything in `$COLLECTORS_CONF_DIR`
and `HANDLERS_CONF_DIR`) is formated by image's entrypoint 
with environment as keys, so you can dynamically change it's contents by
using environment variables in braces, e.g:
```
[server]

# Handlers for published metrics.
handlers = {HANDLERS}
```


For enabling collectors just copy their configuration files:
```
COPY CPUCollector.conf $COLLECTORS_CONF_DIR
```

Same applies to additional collectors/handlers as `.py` files.
```
COPY <myrabbitcollector>.py $COLLECTORS_DIR/rabbitmq/
COPY fancy.py $COLLECTORS_DIR/fancy/
```
