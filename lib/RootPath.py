# -*- coding:utf-8 -*-
class Root():
    path = '/tmp'

import os
x = os.path.abspath(__file__).split('/')
while x.pop():
    if os.path.isdir('/'.join(x)+'/lib'):
        Root.path = '/'.join(x)
        break