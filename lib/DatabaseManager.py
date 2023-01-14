# -*- coding:utf-8 -*-
class DatabaseManager():
    @staticmethod
    def databaseConnectMysql(conf):
        try:
            import pymysql

            return pymysql.connect(
                host=conf.get('host')
                , user=conf.get('user')
                , password=str(conf.get('password'))
                , db=conf.get('db')
                , charset=conf.get('charset')
            )
        except ImportError:
            raise Exception("Mysql import error")
        except Exception:
            raise Exception("Mysql connection error")
            
    @staticmethod
    def databaseConnectionMssql(conf):
        try:
            import pytds

            if conf.get('failover_partner',False):
                return pytds.connect(
                    dsn=conf.get('host')
                    , failover_partner=conf.get('failover_partner')
                    , port=conf.get('port')
                    , user=conf.get('user')
                    , password=conf.get('password')
                    , database=conf.get('db')
                )
            else:
                return pytds.connect(
                    dsn=conf.get('host')
                    , port=conf.get('port')
                    , user=conf.get('user')
                    , password=conf.get('password')
                    , database=conf.get('db')
                )
        except ImportError:
            raise Exception("Mssql import error")
        except Exception:
            raise Exception("Mssql connection error")

    @staticmethod
    def databaseConnectionRedis(conf):
        try:
            import redis

            if conf.get('password',False):
                return redis.StrictRedis(
                    host=conf.get('host'),
                    port=conf.get('port'),
                    password=conf.get('password'),
                    db=conf.get('db')
                )
            else:
                return redis.StrictRedis(
                    host=conf.get('host'),
                    port=conf.get('port'),
                    db=conf.get('db')
                )
        except ImportError:
            raise Exception("Redis import error")
        except Exception:
            raise Exception("Redis connection error")

    @staticmethod
    def connect(env, databaseName, **opt):
        try:
            import yaml
            from RootPath import Root

            with open(Root.path+'/config/database.{}.yaml'.format(env),'r') as y:
                y = yaml.safe_load(y)
                conf = y[databaseName][opt.get('section','primary')]
                databaseType = conf.get('type',False)

                if 'mysql' == databaseType:
                    return DatabaseManager.databaseConnectMysql(conf)
                elif 'mssql' == databaseType:
                    return DatabaseManager.databaseConnectMssql(conf)
                elif 'redis' == databaseType:
                    return DatabaseManager.databaseConnectRedis(conf)
                else:
                    raise Exception("Redis connection error")

        except Exception as e:
            raise Exception("Database connection error : %s" % (databaseName))

    @staticmethod
    def close(conn):
        try:
            conn.close()
            del conn
        except Exception as e:
            pass
