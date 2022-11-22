# -*- coding:utf-8 -*-
import socket
from Log import *

def tracebacks(**kwargs):
    def tags_decorator(func):
        from functools import wraps
        @wraps(func)
        def func_wrapper(name):
            try:
                func(name)
            except:
                traceback_msg = "Traceback: %s" % traceback.format_exc()
                traceback_msg_array = []
                traceback_msg_array.append("*" * 100)
                traceback_msg_array.append("[Traceback-start]")
                traceback_msg_array.append(traceback_msg)
                traceback_msg_array.append("[Traceback-end]")
                traceback_msg_array.append("*" * 100)

                logger.info("\n"+"\n".join(traceback_msg_array))
                print("\n".join(traceback_msg_array))

                if kwargs.get("alert",False):
                    #send alert
                    #msg = "[ %s ][ %s ]\n\n%s" % (socket.gethostname(),sys.argv[0],traceback_msg)
                    pass

                sys.exit(-1)
        return func_wrapper
    return tags_decorator

class BatchBean():
    def __init__(self):
        import argparse
        import atexit

        logger.info("-"*100)
        logger.info("[START]")
        logger.info("-"*100)

        argParser = argparse.ArgumentParser(description='========== [ ' + sys.argv[0] + ' ] ==========')
        self.addArgParserOptionsWrapper(argParser)

        atexit.register(self.cleanup)

    def cleanup(self):
        logger.info("-"*100)
        logger.info("[ END ]")
        logger.info("-"*100)

    def addArgParserOptionsWrapper(self, argParser):

        argParser.add_argument('-g','--debug', required=True, choices=['yes','no'], help="yes:debug mode, n0:normal mode")

        self.addArgParserOptions(argParser)
        self.args = argParser.parse_args()

    def addArgParserOptions(self, parser):
        pass