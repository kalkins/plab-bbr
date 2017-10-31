class Behaviour:
    """A behaviour analyzes some sensors and determines what the motors should do."""

    def __init__(self):
        self.bbcon = None
        self.sensobs = []
        self.motor_recommendations = []
        self.active_flag = False
        self.halt_request = False
        self.priority = 0
        self.match_degree = 0
        self.weight = 0

    def consider_deactivation(self):
        """Consider whether the behaviour should be deactivated."""
        return False

    def consider_activation(self):
        """Consider whether the behaviour should be activated."""
        return False

    def update(self):
        """Update the behaviours status."""
        pass

    def sense_and_act(self):
        """Use sensor readings to make motor recommendations."""
        pass
