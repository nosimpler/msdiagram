import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
#All input values should be floats
#Membrane state diagram as per Law and Levin, 2015
#and described in Law and Jones (2016, bioRxiv)
def msdiagram(gbar, p, E, V, ax, offset = 0, colors = None):
    
    if colors == None:
        n_currents = len(gbar)
        colors = plt.cm.Set1(np.linspace(0,1,n_currents))
    #gp as fraction of total gbar
    gp = gbar/np.sum(gbar)
    #get boundary angles for gbar
    theta_bounds = ([0.0]+list(np.cumsum(gp)*2*np.pi))
    theta_diffs = zip(theta_bounds[0:-1:1], theta_bounds[1::])
    
    #shift voltages
    minV = min([V]+E)
    V = V - minV + offset
    E = [e - minV + offset for e in E]
    
    
    for i, th in enumerate(theta_diffs):
        #get boundary angles for g_i, centered
        width = th[1] - th[0]
        left = th[0]
        right = th[1]
        center = (th[0] + th[1]) / 2

        openleft = center + p[i]*(left - center)
        openright = center + p[i]*(right - center)
        openwidth = openright - openleft

        e = E[i]
        #set radial bounds
        if V > E:
            rmin = np.sqrt(V)
            rmax = np.sqrt(e)

        else:
            rmin = np.sqrt(e)
            rmax = np.sqrt(V)

        scale = np.sqrt(V)
        r_pt = rmax - rmin
        #plot
        ax.bar(left, scale, width = width, bottom = 0, color = 'white',
                edgecolor = 'black', linewidth = 1)
        ax.bar(openleft, r_pt, width = openwidth, bottom = rmin,
                color = colors[i], linewidth = 0)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.spines['polar'].set_visible(False)
    return ax

if __name__ == '__main__':
    from matplotlib import pyplot
    gbar = [10., 20.]
    p = [0.8, 0.4]
    E = [50., -50.]
    V = 0.
    offset = 10.
    fig = pyplot.figure()
    ax = fig.add_subplot(111, projection='polar')
    ax = msdiagram(gbar, p, E, V, ax, offset)
    pyplot.show()
#TODO: automate labeling of figures
        #if label == True:
        #    ax.text(center, scale*
