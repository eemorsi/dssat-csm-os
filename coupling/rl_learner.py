from sys import argv, exit
import numpy as np
import pdi
import yaml


if __name__ == '__main__':

    config_path = "learner.yml"

    with open(config_path, 'r') as config_file:
        try:
            config = yaml.load(config_file)
        except yaml.YAMLError as exc:
            exit(exc)

    pdi.init(yaml.dump(config['pdi']))
    RUN = np.array(0)  # read signal from the CSM app to start reading values
    HASN = np.array(0)
    pdi.expose('RUN_SE', RUN, pdi.IN)

    RL_VALs = np.array(0)

    SIM_FERT_VAL= np.array(4, dtype=float)


    while(RUN != 0):
        # Force simulate to read some values from the learner but not the interanl values
        RL_VALs = 1
        pdi.expose('RUN_SE', RL_VALs, pdi.IN)

        # pass fertilization data to the simulator
        pdi.expose("RL_FERT_VAL", SIM_FERT_VAL, pdi.out)

        pdi.expose("HASN", HASN, pdi.IN)
        print("HASN: {}".format(HASN))

        # may change run value to indicate the input from the learner
        # RUN=3
        pdi.expose('RUN_SE', RUN, pdi.IN)

    pdi.finalize()
