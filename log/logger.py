class logger(object):
    """
        Logger used for writing messages to database
    """

    def __init__(self, type, log_level, **kwargs):
        self._set_log_attributes(type, kwargs)
        self.set_logging_level(log_level)
