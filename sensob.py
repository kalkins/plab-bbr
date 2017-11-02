class Sensob:
    """A generic interface to one or more sensors."""

    expensive = False

    def update(self):
        """Fetch data from sensors."""
        pass

    def reset(self):
        """Reset the sensor"""
        pass
