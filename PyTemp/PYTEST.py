from flowvrapp import *
from pdi_flowvr import Module_PDI

envmodule = Module_PDI("env", cmdline = "./cputter", pdi_conf = "env.yml")
rlmodule = Module_PDI("learner", cmdline = "python learner.py", pdi_conf = "learner.yml")

envmodule.getPort("text").link(rlmodule.getPort("text"))
rlmodule.getPort("rlval").link(envmodule.getPort("rlval"))
      
app.generate_xml("PYTEST")
