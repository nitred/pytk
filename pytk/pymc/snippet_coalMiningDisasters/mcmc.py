"""This module calls applies the MCMC algorithm on the model file."""
from matplotlib import pyplot as plt
from pymc.Matplot import plot
from pymc import MCMC
import model

# initialize model
M = MCMC(model)

# apply mcmc on the model
M.sample(iter=10000, burn=1000, thin=10)

# trace of switchpoint (can be used to plot)
switchpoint_trace = M.trace('switchpoint')[:]

# final plot of all variables
plot(M)
plt.show()
