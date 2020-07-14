from sys import argv, exit
import numpy as np
import pdi, yaml



if __name__ == '__main__':
    
    config_path = "learner.yml"

    with open(config_path, 'r') as config_file:
        try:
            config = yaml.load(config_file)
        except yaml.YAMLError as exc:
            exit(exc)
            
    pdi.init(yaml.dump(config["pdi"]))
    RUN = np.array(0) # read signal from the CSM app to start reading values 
    HASN = np.array(0)
    pdi.expose("RUN_SE", RUN , pdi.IN)
    
    while(RUN != 0):
        print("Python: from the while loop")
        # RUN=0
        # pdi.reclaim('RUN_SE')

        pdi.expose("HASN", HASN, pdi.IN)
        print("PY HASN: {}".format(HASN))
        # pdi.reclaim('HASN')
        
        pdi.expose("RUN_SE", RUN , pdi.IN)
        
    pdi.finalize()
