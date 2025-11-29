# App/logic.py
from DataStructures.Graph import digraph as G
from DataStructures.Graph import dijsktra as dijk

# Crear un grafo
my_graph = G.new_graph(1)

# Agregar vértices con su información
G.insert_vertex(my_graph, "Bogotá", {"nombre": "Bogotá", "poblacion": 7400000})
G.insert_vertex(my_graph, "Medellín", {"nombre": "Medellín", "poblacion": 2600000})
G.insert_vertex(my_graph, "Cali", {"nombre": "Cali", "poblacion": 2300000})
G.insert_vertex(my_graph, "Barranquilla", {"nombre": "Barranquilla", "poblacion": 1300000})
G.insert_vertex(my_graph, "Cartagena", {"nombre": "Cartagena", "poblacion": 1000000})
G.insert_vertex(my_graph, "Londres", {"nombre": "Londres", "poblacion": 8866000})

# Agregar aristas con distancias
G.add_edge(my_graph, "Bogotá", "Medellín", 415)
G.add_edge(my_graph, "Bogotá", "Cali", 468)
G.add_edge(my_graph, "Medellín", "Cali", 412)
G.add_edge(my_graph, "Medellín", "Barranquilla", 738)
G.add_edge(my_graph, "Cali", "Barranquilla", 1020)
G.add_edge(my_graph, "Barranquilla", "Cartagena", 120)

# Ejecutar algoritmo de Dijkstra desde Bogotá
structure = dijk.dijkstra(my_graph, "Bogotá")
print(structure)