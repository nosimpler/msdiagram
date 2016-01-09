import matplotlib as mpl
import numpy as np
def cmviz(gbar, p, E, V, ax, offset = 0, label = True):
    #TODO: more colors
    colors = ['b','r','g']
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
            rmin = sqrt(V)
            rmax = sqrt(e)

        else:
            rmin = sqrt(e)
            rmax = sqrt(V)

        scale = sqrt(V)
        r_pt = rmax - rmin
        #plot
        ax.bar(left, scale, width = width, bottom = 0, color = 'white',
                edgecolor = 'black', linewidth = 1)
        ax.bar(openleft, r_pt, width = openwidth, bottom = rmin,
                color = colors[i], linewidth = 0)
        ax.set_yticks([])
        ax.set_xticks([])
        ax.spines['polar'].set_visable(False)
#TODO: automate labeling of figures
        #if label == True:
        #    ax.text(center, scale*
