from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import vertex as v
from DataStructures.Graph import edge as e

def new_graph(order):
    return {
        'vertices': mp.new_map(order, 0.5),
        'num_edges': 0
    }

def insert_vertex(graph, key, info):
    vert = graph['vertices']
    mp.put(vert, key, v.new_vertex(key, info))
    return graph

def add_edge(graph, key_o, key_f, weight=1):
    vert = graph['vertices']
    vertex_o = mp.get(vert, key_o)
    vertex_f = mp.get(vert, key_f)
    if not vertex_o or not vertex_f:
        raise Exception("El vertice u no existe")
    
    v.add_adjacent(vertex_o, key_f, weight)
    graph['num_edges'] += 1
    
    return graph

def contains_vertex(graph, key):
    vert = graph['vertices']
    return mp.contains(vert, key)

def order(graph):
    return mp.size(graph['vertices'])

def size(graph):
    return graph['num_edges']

def degree(graph, key):
    vert = graph['vertices']
    vertex = mp.get(vert, key)
    if not vertex:
        raise Exception("El vertice u no existe")
    
    return v.degree(vertex)

def adjecents(graph, key):
    vert = graph['vertices']
    vertex = mp.get(vert, key)
    if not vertex:
        raise Exception("El vertice u no existe")
    
    adjecents = v.get_adjacents(vertex)
    adj_keys = mp.key_set(adjecents)
    
    return adj_keys['elements']

def vertices(graph):
    vert = graph['vertices']
    return mp.key_set(vert)

def edges_vertex(graph, key):
    vert = graph['vertices']
    vertex = mp.get(vert, key)
    if not vertex:
        raise Exception("El vertice u no existe")
    
    ret = []
    adj_map = v.get_adjacents(vertex)
    adj_keys = adjecents(graph, key)
    for arc in adj_keys:
        info = mp.get(adj_map, arc)
        ret.append((key, info[0], info[1]))
    
    return ret