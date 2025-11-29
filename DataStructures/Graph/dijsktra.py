from DataStructures.Graph import dijsktra_structure as dst
from DataStructures.Priority_queue import priority_queue as pq
from DataStructures.Graph import digraph as G
from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import vertex as v
from DataStructures.Stack import stack
import math
    

def dijkstra(graph, source):
    struc = dst.init_structure(graph, source)
    visited = struc['visited']
    prq = struc['pq']
    if not G.contains_vertex(graph, source):
        return None
    
    while not pq.is_empty(prq):
        vert_key = pq.remove(prq)
        val = mp.get(visited, vert_key)
        vert = G.get_vertex(graph, vert_key)
        val['marked'] = True
        mp.put(visited, vert_key, val)
        adj = G.adjecents(graph, vert_key)
        for ve in adj:
            ad_ve = G.get_vertex(graph, ve)
            ad_value = mp.get(visited, ve)
            if ad_value['marked']:
                continue
            if v.get_edge(vert, ve)['weight'] + val['dist_to'] < ad_value['dist_to']:
                ad_value['edge_from'] = vert_key
                ad_value['dist_to'] = v.get_edge(vert, ve)['weight'] + val['dist_to']
                pq_pos_ad_ve = pq.is_present_value(prq, ve)
                if pq_pos_ad_ve != -1:
                    pq.improve_priority_set_amount(prq, ad_value['dist_to'], ve)
                else:
                    pq.insert(prq, ad_value['dist_to'], ve)
        
    return struc

def has_path_to(vertex, struc):
    visited = struc['visited']
    ele = mp.get(visited, vertex)
    return ele['marked']

def path_to(vertex, struc):
    if not has_path_to(vertex, struc):
        return None
    
    visited = struc['visited']
    
    camino = stack.new_stack()
    while vertex is not None:
        stack.push(camino, vertex)
        vertex = mp.get(visited, vertex)['edge_from']

    return camino

def dist_to(key_v, struc):
    
    if not has_path_to(struc, key_v):
        return math.inf
    
    visited = struc['visited']
    value = mp.get(visited, key_v)
    coste_t = value['dist_to']
        
    return coste_t