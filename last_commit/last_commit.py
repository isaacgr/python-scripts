#!/usr/bin/python

import subprocess
import re
from optparse import OptionParser

def git_version():
    p = subprocess.Popen(["git", "log" , '-1', '--date=iso'], stdout=subprocess.PIPE)
    out, err = p.communicate()
    m = re.search('\d{4}-\d{2}-\d{2}\s', out)
    return m.group(0)

usage = "usage: %prog -f filepath"
parser = OptionParser(usage=usage)
parser.add_option("-f", default='version.py')
(options, args) = parser.parse_args()
path = options.f
with open(path, 'w+') as f:
    version = git_version().replace('-', '.')
    f.write(version)
