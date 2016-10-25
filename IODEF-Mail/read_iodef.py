# coding: utf-8

import sys
import iodef


if len(sys.argv) < 2:
    print("Usage: python {0} [FILE]\n\nWhere the FILE is a IODEF, JSON formatted".format(sys.argv[0]))
    sys.exit()

try:
    with open(sys.argv[1], 'r') as fd:
        msg = iodef.IODEF(fd.read())
except IOError, e:
    print(e)
    sys.exit()

print msg
