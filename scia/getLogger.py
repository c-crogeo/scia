from . import config
from .handlers import TimedRotatingFileHandler
from logging import getLogger
import logging.config
import os


_configured = False


def get_logger(name):
    """
    Do configuration and call standard logging.getLogger
    :param name: Logger name
    :return: Logger
    """
    global _configured
    if not _configured:
        inifile = config.inifile
        if os.path.isfile(inifile):
            logging.config.fileConfig(inifile, {'project': config.project})
        else:
            # Default configuration
            fmt = '%(asctime)s - %(name)10s - %(levelname)8s - %(message)s'
            logging.basicConfig(
                format=fmt,
                level='DEBUG'
            )
        _configured = True
    return getLogger(name)
