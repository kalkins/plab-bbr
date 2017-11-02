from sensors.irproximity_sensor import IRProximitySensor
from sensob import Sensob


class SensobUltrasonic(Sensob):

    def __init__(self):
        super().__init__()
        self.sensor = IRProximitySensor()
        self.is_detected = [False, False]

    def update(self):
        self.sensor.update()
        self.is_detected = self.sensor.get_value()

    def get_is_detected(self):
        return self.is_detected

    def get_right_detected(self):
        return self.is_detected[0]

    def get_left_detected(self):
        return self.is_detected[1]
