class Arbitrator:
    """A class that decide which behaviour recommendation to follow."""

    def __init__(self, bbcon):
        self.bbcon = bbcon

    def choose_action(self):
        """Decide which behaviour to use."""
        pass


class HighestArbitrator(Arbitrator):
    def choose_action(self, behaviours):
        number = 0
        halt = False

        for behaviour in behaviours:
            if behaviour.halt_request:
                halt = True

            if number > behaviour.weight:
                number = behaviour.weight
                correctBehaviour = behaviour

        return (correctBehaviour.motor_recommendations, halt)
