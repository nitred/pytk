"""
File to setup the logging functionality for a project.

Authors: Ankur Srivastava, Daiem Ali
"""
import os
import logging
import logging.handlers


class LogFormatter(logging.Formatter):
    """Format the meta data in the log message to fix string length."""

    datefmt = '%Y-%m-%d %H:%M:%S'

    def format(self, record):
        """Default formatter."""
        error_location = "%s.%s" % (record.name, record.funcName)
        line_number = "%s" % (record.lineno)
        location_line = error_location[:32] + ":" + line_number
        s = "%.19s [%-8s] [%-36s] %s" % (self.formatTime(record, self.datefmt),
                                         record.levelname,  location_line, record.getMessage())
        return s


def setup_logger():
    """Set up the global logging settings."""
    generated_files = 'logs'
    ALL_LOG_FILENAME = '{0}/all.log'.format(generated_files)
    ERROR_LOG_FILENAME = '{0}/error.log'.format(generated_files)
    if not os.path.exists(generated_files):
        os.makedirs(generated_files)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to info
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(LogFormatter())
    logger.addHandler(handler)

    # create error file handler and set level to error
    handler = logging.handlers.RotatingFileHandler(ERROR_LOG_FILENAME,
                                                   maxBytes=1000000,
                                                   backupCount=100)
    handler.setLevel(logging.ERROR)
    handler.setFormatter(LogFormatter())
    logger.addHandler(handler)

    # create debug file handler and set level to debug
    handler = logging.handlers.RotatingFileHandler(ALL_LOG_FILENAME,
                                                   maxBytes=1000000,
                                                   backupCount=100)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(LogFormatter())
    logger.addHandler(handler)

    print('Logging into directory {}\n'.format(generated_files))


if __name__ == '__main__':
    # Define your logger here in the main.
    setup_logger()
