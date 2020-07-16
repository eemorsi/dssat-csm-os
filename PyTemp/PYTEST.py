from flowvrapp import *
from filters import *
from pdi_flowvr import Module_PDI

envmodule = Module_PDI("env", cmdline = "./cputter", pdi_conf = "env.yml")
rlmodule = Module_PDI("learner", cmdline = "python learner.py", pdi_conf = "learner.yml")

# envmodule.getPort("text").link(rlmodule.getPort("text"))

# Connection from gldens to fluid simulation
pres = FilterPreSignal( "se_presignal", messagetype = 'full' )
envmodule.getPort("text").link(pres.getPort("in"))
pres.getPort("out").link(rlmodule.getPort("text"))


rlmodule.getPort("rlval").link(envmodule.getPort("rlval"))
      
app.generate_xml("PYTEST")
