from sensors.irproximity_sensor import IRProximitySensor
from sensob import Sensob


class SensobIrproximity(Sensob):

    def __init__(self):
        self.sensor = IRProximitySensor()
        self.is_detected = [False, False]

    @property
    def value(self):
        return self.is_detected

    def update(self):
        self.sensor.update()
        self.is_detected = self.sensor.get_value()

    def get_is_detected(self):
        return self.is_detected

    def get_right_detected(self):
        return self.is_detected[0]

    def get_left_detected(self):
        return self.is_detected[1]
