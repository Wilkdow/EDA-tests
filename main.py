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
from DataStructures.Graph import bfs as BFS
from DataStructures.Graph import dfs as DFS
import logic

my_graph = G.new_graph(1)

# Agregar vértices
my_graph = G.insert_vertex(my_graph, "A", {"nombre": "A"})
my_graph = G.insert_vertex(my_graph, "B", {"nombre": "B"})
my_graph = G.insert_vertex(my_graph, "C", {"nombre": "C"})
my_graph = G.insert_vertex(my_graph, "D", {"nombre": "D"})
my_graph = G.insert_vertex(my_graph, "E", {"nombre": "E"})

# Agregar aristas
my_graph = G.add_edge(my_graph, "A", "B", 1)
my_graph = G.add_edge(my_graph, "A", "C", 1)
my_graph = G.add_edge(my_graph, "B", "D", 1)
my_graph = G.add_edge(my_graph, "C", "E", 1)
my_graph = G.add_edge(my_graph, "D", "E", 1)

# Realizar BFS desde el vértice A
visited_map = BFS.bfs(my_graph, "A")

# Verificar los vértices visitados
print("Vértices visitados desde A:")
vertices = G.vertices(my_graph)
for i in range(lt.size(vertices)):
    vertex = lt.get_element(vertices, i)
    if mp.contains(visited_map, vertex):
        info = mp.get(visited_map, vertex)
        print(f"Vértice {vertex}:")
        print(f"  - Distancia: {info['dist_to']}")
        print(f"  - Viene de: {info['edge_from']}")
