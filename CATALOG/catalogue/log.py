import logging
import logging.handlers


class Logger:
    def __init__(self, log_filename="logs/gs_shell.log"):
        self.logger = logging.getLogger("Default")
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s %(levelname)s - %(message)s')
        LOG_FILENAME = log_filename
        file_handler = logging.handlers.RotatingFileHandler(
            LOG_FILENAME,
            maxBytes=600000,
            backupCount=10
        )
        consoler_handler = logging.StreamHandler()
        consoler_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        consoler_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(consoler_handler)

    def setlevel(self, level):
        self.logger.setLevel(logging[level])
