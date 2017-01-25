## Minimal 3-node example of PyPSA linear optimal power flow
#
#Available as a Jupyter notebook at <http://www.pypsa.org/examples/minimal_example_opf.ipynb>.

# make the code as Python 3 compatible as possible
from __future__ import print_function, division
import pypsa
import numpy as np

network = pypsa.Network()

#add three buses
for i in range(3):
    network.add("Bus","My bus {}".format(i))

print(network.buses)

#add three lines in a ring
for i in range(3):
    network.add("Line","My line {}".format(i),
                bus0="My bus {}".format(i),
                bus1="My bus {}".format((i+1)%3),
                x=0.0001,
                s_nom=60)

print(network.lines)

#add a generator at bus 0
network.add("Generator","My gen 0",
            bus="My bus 0",
            p_nom=100,
            marginal_cost=50)

#add a generator at bus 1
network.add("Generator","My gen 1",
            bus="My bus 1",
            p_nom=100,
            marginal_cost=25)

print(network.generators)

print(network.generators.p_set)

#add a load at bus 2
network.add("Load","My load",
            bus="My bus 2",
            p_set=100)

print(network.loads)

print(network.loads.p_set)

#Do a linear OPF

def my_f(network,snapshots):
    print(snapshots)


network.lopf(extra_functionality=my_f)

print(network.generators_t.p)

print(network.lines_t.p0)

print(network.buses_t.v_ang*180/np.pi)

print(network.buses_t.v_mag_pu)
