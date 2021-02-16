#%% Function definition

import numpy as np
import matplotlib.pyplot as mpl
import matplotlib.animation as animation


class Bodies:
    def __init__(self, mass, posv, velv, disv):
        self.M=mass                             # Mass of the body
        self.pos=np.array(posv,dtype='float64') # Initial position vector
        self.vel=np.array(velv,dtype='float64') # Initial velocity vector
        self.dis=np.array(disv,dtype='float64') # Distance between bodies
        self.posa=self.pos
        self.vela=self.vel
        
#%% Initialising the parameters

B1=Bodies(1, [0.3361300950,0.0000000000],  [0.0000000000,1.5324315370],  [2, 1])
B2=Bodies(1, [0.7699893804,0.0000000000],  [0.0000000000,-0.6287350978], [2, 2])
B3=Bodies(1, [-1.1061194753,0.000000000],  [0.0000000000,-0.9036964391], [2, 1])

h=0.001 # step size
steps=10000 # total number of steps

#%% Main Loop

for i in range(steps):
    for (b1,b2,b3) in [(B1,B2,B3),(B2,B1,B3),(B3,B1,B2)]:
        b1.pos+=0.5*h*b1.vel
    
        b1.dis=b1.pos-b2.pos
        r12=np.sqrt(b1.dis[0]**2 + b1.dis[1]**2)
        b1.dis=b1.pos-b3.pos
        r13=np.sqrt(b1.dis[0]**2 + b1.dis[1]**2)
    
        b1.vel+=h*(-1*(b2.M)*(b1.pos-b2.pos)/r12**3) + h*(-1*(b3.M)*(b1.pos-b3.pos)/r13**3)
        b1.pos+= 0.5*h*b1.vel
        b1.posa=np.vstack((b1.posa,b1.pos))
        b1.vela=np.vstack((b1.vela,b1.vel))
        
#%% Animation/Plotting

ANIMATE=True
if ANIMATE:
    
    fig=mpl.figure()
    mpl.grid()
    xm=max([max(b1.posa[:,0]),max(b2.posa[:,0]),max(b3.posa[:,0])]) + 1
    ym=max([max(b1.posa[:,1]),max(b2.posa[:,1]),max(b3.posa[:,1])]) + 1   
    ax=mpl.axis([-xm,xm,-ym,ym])
    
    dot1,dot2,dot3 = mpl.plot(0,0,'ro',markersize=15)[0],\
                     mpl.plot(0,0,'go',markersize=15)[0],\
                     mpl.plot(0,0,'bo',markersize=15)[0]
    
    lin1,lin2,lin3 = mpl.plot([0],[0],'r-')[0],\
                     mpl.plot([0],[0],'g-')[0],\
                     mpl.plot([0],[0],'b-')[0]

    def animate(i):
        dot1.set_data(b1.posa[i,0],b1.posa[i,1])
        dot2.set_data(b2.posa[i,0],b2.posa[i,1])
        dot3.set_data(b3.posa[i,0],b3.posa[i,1])
        
        lin1.set_data(b1.posa[0:i,0],b1.posa[0:i,1])
        lin2.set_data(b2.posa[0:i,0],b2.posa[0:i,1])
        lin3.set_data(b3.posa[0:i,0],b3.posa[0:i,1])
        return dot1,dot2,dot3,lin1,lin2,lin3
    anim=animation.FuncAnimation(fig,animate,interval=0.001,
                                 frames=list(range(0,steps,int(steps/300))),
                                 save_count=300,repeat=False)
else:
    mpl.grid()
    mpl.plot(b1.posa[:,0],b1.posa[:,1],'r-')
    mpl.plot(b2.posa[:,0],b2.posa[:,1],'g-')
    mpl.plot(b3.posa[:,0],b3.posa[:,1],'b-')
    


    
    
