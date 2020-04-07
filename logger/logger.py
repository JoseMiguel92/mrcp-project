import logging
import logging.handlers
import sys
import datetime


class Logger:
    LEVEL = logging.DEBUG

    @staticmethod
    def init_log():
        logging.basicConfig(stream=sys.stdout, format='%(asctime)s\t%(levelname)s\t%(name)s\t%(message)s',
                            level=Logger.LEVEL)
        logging.info('Logging started')
