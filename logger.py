import logging

def logg():
    logger = logging.getLogger()
    if not logger.handlers:  # Evita adicionar múltiplos handlers
        log_formatter = logging.Formatter('%(asctime)s %(levelname)s - %(funcName)s : Linha %(lineno)d - %(message)s')
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(log_formatter)
        logger.addHandler(consoleHandler)
        logger.setLevel(logging.INFO)
    return logger