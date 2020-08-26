from flowvrapp import *
from filters import *
from pdi_flowvr import Module_PDI

envmodule = Module_PDI("env", cmdline = "./run_dssat C UFGA8201.MZX 1", pdi_conf = "env.yml")
rlmodule = Module_PDI("learner", cmdline = "python rl_learner.py", pdi_conf = "learner.yml")

envmodule.getPort("text").link(rlmodule.getPort("text"))

pres = FilterPreSignal( "se_presignal", messagetype = 'full' )
rlmodule.getPort("rlval").link(pres.getPort("in"))
pres.getPort("out").link(envmodule.getPort("rlval"))
# rlmodule.getPort("rlval").link(envmodule.getPort("rlval"))
      
app.generate_xml("CSM")
