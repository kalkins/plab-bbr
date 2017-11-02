from behaviour import Behaviour

class Investigate_Sides(Behaviour):

    def consider_deactivation(self):
        self.active_flag = True in self.sensobs["irproximitysensob"].value

    def consider_activation(self):
        self.active_flag = True in self.sensobs["irproximitysensob"].value

    def update(self):
        self.consider_activation()
        self.consider_deactivation()
        if self.active_flag:
            self.sense_and_act()
        self.update_weight()

    def sense_and_act(self):
        proximity_sensor = self.sensobs["irproximitysensob"]
        if proximity_sensor.value[0]:
            self.motor_recommendations = [("l", 0.4, 45, -1)]
        elif proximity_sensor.value[1]:
            self.motor_recommendations = [("r", 0.4, 45, -1)]
        self.match_degree = 1

    def update_weight(self):
        self.weight = self.match_degree * self.priority


