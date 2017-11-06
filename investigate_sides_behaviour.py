from behaviour import Behaviour


class InvestigateSidesBehaviour(Behaviour):
    sensob_names = ["irproximity"]

    def consider_deactivation(self):
        self.active_flag = True in self.sensobs["irproximity"].value

    def consider_activation(self):
        self.active_flag = True in self.sensobs["irproximity"].value

    def sense_and_act(self):
        proximity_sensor = self.sensobs["irproximity"]
        if proximity_sensor.value[0]:
            self.motor_recommendations = [("l", 0.8, 45, -1)]
        elif proximity_sensor.value[1]:
            self.motor_recommendations = [("r", 0.8, 45, -1)]
        self.match_degree = 1
