from flowvrapp import *
from pdi_flowvr import Module_PDI

putmodule = Module_PDI("put", cmdline = "./run_dssat C UFGA8201.MZX 1", pdi_conf = "env.yml")
getmodule = Module_PDI("get", cmdline = "python rl_learner.py", pdi_conf = "learner.yml")

putmodule.getPort("text").link(getmodule.getPort("text"))
        
app.generate_xml("csm")