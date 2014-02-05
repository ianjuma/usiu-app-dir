#! /usr/bin/env python

import os

software_folders = []

# list comprehension on files
software_folders += [for file in os.listdir('/Data/software') if os.path.isfile(file)]
