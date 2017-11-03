from behaviour import Behaviour


class AttackBehaviour(Behaviour):
    def consider_deactivation(self):
        ultraSonic = self.sensobs["ultrasonic"]
        greenCamera = self.sensobs["greencamera"]
        if ultraSonic.get_is_detected() and greenCamera.value < 0.5:
            self.active_flag = False

    def consider_activation(self):
        ultraSonic = self.sensobs["ultrasonic"]
        redCamera = self.sensobs["redcamera"]
        if not ultraSonic.get_is_detected() and redCamera.value > 0.7:
            self.active_flag = True

    def sense_and_act(self):
        if self.active_flag:
            self.motor_recommendations = [("f", 1, 0, 1)]
            self.match_degree = self.sensobs["redcamera"].value
        else:
            self.match_degree = 0
