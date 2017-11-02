from behavior import Behaviour


class AttackBehaviour(Behaviour):
    def consider_deactivation(self):
        ultraSonic = self.sensobs["ultrasonicsensob"]
        greenCamera = self.sensobs["greencamerasensob"]
        if ultraSonic.get_is_detected() and greenCamera.value() < 0.5:
            self.active_flag = False

    def consider_activation(self):
        ultraSonic = self.sensobs["ultrasonicsensob"]
        redCamera = self.sensobs["redcamerasensob"]
        if not ultraSonic.get_is_detected() and redCamera.value() > 0.7:
            self.active_flag = True

    def sense_and_act(self):
        if self.active_flag:
            self.motor_recommendations = [("f", 1, 0, 1)]
            self.match_degree = self.sensobs["redcamerasensob"].value()
        else:
            self.match_degree = 0
