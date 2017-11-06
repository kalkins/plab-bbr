from behaviour import Behaviour


class InvestigateForwardBehaviour(Behaviour):
    sensob_names = ["ultrasonic"]

    def consider_deactivation(self):
        """Consider whether the behaviour should be deactivated."""
        self.active_flag = self.sensobs['ultrasonic'].get_is_detected()

    def consider_activation(self):
        """Consider whether the behaviour should be activated."""
        self.active_flag = self.sensobs['ultrasonic'].get_is_detected()

    def sense_and_act(self):
        """Use sensor readings to make motor recommendations."""
        self.match_degree = self.sensobs['ultrasonic'].get_is_detected()
        self.motor_recommendations = [('f', 0.7, 0, -1)]
