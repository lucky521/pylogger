#!/usr/bin/env python
from datetime import *
import logging.handlers
from logging import *
import traceback
import os

log_file = "./log/logger.log"
log_format = "%(asctime)s %(levelname)s %(filename)s:%(lineno)s %(funcName)s() %(message)s"

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
rht = logging.handlers.TimedRotatingFileHandler(log_file,'d')
#rht.suffix = "%Y-%m-%d_%H-%M-%S.log"
fmt = logging.Formatter(log_format, "%Y-%m-%d %H:%M:%S")
rht.setFormatter(fmt)
logger.addHandler(rht)

debug = logger.debug
info = logger.info
warning = logger.warn
error = logger.error
critical = logger.critical


def logging_for_func(level='INFO'):
    logging.basicConfig(level=DEBUG,
		    format=log_format,
		    datefmt='%Y-%m-%d %H:%M:%S',
		    filename=log_file,
		    filemode='a')

    def _raw_log(logfn, message, exc_info):
        loc = ''
        fn = ''
        tb = traceback.extract_stack()
	print tb
        if len(tb) > 2:
            loc = '(%s:%d):' % (os.path.basename(tb[-3][0]), tb[-3][1])
            fn = tb[-3][2]
            if fn != '<module>':
                fn += '()'
	print loc + fn
        logfn(message, exc_info=exc_info)

    def debug(message, exc_info=False):
        _raw_log(logging.debug, message, exc_info)

    def warning(message, exc_info=False):
        _raw_log(logging.warning, message, exc_info)

    def error(message, exc_info=False):
        _raw_log(logging.error, message, exc_info)

    def info(message, exc_info=False):
        _raw_log(logging.info, message, exc_info)

    def hundle_func(func):
        def call_inside(*args, **kwargs):
            start_message = 'Entering %s(). ARGS=%s, KWARGS=%s.' % (func.__name__, args, kwargs)
            if level == 'INFO':
                info(start_message)
            elif level == 'DEBUG':
                debug(start_message)
            elif level == 'WARNING':
                warning(start_message)
            elif level == 'ERROR':
		error(start_message)

            start = datetime.now()
            result = func(*args, **kwargs)
            end = datetime.now()
            elapsed = end - start

            end_message = 'Exited %s(). Returnvalue=%s. Time=%s' % (func.__name__, result, elapsed)
            if level == 'INFO':
                info(end_message)
            elif level == 'DEBUG':
                debug(end_message)
            elif level == 'WARNING':
                warning(end_message)
            elif level == 'ERROR':
                error(end_message)

            return result
        return call_inside

    return hundle_func

