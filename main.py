from bbcon import BBCON

from flee_behaviour import FleeBehaviour
from attack_behaviour import AttackBehaviour
from explore_behaviour import ExploreBehaviour
from investigate_sides_behaviour import InvestigateSidesBehaviour
from investigate_forward_behaviour import InvestigateForwardBehaviour

from sensob_ultrasonic import SensobUltrasonic
from sensob_irproximity import SensobIrproximity
from color_sensob import ColorSensob

from motobs import MainMotob


def main():
    sensobs = {
        'ultrasonic': SensobUltrasonic(),
        'irproximity': SensobIrproximity(),
        'greencamera': ColorSensob(),
        'redcamera': ColorSensob(),
    }

    behaviours = [
        FleeBehaviour(sensobs, 1),
        AttackBehaviour(sensobs, 1),
        ExploreBehaviour(sensobs, 1),
        InvestigateSidesBehaviour(sensobs, 1),
        InvestigateForwardBehaviour(sensobs, 1),
    ]

    motobs = [
        MainMotob(),
    ]

    bbcon = BBCON(behaviours, sensobs, motobs)

    try:
        while True:
            bbcon.run_one_timestep()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
