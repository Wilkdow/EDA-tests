from DataStructures.Graph import digraph as G
from DataStructures.Graph import vertex as V
from DataStructures.Map import map_linear_probing as mp
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack

def bfs(graph, source):
    
    visited_ht = mp.new_map(G.order(graph), load_factor=0.5)
    bfs_vertex(graph, source, visited_ht)
    return visited_ht

def bfs_vertex(graph, source, visited_ht):
    
    cola = q.new_queue()
    q.enqueue(cola, source)
    visited_ht = mp.put(visited_ht, source, {'marked': True, 'edge_from': None, 'dist_to': 0})
    
    while not q.is_empty(cola):
        vertex = q.dequeue(cola)
        adj = G.adjecents(graph, vertex)
        for v in adj:
            val = mp.get(visited_ht, v)
            if val != None and val['marked']:
                continue
            q.enqueue(cola, v)
            distance = mp.get(visited_ht, vertex)['dist_to']
            visited_ht = mp.put(visited_ht, v, {'marked': True, 'edge_from': vertex, 'dist_to': distance + 1})

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