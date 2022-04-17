import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from pyecharts import options as opts
from graphviz import Digraph
from matplotlib import pyplot as plt
import PIL
file='input.txt'
with open(file) as fp:
    data=fp.readlines()
data=[int(item) for item in data]
data.sort(reverse=False)
n=len(data)
connect=[[0 for i in range(n)] for i in range(n)]
ind=[0 for i in range(n)]
flg=[0 for i in range(n)]
for i in range(0,n,1):
    for j in range(i+1,n,1):
        if data[j]%data[i]==0:
            connect[i][j]=1
            ind[j]=ind[j]+1
for i in range(n):
    for j in range(n):
        if i==j:
            pass
        else:
            for k in range(n):
                if i==k or j==k:
                    pass
                else:
                    if connect[i][k] and connect[k][j]:
                        connect[i][j]=0
max(ind)
height=[0 for i in range(n)]
for i in range(n):
    for j in range(n):
        if connect[i][j]:
            height[j]=height[i]+1
nums=[0 for i in range(n)]
node_id=[0 for i in range(n)]
for i in range(n):
    nums[height[i]]+=1
    node_id[i]=nums[height[i]]
pos={}
for i in range(n):
    item={data[i]:(n/(nums[height[i]]+1)*node_id[i],height[i])}
    pos.update(item)
G=nx.Graph()
G.add_nodes_from(data)
for i in range(0,n,1):
    for j in range(i+1,n,1):
        if connect[i][j]:
            G.add_edge(data[i],data[j])
nx.draw(G,with_labels=True,pos=pos,arrows=False)
plt.show()