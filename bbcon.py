from time import sleep
from arbitrator import Arbitrator, HighestArbitrator


class BBCON:
    """The Behaviour-Based Controller."""

    def __init__(self, behaviours, sensobs, motobs, arbitrator=None):
        """
        Initialize the controller.

        Arguments:
        behaviours -- A list of behaviour objects to use
        sensobs    -- A list of sensob objects that the behaviours use
        motobs     -- A list of motob objects to use
        arbitrator -- An arbitrator object or class (default HighestArbitrator)
        """
        self.behaviours = behaviours

        for behaviour in behaviours:
            behaviour.bbcon = self

        self.active_behaviours = []
        self.sensobs = sensobs

        for sensob_name in self.sensobs:
            self.sensobs[sensob_name].update()

        self.motobs = motobs

        if arbitrator is None:
            arbitrator = HighestArbitrator

        if isinstance(arbitrator, Arbitrator):
            self.arbitrator = arbitrator
        else:
            self.arbitrator = arbitrator(self)

    def add_behaviour(self, behaviour):
        """Add a behaviour to the list of available behaviours."""
        if behaviour not in self.behaviours:
            self.behaviours.append(behaviour)

    def add_sensobs(self, sensob):
        """Add a sensob to the list of available sensobs."""
        if sensob not in self.sensobs:
            self.sensobs.append(sensob)

    def activate_behaviour(self, behaviour):
        """Add a behaviour to the list of active behaviours."""
        if behaviour in self.behaviours and behaviour not in self.active_behaviours:
            self.active_behaviours.append(behaviour)

    def deactivate_behaviour(self, behaviour):
        """Remove a behaviour from the list of active behaviours."""
        if behaviour in self.behaviours and behaviour in self.active_behaviours:
            self.active_behaviours.remove(behaviour)

    def run_one_timestep(self):
        # Update active sensobs
        for sensob_name in self.sensobs:
            sensob = self.sensobs[sensob_name]

            if sensob.expensive:
                for behaviour in self.active_behaviours:
                    # If the sensob is required right now
                    if sensob in behaviour.sensobs.values():
                        # Break and update
                        sensob.update()
                        break
                else:
                    # Don't update, and continue to the next sensob
                    continue

            sensob.update()

        # Update behaviours
        for behaviour in self.behaviours:
            behaviour.update()

        if self.active_behaviours:
            action = self.arbitrator.choose_action(self.active_behaviours)

            if action[1]:
                # Halt
                pass

            for motob in self.motobs:
                motob.update(action[0])

        for behaviour in self.behaviours:
            if behaviour.active_flag:
                self.activate_behaviour(behaviour)
            else:
                self.deactivate_behaviour(behaviour)
