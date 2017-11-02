import random

from behaviour import Behaviour


class ExploreBehaviour(Behaviour):
    active_flag = True

    def consider_deactivation(self):
        pass

    def consider_activiation(self):
        pass

    def sense_and_act(self):
        self.match_degree = 0.1
        dirNumber = random.randint(0, 2)

        if dirNumber == 0:
            self.motor_recommendations = [("f", 0.4, 0, -1)]
        elif dirNumber == 1:
            self.motor_recommendations = [("l", 0.4, 45, -1)]
        else:
            self.motor_recommendations = [("r", 0.4, 45, -1)]
