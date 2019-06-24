# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#function cost= decodingFun(RouteData,antNumber,dmat,N)
def mapminmax(cost, lower, upper):
    costmax = np.max(cost)
    costmin = np.min(cost)
    costmm = (upper-lower)/(costmax - costmin)*cost - (upper-lower)/(costmax - costmin)*costmax + upper
    
    return costmm

def decodingFun(RouteData,popsize,dmat,N):
    cost=np.zeros([popsize,1]);
    for m in range(popsize):
        route=RouteData[m,:];
        y=0;
        for i in range(N-1): 
            y=y+dmat[int(route[i]),int(route[i+1])];
        cost[m]=y;
    return cost    

def drawroutetsp(XY,route):
    fig2 = plt.figure('RouteStep')
    plt.show()
    N = len(route)
    plt.scatter(XY[:,0],XY[:,1])
#    for i in range(XY.shape[0]):
#        plt.text(XY[:,0],XY[:,1],str(i))
#    
#    #plt.plot([XY[int(route[0]),0], XY[int(route[N-1]),0]], [XY[int(route[0]),1], XY[int(route[N-1]),1]])
#    
    for j in range(0,N):
        plt.plot([XY[int(route[j-1]),0], XY[int(route[j]),0]], [XY[int(route[j-1]),1], XY[int(route[j]),1]])