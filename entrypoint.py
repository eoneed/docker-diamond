#!/usr/bin/env python

from os import environ
from subprocess import call
from sys import argv

with open(environ['DIAMOND_CONF'], 'r+') as f:
    content = f.read()
    content = content.format(**environ)
    f.seek(0)
    f.truncate()
    f.write(content)

exit(call(['diamond', '-f', '--skip-pidfile', '-c', environ['DIAMOND_CONF']] +
          argv[1:]))
