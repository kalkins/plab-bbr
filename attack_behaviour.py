from behaviour import Behaviour


class AttackBehaviour(Behaviour):
    sensob_names = ["redcamera", "ultrasonic"]

    def consider_deactivation(self):
        ultraSonic = self.sensobs["ultrasonic"]
        if not ultraSonic.get_is_detected():
            self.active_flag = False

    def consider_activation(self):
        ultraSonic = self.sensobs["ultrasonic"]
        if ultraSonic.get_is_detected():
            self.active_flag = True

    def sense_and_act(self):
        red_value = self.sensobs["redcamera"]
        if red_value > 0.7:
            self.motor_recommendations = [("f", 1, 0, 1)]
            self.match_degree = red_value
        else:
            self.motor_recommendations = []
            self.match_degree = 0
