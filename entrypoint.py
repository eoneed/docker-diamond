#!/usr/bin/env python

import logging
from glob import glob
from os import environ, path
from subprocess import call
from sys import argv

logging.basicConfig(level=logging.INFO)


def format_with_environment(path):
    """
    Open file and format its content with environment variables.
    :param path: path to file which should be formatted
    """
    with open(path, 'r') as f:
        content = f.read()
        new_content = content.format(**environ)

    if content != new_content:
        with open(path, 'w+') as f:
            f.write(new_content)

configs = [environ['DIAMOND_CONF']]

for configs_dir in [environ['COLLECTORS_CONF_DIR'],
                    environ['HANDLERS_CONF_DIR']]:
    configs += glob(path.join(configs_dir, '*.conf'))


logging.info('Formatting %s with environments', ', '.join(configs))

for config in configs:
    format_with_environment(config)

exit(call(['diamond', '-f', '--skip-pidfile', '-c', environ['DIAMOND_CONF']] +
          argv[1:]))
