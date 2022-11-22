# -*- coding:utf-8 -*-
import os
x = os.path.abspath(__file__).split('/')
ROOT_PATH = '/tmp'
while x.pop():
    if os.path.isdir('/'.join(x)+'/lib'):
        ROOT_PATH = '/'.join(x)
        break