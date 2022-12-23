# -*- coding:utf-8 -*-
import sys, os

x = os.path.abspath(__file__).split('/')
while x.pop(): sys.path.append('/'.join(x)+'/lib') if os.path.isdir('/'.join(x)+'/lib') else ''

from BatchBean import *

class Batch(BatchBean):

    @tracebacks(telegram="telegram_api_key", line="line_api_key")
    def main(self):
        self.test1()
        self.test2()
        pass

    @elapse()
    def test1(self):
        tm.sleep(0.1)
        pass

    @elapse()
    def test2(self):
        tm.sleep(0.2)
        pass
    
    # abstract method
    def addArgParserOptions(self, argParser):
        argParser.add_argument('-d','--dttm', required=False, help="yyyy-mm-dd HH:00:00")

    # abstract method
    def addDatabaseConnection(self):
        self.conn['sample1'] = DatabaseManager.connect(self.env, 'mysql_sample', section='primary')
        self.conn['sample2'] = DatabaseManager.connect(self.env, 'mysql_sample', section='secondary')

if __name__== '__main__':
    b = Batch()
    b.main()
