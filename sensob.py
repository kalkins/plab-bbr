class Sensob:
    """A generic interface to one or more sensors."""

    def __init__(self):
        self.value = None

    def update(self):
        """Fetch data from sensors."""
        pass
