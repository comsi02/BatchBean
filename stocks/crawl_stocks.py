# -*- coding:utf-8 -*-
import sys, os
import requests
import json

x = os.path.abspath(__file__).split('/')
while x.pop(): sys.path.append('/'.join(x)+'/lib') if os.path.isdir('/'.join(x)+'/lib') else ''

from BatchBean import *

url = 'https://www.investing.com/indices/nq-100-futures?cid=1175151'

custom_header = {
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

class Batch(BatchBean):

    @tracebacks(telegram="telegram_api_key", line="line_api_key")
    def main(self):#{

        req = requests.get(url, headers = custom_header)

        print(req.session())

        if req.status_code == requests.codes.ok:
            stock_data = req.text.split('instrument-price-last">')[1].split("</span>")
            print(stock_data[0])
        pass
    #}
    
    def addArgParserOptions(self, argParser):#{
        argParser.add_argument('-d','--dttm', required=False, help="yyyy-mm-dd HH:00:00")
        pass
    #}def

if __name__== '__main__':
    b = Batch()
    b.main()
