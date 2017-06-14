import networkx as nx
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np 
from scipy.spatial import distance

file_name2 = 'networkinfo.txt'
handle = open(file_name2)
network = nx.Graph()
for line in handle:
	line = line.strip().split('\t')
	if len(line)==1:
		network.add_node(float(line[0]))
	else:
		network.add_edge(float(line[0]),float(line[1]))

handle.close()


degrees = []
for node in network.nodes():
	degrees.append(nx.degree(network)[node])

unique = list(set(degrees))
distribution = []
for number in unique:
	distribution.append(degrees.count(number))
distribution = np.log(distribution)
distribution = list(distribution)

line = plt.figure()
plt.plot(unique,distribution,"o")
plt.title('scatterplot of degree distribution')
plt.xlabel('degree of a node')
plt.ylabel('log frequency')
plt.savefig('scatterplot.png')

handle = open('clusterinfo9.txt').readlines()
clustering = []
handle = handle[0]
for i in handle:
	clustering.append(int(i))


#spring layout
#toDelete = []
#toKeep = []
#for i in range(0,len(network.nodes())):
#	if degrees[i] < 3:
#		toDelete.append(i)
#	else: 
#		toKeep.append(i)

#nodesDel = [network.nodes()[i] for i in toDelete]
subnetwork = nx.Graph(network.edges()[:200])
#subnetwork.remove_nodes_from(nodesDel)

unique =  list(set(clustering))
color_codes = {0:'b',1:'g',2:'r',3:'c',4:'m',5:'y',6:'k',7:'w'}
for j in range(0,len(clustering)):
	 clustering[j] = color_codes[clustering[j]]

subclustering = [clustering[int(i)] for i in subnetwork.nodes()]
line = plt.figure()
nx.draw( subnetwork, pos=nx.spring_layout(subnetwork), node_color = subclustering, with_labels=False, node_size = 30)
plt.draw()
plt.savefig('network2.png')