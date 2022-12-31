from Log import *

class MysqlUtils:
    @staticmethod
    def init(query,opt):
        import pymysql

        params = opt.get('params',[])
        output = None
        if opt.get('output',dict) == dict:
            output = pymysql.cursors.DictCursor

        if opt.get('debug',False) == True:
            try:
                logger.info(query % tuple(["'%s'" % x if x != None else 'null' for x in params]))
            except:
                logger.info(query)
                logger.info(params)

        return query, params, output

    @staticmethod
    def select(conn,query,**opt):
        query, params, output = MysqlUtils.init(query,opt)
        with conn.cursor(output) as cursor:
            if params:
                cursor.execute(query,params)
            else:
                cursor.execute(query)
            return cursor

    @staticmethod
    def selectOne(conn,query,**opt):
        query, params, output = MysqlUtils.init(query,opt)
        with conn.cursor(output) as cursor:
            if params:
                cursor.execute(query,params)
            else:
                cursor.execute(query)
            row = cursor.fetchone()
            if row:
                return row
            else:
                if opt.get('default',False) == True:
                    return opt['default']
                else:
                    return {} if output else []

    @staticmethod
    def query(conn,query,**opt):
        query, params, output = MysqlUtils.init(query,opt)
        with conn.cursor() as cursor:
            if params:
                res = cursor.execute(query,params)
            else:
                res = cursor.execute(query)
            if opt.get('auto_commit',False) == True:
                conn.commit()
            return res
    
    @staticmethod
    def escapeColumn(colName):
        return '`{}`'.format(colName.replace('`', '``'))

    @staticmethod
    def selectDict(conn, tableName, columns, conditions, **opt):
        whereCondition = ' AND '.join(["`{}` = '{}'".format(k,v) for k,v in conditions.items()])
        cols = ', '.join(map(MysqlUtils.escapeColumn, columns))
        sql = "SELECT %s FROM %s WHERE %s" % (cols, tableName, whereCondition)
        return MysqlUtils.select(conn, sql, output=opt.get('output',dict), debug=opt.get('debug',False))
 
    @staticmethod
    def insertDict(conn, tableName, param, **opt):
        names = list(param)
        cols = ', '.join(map(MysqlUtils.escapeColumn, names))
        vals = ', '.join(['%({})s'.format(name) for name in names])
        sql = 'INSERT INTO {} ({}) VALUES ({})'.format(tableName, cols, vals)
        return MysqlUtils.query(conn, sql, params=param, auto_commit=opt.get('auto_commit', False), debug=opt.get('debug',False))
