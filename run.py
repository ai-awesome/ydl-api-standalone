#!/usr/bin/env python3

import os

os.chdir('dist')
os.execl('./main', ['./main'])
