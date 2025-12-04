# App/logic.py
from DataStructures.Graph import digraph as G
from DataStructures.Graph import prim as prim

# Crear un grafo No dirigido
my_graph = G.new_graph(6)

# Agregar vértices con su información
G.insert_vertex(my_graph, "Bogotá", {"nombre": "Bogotá", "poblacion": 7400000})
G.insert_vertex(my_graph, "Medellín", {"nombre": "Medellín", "poblacion": 2600000})
G.insert_vertex(my_graph, "Cali", {"nombre": "Cali", "poblacion": 2300000})
G.insert_vertex(my_graph, "Barranquilla", {"nombre": "Barranquilla", "poblacion": 1300000})
G.insert_vertex(my_graph, "Cartagena", {"nombre": "Cartagena", "poblacion": 1000000})
G.insert_vertex(my_graph, "Londres", {"nombre": "Londres", "poblacion": 8866000})

# Agregar aristas con distancias
G.add_edge(my_graph, "Bogotá", "Medellín", 415)
G.add_edge(my_graph, "Medellín", "Bogotá", 415)
G.add_edge(my_graph, "Bogotá", "Cali", 468)
G.add_edge(my_graph, "Cali", "Bogotá", 468)
G.add_edge(my_graph, "Medellín", "Cali", 412)
G.add_edge(my_graph, "Cali", "Medellín", 412)
G.add_edge(my_graph, "Medellín", "Barranquilla", 738)
G.add_edge(my_graph, "Barranquilla", "Medellín", 738)
G.add_edge(my_graph, "Cali", "Barranquilla", 1020)
G.add_edge(my_graph, "Barranquilla", "Cali", 1020)
G.add_edge(my_graph, "Barranquilla", "Cartagena", 120)
G.add_edge(my_graph, "Cartagena", "Barranquilla", 120)

# Ejecutar algoritmo de Prim desde Bogotá
structure = prim.prim_mst(my_graph, "Bogotá")
weight = prim.weight_mst(my_graph, structure)
print ("Peso del MST: " + str(weight))
