from behavior import Behaviour

class attackBehaviour(Behaviour):
    def consider_deactivation(self):
        if self.active_flag:
            ultraSonic = self.sensobs["ultrasonicsensob"]
            greenCamera = self.sensobs["greencamerasensob"]
            if ultraSonic.get_is_detected() and greenCamera.value() < 0.5:
                self.active_flag = False

    def consider_activation(self):
        if not self.active_flag:
            ultraSonic = self.sensobs["ultrasonicsensob"]
            redCamera = self.sensobs["redcamerasensob"]
            if not ultraSonic.get_is_detected() and redCamera.value() > 0.7:
                self.active_flag = True

    def update(self):
        self.consider_activation()
        self.consider_deactivation()
        self.sense_and_act()
        self.updateWeight()

    def sense_and_act(self):
        if self.active_flag:
            self.motor_recommendations = [("f",1,0,1)]
            self.match_degree = self.sensobs["redcamerasensob"].value()
        else:
            self.match_degree = 0

    def updateWeight(self):
        self.weight = self.match_degree * self.priority
