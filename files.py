#! /usr/bin/env python

import os

software_folders = []

# list comprehension on files
try:
    software_folders += [for file in os.listdir('/Data/software') if os.path.isfile(file)]
except IOError:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise
