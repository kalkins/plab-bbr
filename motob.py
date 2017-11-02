from motors import Motors


class Motob:
    """An interface one or more motors."""

    def __init__(self):
        self.motor = Motors()
        self.value = None

    def update(self, rec):
        """Apply a recommendation to the motor."""
        pass

    def operationalize(self):
        """Convert a motor recommendation to one or more motor settings."""
        pass


class MainMotob(Motob):

    def update(self, rec):
        self.value = rec
        self.operationalize()

    def operationalize(self):
        for operation in self.value:
            direction = operation[0].lower()
            speed = operation[1]
            if speed == -1:
                speed = 0.25
            angle = operation[2]
            duration = operation[3]
            if duration == -1:
                duration = 0.5  # To be replaced with potential timestep-time
            turntime = angle/180 * 1/speed * 0.2  # 0.2 is a guess, and must be adjusted
            if direction == "f":
                self.motor.forward(speed, duration)
            elif direction == "r":
                self.motor.backward(speed, duration)
            elif direction == "l":
                self.motor.left(speed, turntime)
            elif direction == "r":
                self.motor.right(speed, turntime)
            elif direction == "s":
                self.motor.stop()
