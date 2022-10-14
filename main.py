import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

#graphical representation of Madaraka estate network
G.add_node('SportComplex')
G.add_node('Siwaka')
G.add_node('PH.1A')
G.add_node('PH.1B')
G.add_node('STC')
G.add_node('Phase2')
G.add_node('J1')
G.add_node('Mada')
G.add_node('Phase3')
G.add_node('ParkingLot')

G.add_edge('SportComplex', 'Siwaka') ('Siwaka', 'PH.1A') 
G.add_edge('Siwaka', 'PH.1B')
G.add_edge('PH.1A', 'PH.1B')
G.add_edge('PH.1A', 'Mada')
G.add_edge('Mada', 'ParkingLot')
G.add_edge('ParkingLot', 'STC')
G.add_edge('PH.1B', 'Phase2')
G.add_edge('PH.1B', 'STC')
G.add_edge('Phase2', 'STC')
G.add_edge('Phase2', 'J1')
G.add_edge('Phase3', 'Phase2')
G.add_edge('Phase3', 'ParkingLot')

G.nodes["SportComplex"]['pos']=(1,5)
G.nodes["Siwaka"]['pos']=(5,5)
G.nodes["PH.1A"]['pos']=(8,5)
G.nodes["PH.1B"]['pos']=(8,4)
G.nodes["STC"]['pos']=(8,3)
G.nodes["Phase2"]['pos']=(12,4)
G.nodes["J1"]['pos']=(15,4)
G.nodes["Mada"]['pos']=(18,4)
G.nodes["Phase3"]['pos']=(15,3)
G.nodes["ParkingLot"]['pos']=(17,2)



print(nx.info(G))

nx.draw(G, with_labels=1)
plt.show()