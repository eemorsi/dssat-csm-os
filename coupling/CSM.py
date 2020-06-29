from flowvrapp import *
from pdi_flowvr import Module_PDI

envmodule = Module_PDI("env", cmdline = "./run_dssat C UFGA8201.MZX 1", pdi_conf = "env.yml")
rlmodule = Module_PDI("learner", cmdline = "python rl_learner.py", pdi_conf = "learner.yml")

envmodule.getPort("text").link(rlmodule.getPort("text"))
rlmodule.getPort("rl_val").link(envmodule.getPort("rl_val"))
      
app.generate_xml("csm")