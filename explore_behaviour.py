import random

from behaviour.py import Behaviour


class ExploreBehaviour(Behaviour):
    def consider_deactivation(self):
        if self.active_flag:
            if self.senobs["ultrasonicsenob"].get_is_detected():
                self.active_flag = False

    def consider_activiation(self):
        if not self.active_flag:
            if not self.senobs["ultrasonicsenob"].get_is_detected():
                self.active_flag = True

    def sense_and_act(self):
        if self.active_flag:
            self.match_degree = 0.1
            dirNumber = random.randint(0, 2)
            if dirNumber == 0:
                self.motor_recommendations = [(("f", 0.4, 0, -1))]
            elif dirNumber == 1:
                self.motor_recommendations = [("l", 0.4, 45, -1)]
            else:
                self.motor_recommendations = [("r", 0.4, 45, -1)]
