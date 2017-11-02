from behaviour import Behaviour


class FleeBehaviour(Behaviour):

    def consider_activation(self):
        self.active_flag = self.sensobs["greencamerasensob"].value > 0.5

    def consider_deactivation(self):
        self.active_flag = self.sensobs["greencamerasensob"].value <= 0.5

    def update(self):
        self.consider_activation()
        self.consider_deactivation()
        if self.active_flag:
            self.sense_and_act()
        self.updateWeight()

    def sense_and_act(self):
        self.motor_recommendations = [("r", 0.6, 180, -1), ("f", 1, 0, -1)]
