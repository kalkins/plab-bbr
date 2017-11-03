from sensors.ultrasonic import Ultrasonic
from sensob import Sensob


class SensobUltrasonic(Sensob):

    def __init__(self):
        self.sensor = Ultrasonic()
        self.is_detected = False
        self.distance = 0

    @property
    def value(self):
        return self.is_detected

    def update(self):
        self.sensor.update()
        self.distance = self.sensor.get_value()
        self.is_detected = self.distance < 15

    def get_is_detected(self):
        return self.is_detected

    def get_distance(self):
        return self.distance
