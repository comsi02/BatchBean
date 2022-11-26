# -*- coding:utf-8 -*-
import datetime as dt
import time as tm
from Log import *

def tracebacks(**kwargs):
    def tags_decorator(func):
        from functools import wraps
        @wraps(func)
        def func_wrapper(name):
            start_dt = dt.datetime.now()
            logger.info("-"*100)
            logger.info("[START]")
            logger.info("-"*100)
            try:
                func(name)
            except:
                traceback_msg = "Traceback: %s" % traceback.format_exc()
                traceback_msg_array = []
                traceback_msg_array.append("*" * 100)
                traceback_msg_array.append("[Traceback-start]")
                traceback_msg_array.append("")
                traceback_msg_array.append(traceback_msg)
                traceback_msg_array.append("[Traceback-end]")
                traceback_msg_array.append("*" * 100)

                logger.info("\n"+"\n".join(traceback_msg_array))
                print("\n".join(traceback_msg_array))

                if kwargs.get("telegram",False):
                    # send telegram alert use telegram_api_key
                    pass
                elif kwargs.get("line",False):
                    # send line alert use line_api_key
                    pass
            finally:
                logger.info("-"*100)
                logger.info("[ END ] - elapse : %s ms",(dt.datetime.now() - start_dt).total_seconds())
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
            logger.info(" * (%s) - elapse : %s ms" % (func.__name__,(dt.datetime.now() - start_dt).total_seconds()))
        return func_wrapper
    return tags_decorator

class BatchBean():
    def __init__(self):
        import argparse
        import atexit

        argParser = argparse.ArgumentParser(description='========== [ ' + sys.argv[0] + ' ] ==========')
        self.addArgParserOptionsWrapper(argParser)

        atexit.register(self.cleanup)

    def cleanup(self):
        pass

    def addArgParserOptionsWrapper(self, argParser):
        argParser.add_argument('-g','--debug', required=True, choices=['yes','no'], help="yes:debug mode, n0:normal mode")
        self.addArgParserOptions(argParser)
        self.args = argParser.parse_args()

    def addArgParserOptions(self, parser):
        pass

