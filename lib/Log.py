# -*- coding:utf-8 -*-
import os, sys
import logging, traceback
from logging.handlers import TimedRotatingFileHandler
from RootPath import ROOT_PATH

LOG_PATH = os.path.splitext(os.path.join(ROOT_PATH,'logs',(os.path.abspath(sys.argv[0])).replace(ROOT_PATH+'/','')))[0]+'.log'

if not os.path.isdir(os.path.dirname(LOG_PATH)):
    os.makedirs(os.path.dirname(LOG_PATH))

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_handler = TimedRotatingFileHandler(LOG_PATH, when='midnight', interval=1, backupCount=370)
log_handler.setFormatter(logging.Formatter("%(asctime)-15s,%(message)s"))
log_handler.suffix = "%Y%m%d"
logger.addHandler(log_handler)