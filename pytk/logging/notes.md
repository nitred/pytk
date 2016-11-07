# Notes

### TimedRotatingFileHandler
Another example is to change RotatingFileHandler to TimedRotatingFileHandler. In this case a log file will be rotated every 'D' ( 1 day ) and with a backup count of 120 ( which roughly is 4 months ).
```python
handler = logging.handlers.TimedRotatingFileHandler(ERROR_LOG_FILENAME,
                                                    when='D',
                                                    backupCount=120)
```

### Usage Instructions
Don't foget to declare a module level logger using.
```python
logger = logging.getLogger(__name__)
```
###### Example
```python
import logging

logger = logging.getLogger(__name__)


def my_func():
    logger.info("I will be on console+all.log file but NOT in error.log file")
    print
    print("Debug logs go to all.log, as they are extensive and needed for debugging")
    print
    logger.debug("I will be in all.log file, but NOT on console")
    logger.warning("I will be on console+all.log file but NOT in errror.log file")
    logger.error("I will be on console+all.log file + EXPLICITLY in error.log file")
    logger.critical("I will be on console+all.log file + EXPLICITLY in error.log file")
```
