class Motob:
    """An interface one or more motors."""

    def __init__(self):
        self.motors = []
        self.value = None

    def update(self, rec):
        """Apply a recommendation to the motor."""
        pass

    def operationalize(self, rec):
        """Convert a motor recommendation to one or more motor settings."""
        pass
