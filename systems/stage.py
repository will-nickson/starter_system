from log.logger import logger


class SystemStage(object):
    """
        Default stage object: creates a SystemStage for doing something
    """

    @property
    def name(self):
        return "Need to replace name when inheriting"
    
    def __repr__(self):
        return "SystemStage '%s' Try %s.methods()" % (
            self.name,
            self.name,
        )
    
    def methods(self):
        return get_methods(self)

    def system_init(self, system: System):
        # method called once we have a system
        self._parent = system

        # and a log
        log = system.log.setup(stage=self.name)
        self._log = log

    @property
    def log(self) -> logger:
        log = getattr(self, "_log", logtoscreen(""))
        return log

    @property
    def parent(self) -> System:
        parent = getattr(self, "_parent", None)
        return parent
