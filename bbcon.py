class BBCON:
    """The Behaviour-Based Controller."""

    def __init__(self):
        self.behaviours = []
        self.active_behaviours = []
        self.sensobs = []
        self.motobs = []
        self.arbitrator = None

    def add_behaviour(self, behaviour):
        """Add a behaviour to the list of available behaviours."""
        pass

    def add_sensobs(self, sensob):
        """Add a sensob to the list of available sensobs."""
        pass

    def activate_behaviour(self, behaviour):
        """Add a behaviour to the list of active behaviours."""
        pass

    def deactivate_behaviour(self, behaviour):
        """Remove a behaviour from the list of active behaviours."""
        pass

    def run_one_timestep(self):
        pass
