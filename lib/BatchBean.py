# -*- coding:utf-8 -*-
import datetime as dt
import time as tm
from DatabaseManager import *
from Log import *

def tracebacks(**kwargs):
    def tags_decorator(func):
        from functools import wraps
        @wraps(func)
        def func_wrapper(name):
            start_dt = dt.datetime.now()
            logger.info("-"*100)
            logger.info("[BGN - (%s)]" % (name))
            logger.info("-"*100)
            try:
                func(name)
            except Exception as e:
                traceback_msg = "Traceback: %s" % traceback.format_exc()
                traceback_msg_array = []
                traceback_msg_array.append("*" * 100)
                traceback_msg_array.append("[Traceback-start]")
                traceback_msg_array.append("")
                traceback_msg_array.append(traceback_msg)
                traceback_msg_array.append("[Traceback-end]")
                traceback_msg_array.append("*" * 100)

                exception_msg = "Exception: %s" % e

                logger.info("\n"+"\n".join(traceback_msg_array))
                logger.info(exception_msg)

                print("\n".join(traceback_msg_array))
                print(exception_msg)

                if kwargs.get("telegram",False):
                    # send telegram alert use telegram_api_key
                    pass
                elif kwargs.get("line",False):
                    # send line alert use line_api_key
                    pass
            finally:
                logger.info("-"*100)
                logger.info("[END - (%s)] - elapse : %s ms" % (name,(dt.datetime.now() - start_dt).total_seconds()))
                logger.info("-"*100)
                sys.exit(-1)
        return func_wrapper
    return tags_decorator

def elapse():
    def tags_decorator(func):
        from functools import wraps
        @wraps(func)
        def func_wrapper(name):
            start_dt = dt.datetime.now()
            func(name)
            logger.info("#"*(26+int(len(func.__name__))))
            logger.info("# ({}) - elapse : {:.3f} ms #".format(func.__name__,(dt.datetime.now() - start_dt).total_seconds()))
            logger.info("#"*(26+int(len(func.__name__))))
            logger.info("")
        return func_wrapper
    return tags_decorator

class BatchBean():
    def __init__(self):
        logger.info("")
        logger.info("[INT]"+"-"*95)

        try:
            import argparse
            import atexit

            argParser = argparse.ArgumentParser(description='========== [ ' + sys.argv[0] + ' ] ==========')

            self.addArgParserOptionsWrapper(argParser)
            self.addDatabaseConnectionWarrper()

            atexit.register(self.cleanup)
        except:
            pass

    def cleanup(self):
        if self.conn:
            for name,conn in sorted(self.conn.items()):
                DatabaseManager.close(conn)
                logger.info(" * db close  : %-20s : %s" % (name,conn))

        logger.info("[DEL]"+"-"*95)

    def addArgParserOptionsWrapper(self, argParser):
        argParser.add_argument('-e','--env', required=True, choices=['dev','prod'], help="dev:development mode, prod:production mode")
        self.addArgParserOptions(argParser)
        self.args = argParser.parse_args()
        self.env = self.args.env

        logger.info(" * argparse  : {}".format(self.args))

    def addDatabaseConnectionWarrper(self):
        self.conn = {}
        self.addDatabaseConnection()

        for name,conn in sorted(self.conn.items()):
            logger.info(" * db connect: %-20s : %s" % (name,conn))

    def addArgParserOptions(self, parser):
        pass

    def addDatabaseConnection(self):
        pass