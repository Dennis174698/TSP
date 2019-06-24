#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import random
import fun


# In[ ]:


# read map
XY = np.random.randint(1,100,(20,2))    #20 dots with (x,y)
N = XY.shape[0]                         


# In[ ]:


# Perameters of ACO
MaxGen=100 #Iteration
popsize=20 #population of ants
alpha=4    #α
beta=1     #β
rho=0.5    #ρ
Q=5        #q
#acoValues = np.zeros([MaxGen * popsize, 2])   # 


# Set up map and perameters of ACO

# In[ ]:


# distance
dmat=np.zeros([N,N])

for i in range(0,N-1):
    for j in range(i+1,N):
        d=np.linalg.norm(XY[i,:]-XY[j,:])   #sqrt((x1-x2)²+(y1-y2)²))
        dmat[i,j]=d                         
        dmat[j,i]=d                         #generate the distance between every dots
temp = dmat.copy()
dmat[temp==0.0] = np.spacing(1)             #


# Count distance between nodes

# In[ ]:


# Herustic value
Eta=np.zeros([N,N])
for i in range(N):
    for j in range(N):
        Eta[i,j]=1/(dmat[i,j]) 
        
index0 = np.arange(0,N)
Tau=np.ones([N,N])*0.1            # Initiate pheromone map
tracemataco=np.zeros([MaxGen,2])    


# Set up herustic value
# 

# In[ ]:


# ACOmap
for gen in range(0,MaxGen):                   #Iteration
    RouteData=np.zeros([popsize,N])
    for m in range(0,popsize):
        OpNodeSetLocal=index0                 
        Route=np.random.randint(0,N-1,[1,1]) #Initiate start point 
        currNode=Route[-1]
        temp = OpNodeSetLocal.tolist()        #array to list
        temp.remove(currNode)               
        OpNodeSetLocal = np.array(temp)      #list to array
        
        while len(OpNodeSetLocal)!= 0:
            long1=len(OpNodeSetLocal)
            P=np.zeros([long1,1])
            # Probability of choosing next city
            for i in range(long1):
                tempnextnode=OpNodeSetLocal[i]
                P[i]=(Tau[currNode,tempnextnode]**alpha)*(Eta[currNode,tempnextnode]**beta)     #𝑠𝑐𝑜𝑟𝑒 = 𝑝ℎ𝑒𝑟𝑜𝑚𝑜𝑛𝑒𝛼**α ∗ ℎ𝑒𝑢𝑟𝑖𝑠𝑡𝑖𝑐**β
            P = P/sum(P)                                         
            Pc = np.cumsum(P)                                    #Pc[i]=P[i]+P[i-1]+..+P[0]

            rand = np.random.rand()                              #random number(0,1)
            index02 = np.argwhere(Pc >= rand)                    #returns the indices where Pc[i]>=rand  
            next_node = OpNodeSetLocal[index02[0]]               #choosing nextnode
            Route=np.append(Route,next_node)                     #update nodes
            currNode=Route[-1]                                   
            temp = OpNodeSetLocal.tolist()                          
            temp.remove(currNode)
            OpNodeSetLocal = np.array(temp)                      #remove currNode
            
        RouteData[m,:]=Route                                     #The ants' visiting sequence
        
        
#%%
    cost= fun.decodingFun(RouteData,popsize,dmat,N)              #calculate the cost of every route
    v1 = np.min(cost)                                            #find the minimum cost of the routes
    index1 = np.where(cost == v1)[0]                             
    #for k in range(len(cost)):
    #   acoValues[gen * k, 1]= cost[k]                           #update acoValues
        
    bestRoute=RouteData[index1,:]                                #find the best route of every iteration
    costu = fun.mapminmax(cost,100,200)                          #Normalise the scores into the range [100, 200].
    
    
#%%
    detaTau=np.zeros([N,N])
    for m in range(popsize):
        Route=RouteData[m,:]
        for i in range(0,N-2):
            node1=int(Route[i])
            node2=int(Route[i+1])
            detaTau[node1,node2]=Q/costu[m]                     #𝑞 / 𝑠𝑐𝑎𝑙𝑒𝑑 𝑠𝑐𝑜𝑟𝑒 pheromone to each path on the route
    Tau=Tau*(1-rho)+detaTau
#%%
    if (gen==0):
        bestroute=RouteData[int(index1),:]
        bestvalueaco=v1
    if (bestvalueaco>v1):
        bestvalueaco=v1                                        #best value of every iteration
        bestroute=RouteData[int(index1),:]
    tracemataco[gen,0]=bestvalueaco                            # Keep the best value
    tracemataco[gen,1]=np.mean(cost)                           # mean value


# In[ ]:


#%%        
plt.plot(tracemataco[:,0],'r-')
plt.plot(tracemataco[:,1],'b-')
plt.savefig('exp01.jpg')

fun.drawroutetsp(XY,bestroute)
for i in range(XY.shape[0]):
    plt.text(XY[i,0],XY[i,1],str(i))
    plt.savefig('exp02.jpg')
  
   


# In[ ]:




