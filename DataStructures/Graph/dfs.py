from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import vertex as V
from DataStructures.Graph import digraph as G
from DataStructures.Stack import stack

def dfs(graph, source):
    
    visited_ht = mp.new_map(G.order(graph), load_factor= 0.5)
    visited_ht = mp.put(visited_ht, source, {'marked': True, 'edge_from': None})
    dfs_vertex(graph, source, visited_ht)
    return visited_ht

def dfs_vertex(graph, vertex, visited_ht):
    
    adj = G.adjecents(graph, vertex)
    for vert in adj:
        value = mp.get(visited_ht, vert)
        if not value:
            visited_ht = mp.put(visited_ht, vert, {'marked': True, 'edge_from': vertex})
            dfs_vertex(graph, vert, visited_ht)

def has_path_to(vertex, visited_ht):
    
    value = mp.get(visited_ht, vertex)
    if not value:
        return False
    
    return value['marked']

def path_to(vertex, visited_ht):
    
    if not has_path_to(vertex, visited_ht):
        return None
    
    path = stack.new_stack()
    while vertex != None:
        value = mp.get(visited_ht, vertex)
        vertex_v = value['edge_from']
        stack.push(path, vertex_v)
        vertex = vertex_v
    
    return path