from DataStructures.Graph import dijsktra_structure as dst
from DataStructures.Priority_queue import priority_queue as pq
from DataStructures.Graph import digraph as G
from DataStructures.Map import map_linear_probing as mp
from DataStructures.List import array_list as lt
from DataStructures.Graph import vertex as v

def prim_mst(graph, source):
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
            if v.get_edge(vert, ve)['weight']  < ad_value['dist_to']:
                ad_value['edge_from'] = vert_key
                ad_value['dist_to'] = v.get_edge(vert, ve)['weight']
                pq_pos_ad_ve = pq.is_present_value(prq, ve)
                if pq_pos_ad_ve != -1:
                    pq.improve_priority_set_amount(prq, ad_value['dist_to'], ve)
                else:
                    pq.insert(prq, ad_value['dist_to'], ve)
        
    return struc

def edges_mst(graph, struc):
    visited = struc['visited']
    keys = mp.key_set(visited)
    edges = lt.new_list()
    
    for i in range(lt.size(keys)):
        key = lt.get_element(keys, i)
        val = mp.get(visited, key)
        if val['edge_from'] == None:
            continue
        lt.add_last(edges, {'edge_from': val['edge_from'], 'to': key, 'dist_to': val['dist_to']})
        
    return edges

def weight_mst(graph, struc):
    edges = edges_mst(graph, struc)
    weight = 0
    for i in range(lt.size(edges)):
        edge = lt.get_element(edges, i)
        weight += edge['dist_to']
    return weight