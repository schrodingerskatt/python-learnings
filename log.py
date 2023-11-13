import logging
logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger('test_logger')
logger.info("This will not show up") # logging.basicConfig(level = logging.DEBUG), because of this line above this msg is being printed
logger.warning("This will")

"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""