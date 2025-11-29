from DataStructures.Map import map_linear_probing as mp
from DataStructures.Priority_queue import priority_queue as pq
from DataStructures.Graph import digraph as G
from DataStructures.List import array_list as lt
import math


def new_dijsktra_structure(source, g_order):
    """

    Crea una estructura de busqueda usada en el algoritmo **dijsktra**.

    Se crea una estructura de busqueda con los siguientes atributos:

    - **source**: Vertice de origen. Se inicializa en ``source``
    - **visited**: Mapa con los vertices visitados. Se inicializa en ``None``
    - **pq**: Cola indexada con los vertices visitados. Se inicializa en ``None``

    :returns: Estructura de busqueda
    :rtype: dijsktra_search
    """
    structure = {
        "source": source,
        "visited": mp.new_map(
            g_order, 0.5),
        "pq": pq.new_heap()}
    return structure

def init_structure(graph, source):
    
    struc = new_dijsktra_structure(source, G.order(graph))
    vertices = G.vertices(graph)
    for i in range(lt.size(vertices)):
        vert = lt.get_element(vertices, i)
        mp.put(struc['visited'], vert, {'marked': False, 'edge_from': None, 'dist_to': math.inf})
    
    mp.put(struc['visited'], source, {'marked': False, 'edge_from': None, 'dist_to': 0})
    pq.insert(struc['pq'], 0.0, source)
    return struc