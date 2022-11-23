# -*- coding:utf-8 -*-
import sys, os

x = os.path.abspath(__file__).split('/')
while x.pop(): sys.path.append('/'.join(x)+'/lib') if os.path.isdir('/'.join(x)+'/lib') else ''

from BatchBean import *

class Batch(BatchBean):

    @tracebacks(telegram="telegram_api_key", line="line_api_key")
    def main(self):#{
        pass
    #}
    
    def addArgParserOptions(self, argParser):#{
        argParser.add_argument('-d','--dttm', required=False, help="yyyy-mm-dd HH:00:00")
    #}def

if __name__== '__main__':
    b = Batch()
    b.main()
