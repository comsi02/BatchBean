# -*- coding:utf-8 -*-
import os, sys
import logging
from logging.handlers import TimedRotatingFileHandler
from RootPath import Root

logPath = os.path.splitext(os.path.join(Root.path,'logs',(os.path.abspath(sys.argv[0])).replace(Root.path+'/','')))[0]+'.log'

if not os.path.isdir(os.path.dirname(logPath)):
    os.makedirs(os.path.dirname(logPath))

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_handler = TimedRotatingFileHandler(logPath, when='midnight', interval=1, backupCount=370)
log_handler.setFormatter(logging.Formatter("%(asctime)-15s,%(message)s"))
log_handler.suffix = "%Y%m%d"
logger.addHandler(log_handler)