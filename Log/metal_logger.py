import logging


log = logging.getLogger('Application Setup')
formatter = logging.Formatter("[%(asctime)s] %(name)s: [%(filename)s] [%(levelname)s] %(message)s", datefmt="%Y/%m/%d %H:%M:%S")
fileHandler = logging.FileHandler('Application.log')
consoleHandler = logging.StreamHandler()
log.addHandler(consoleHandler)
log.addHandler(fileHandler)
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)
log.setLevel(logging.DEBUG)
