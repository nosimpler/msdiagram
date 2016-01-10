from msdiagram import msdiagram
from matplotlib import pyplot as plt
import os
gbar = [1.0, 2.0]
p = [0.5, 0.3]
E = [5.0, 95.0]
V = 50
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
ax = msdiagram(gbar, p, E, V, ax)
print os.path
savefile = 'test.eps'
plt.savefig(savefile)
