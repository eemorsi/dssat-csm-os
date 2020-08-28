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

    pdi.init(yaml.dump(config["pdi"]))
    RUN = np.array(0)  # read signal from the CSM app to start reading values
    HASN = np.array(0)
    
    pdi.expose("RUN_SE", RUN, pdi.IN)

    SIM_FERT_VAL = np.zeros(4, dtype=float, order='F') #np.array(0, dtype=float)#np.zeros(4, dtype=float, order='F')

    CNT = 1
    while(RUN != 0):
        print("Python: from the while loop")
      
        SIM_FERT_VAL[:]= 0.1 * CNT
        # pass fertilization data to the simulator
        pdi.expose("RL_FERT_VAL", SIM_FERT_VAL, pdi.OUT)

        pdi.expose("HASN", HASN, pdi.IN)
        print("PY HASN: {}".format(HASN))
        CNT += 1

        pdi.expose("RUN_SE", RUN, pdi.IN)

    pdi.finalize()
