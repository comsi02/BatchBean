# -*- coding:utf-8 -*-
import sys, os

x = os.path.abspath(__file__).split('/')
while x.pop(): sys.path.append('/'.join(x)+'/lib') if os.path.isdir('/'.join(x)+'/lib') else ''

from BatchBean import *
from MysqlUtils import *

class Batch(BatchBean):

    @tracebacks(telegram="telegram_api_key", line="line_api_key")
    def main(self):
        self.testSelectWithoutParam()
        self.testSelectWithParam()
        self.testSelectOne()
        self.testSelectDict()

        self.testInsert()
        self.testUpdate()
        self.testDelete()
        self.testInsertDict()
        pass

    @elapse()
    def testSelectWithoutParam(self):
        query = "SELECT * FROM sample.users WHERE sex = 'Female' AND birth like '1977%' LIMIT 2"

        for x in MysqlUtils.select(self.conn['sample_primary'], query, debug=True):
            logger.info(x)

        for x in MysqlUtils.select(self.conn['sample_primary'], query, debug=True, output=list):
            logger.info(x)

    @elapse()
    def testSelectWithParam(self):
        query = "SELECT * FROM sample.users WHERE sex = %s AND birth like %s LIMIT 4"
        param = ['Male', '1977%']

        for x in MysqlUtils.select(self.conn['sample_primary'], query, params=param, debug=True):
            logger.info(x)

    @elapse()
    def testSelectOne(self):
        query = "SELECT * FROM sample.users WHERE sex = %s AND birth like %s LIMIT 4"
        param = ['Male', '1977%']

        x = MysqlUtils.selectOne(self.conn['sample_primary'], query, params=param, debug=True)

        logger.info(x)


    @elapse()
    def testInsert(self):
        query = "INSERT INTO sample.users_modify (`name`, `grade`) VALUES (%s,%s)"
        param1 = ['andrew','12']
        param2 = ['andrew','13']
        MysqlUtils.query(self.conn['sample_primary'], query, params=param1, debug=True, auto_commit=True)
        MysqlUtils.query(self.conn['sample_primary'], query, params=param2, debug=True, auto_commit=True)
        pass

    @elapse()
    def testUpdate(self):
        query = "UPDATE sample.users_modify SET name = %s WHERE grade = %s"
        param1 = ['ANDREW','12']
        param2 = ['ANDREW','13']
        MysqlUtils.query(self.conn['sample_primary'], query, params=param1, debug=True, auto_commit=True)
        MysqlUtils.query(self.conn['sample_primary'], query, params=param2, debug=True, auto_commit=True)
        pass

    @elapse()
    def testDelete(self):
        query = "DELETE FROM sample.users_modify WHERE name = %s AND grade = %s"
        param = ['ANDREW','12']
        MysqlUtils.query(self.conn['sample_primary'], query, params=param, debug=True, auto_commit=True)
        pass

    @elapse()
    def testInsertDict(self):
        table =  "sameple.users_modify"
        param1 = {'name': 'Hm', 'grade': '6'}
        param2 = {'name': 'Tm', 'grade': '4'}
        MysqlUtils.insertDict(self.conn['sample_primary'], "sample.users_modify", param1, debug=True, auto_commit=True)
        MysqlUtils.insertDict(self.conn['sample_primary'], "sample.users_modify", param2, debug=True, auto_commit=True)
        pass

    @elapse()
    def testSelectDict(self):
        tableName = 'sample.users'
        columns = ['firstname','lastname','birth']
        conditions = {'sex':'female','birth':'1977-11-05'}

        for x in MysqlUtils.selectDict(self.conn['sample_primary'],tableName,columns,conditions,debug=True):
            logger.info(x)
        pass

    # abstract method
    def addArgParserOptions(self, argParser):
        argParser.add_argument('-d','--dttm', required=False, help="yyyy-mm-dd HH:00:00")

    # abstract method
    def addDatabaseConnection(self):
        self.conn['sample_primary']   = DatabaseManager.connect(self.env, 'mysql_sample', section='primary')
        self.conn['sample_secondary'] = DatabaseManager.connect(self.env, 'mysql_sample', section='secondary')

if __name__== '__main__':
    b = Batch()
    b.main()
