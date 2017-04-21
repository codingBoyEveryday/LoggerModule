import logging


class ISensitLogger:
    """This class defines the default settings
    of logging info. It also enables us to change
    the logging file, the format and the level of
    logging info. The class also enables the user
    to type the logging info by themselves.

    """
    def __init__(self):
        """This is for the initialization of class
        ISensitLogger. The default filename saving
        the logging info, the default format of the
        logging info, the default logging level.


        """
        self.filename = 'isensit.log'
        self.format = '%(levelname)s:%(asctime)s, %(message)s'
        self.level = logging.DEBUG
        self.logger = logging.getLogger()
        self.logger.setLevel(self.level)
        logging.basicConfig(filename=self.filename, format=self.format, level=self.level)

    def format_enable_filename(self):
        """This function is to enable the format of
        logging info to contain the file name that
        calls the logging.


        """
        self.format = '%(levelname)s:%(asctime)s, %(filename)s, %(message)s'

    def format_enable_lineno(self):
        """This function is to enable the format of
        logging info to contain the line number in
        the code that calls the logging.


        """
        self.format = '%(levelname)s:%(asctime)s, %(filename)s, line: %(lineno)d, %(message)s'

    def log_file_settings(self, filename=None, level=None):
        """This function is to reset the file name or
        logging level instead of the default settings.


        :param filename: the file containing the logging info
        :param level: the logging level
        """
        if filename is not None:
            self.filename = filename
        if level is not None:
            self.level = level

        handler = logging.FileHandler(self.filename)
        handler.setLevel(self.level)

        # Create formatter for the logging info
        formatter = logging.Formatter(self.format)

        # Add formatter to handler
        handler.setFormatter(formatter)

        # Add handler to logger
        self.logger.addHandler(handler)

        logging.basicConfig(filename=self.filename, format=self.format, level=self.level)

    @staticmethod
    def log(msg='', level='DEBUG'):
        """This function is to generate the logging message
        corresponding to the logging level

        :param msg: the logging message
        :param level: the logging level
        """
        if level == 'DEBUG':
            logging.debug(msg)

        if level == 'INFO':
            logging.info(msg)

        if level == 'WARNING':
            logging.warning(msg)

        if level == 'ERROR':
            logging.error(msg)

        if level == 'CRITICAL':
            logging.critical(msg)

