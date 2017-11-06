from behaviour import Behaviour


class FleeBehaviour(Behaviour):
    sensob_names = ["greencamera", "ultrasonic"]

    def consider_deactivation(self):
        ultraSonic = self.sensobs["ultrasonic"]
        if not ultraSonic.get_is_detected():
            self.active_flag = False

    def consider_activation(self):
        ultraSonic = self.sensobs["ultrasonic"]
        if ultraSonic.get_is_detected():
            self.active_flag = True

    def sense_and_act(self):
        green_value = self.sensobs["greencamera"].value
        if green_value > 0.5:
            self.motor_recommendations = [("r", 0.6, 180, -1), ("f", 1, 0, -1)]
            self.match_degree = green_value
        else:
            self.motor_recommendations = []
            self.match_degree = 0
