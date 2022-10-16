import networkx as nx
import matplotlib.pyplot as plt

#Graphical implementation of Madaraka Estate Network
G = nx.Graph()
nodes=["SportComplex","Siwaka","Ph.1A","Ph.1B","STC","Phase2","Phase3","J1","Mada","ParkingLot"]
G.add_nodes_from(nodes)
G.nodes()

#Add Edges and their weights
G.add_edge("SportComplex","Siwaka",weight="450")
G.add_edge("Siwaka","Ph.1A",weight="10")
G.add_edge("Siwaka","Ph.1B",weight="230")
G.add_edge("Ph.1A","Ph.1B",weight="100")
G.add_edge("Ph.1A","Mada",weight="850")
G.add_edge("Ph.1B","STC",weight="50")
G.add_edge("Ph.1B","Phase2",weight="112")
G.add_edge("STC","Phase2",weight="50")
G.add_edge("STC","ParkingLot",weight="250")
G.add_edge("Phase2","J1",weight="600")
G.add_edge("J1","Mada",weight="200")
G.add_edge("Mada","ParkingLot",weight="700")
G.add_edge("Phase2","Phase3",weight="500")
G.add_edge("Phase3","ParkingLot",weight="350")

#Position the nodes accordingly
G.nodes["SportComplex"]['pos']=(1,5)
G.nodes["Siwaka"]['pos']=(5,5)
G.nodes["Ph.1A"]['pos']=(8,5)
G.nodes["Ph.1B"]['pos']=(8,4)
G.nodes["Phase2"]['pos']=(12,4)
G.nodes["STC"]['pos']=(8,3)
G.nodes["Phase3"]['pos']=(15,3)
G.nodes["ParkingLot"]['pos']=(17,2)
G.nodes["J1"]['pos']=(15,4)
G.nodes["Mada"]['pos']=(18,4)

#Store all positions in a variable
node_pos = nx.get_node_attributes(G,'pos')
arc_weight=nx.get_edge_attributes(G,'weight')

#graph output
print(nx.info(G))
nx.draw(G, node_pos, with_labels=1)
nx.draw_networkx_edge_labels(G, node_pos,edge_labels=arc_weight)
plt.show()