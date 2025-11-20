from DataStructures.List import array_list as lt
from DataStructures.Map import map_linear_probing as mp
from DataStructures.Map import map_separate_chaining as sc
from DataStructures.Tree import binary_search_tree as bst
from DataStructures.Tree import red_black_tree as rbt
from DataStructures.Tree import rbt_node as rbtn
from DataStructures.Tree import tree_traversal as trav
from DataStructures.Priority_queue import priority_queue as pq
from DataStructures.Graph import digraph as G
from DataStructures.Graph import vertex as V
import logic

my_graph = G.new_graph(1)

# Inserta vértices
my_graph = G.insert_vertex(my_graph, "Pasto", {"nombre": "Pasto", "poblacion": 400000})
my_graph = G.insert_vertex(my_graph, "Ibague", {"nombre": "Ibague", "poblacion": 500000})
my_graph = G.insert_vertex(my_graph, "Monteria", {"nombre": "Monteria", "poblacion": 300000})

# Inserta arcos
my_graph = G.add_edge(my_graph, "Pasto", "Ibague", 120)
my_graph = G.add_edge(my_graph, "Pasto", "Monteria", 250)

# # Consulta de arcos salientes del vértice 'Pasto'
# edges = G.edges_vertex(my_graph, "Pasto")
# for edge in edges:
#     print(edge)