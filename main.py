from bbcon import BBCON

from flee_behaviour import FleeBehaviour
from attack_behaviour import AttackBehaviour
from explore_behaviour import ExploreBehaviour
from investigate_sides_behaviour import InvestigateSidesBehaviour
from investigate_forward_behaviour import InvestigateForwardBehaviour

from sensob_ultrasonic import SensobUltrasonic
from sensob_irproximity import SensobIrproximity
from color_sensob import ColorSensob

from motob import MainMotob


def main():
    sensobs = {
        'ultrasonic': SensobUltrasonic(),
        'irproximity': SensobIrproximity(),
        'greencamera': ColorSensob((60, 150, 0), 0.3),
        'redcamera': ColorSensob((150, 50, 50), 0.2),
    }

    behaviours = [
        FleeBehaviour(sensobs, 8),
        AttackBehaviour(sensobs, 10),
        ExploreBehaviour(sensobs, 1),
        InvestigateSidesBehaviour(sensobs, 2),
        InvestigateForwardBehaviour(sensobs, 3),
    ]

    motobs = [
        MainMotob(),
    ]

    bbcon = BBCON(behaviours, sensobs, motobs)

    try:
        while True:
            bbcon.run_one_timestep()
    except KeyboardInterrupt:
        motobs[0].update([("s", -1, 0, -1)])


if __name__ == '__main__':
    main()
