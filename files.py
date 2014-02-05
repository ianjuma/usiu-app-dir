#! /usr/bin/env python

# simple python script to get files but no dirs
# JIW

import os
import sys

dir = '.'

software_folders = []

# list comprehension on files
try:
    # iterable
    software_folders += [file for file in os.listdir(dir) if os.path.isfile(file)]
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except OSError as e:
    print "OS error({0}): {1}".format(e.errno, e.strerror)
    print "sure the dir is right?"
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

print software_folders
