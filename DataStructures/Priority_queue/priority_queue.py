from DataStructures.Priority_queue import pq_entry as pqe
from DataStructures.List import array_list as lt


def new_heap(is_min_pq=True):
    
    if is_min_pq == True:
        cmp_function = default_compare_lower_value
    else:
        cmp_function = default_compare_higher_value
    
    new_h = {
       "elements" : lt.new_list(),
       "size" : 0,
       "cmp_function" : cmp_function 
       }
    
    lt.add_last(new_h['elements'], None)
    
    return new_h

def size(my_heap):
    return my_heap["size"]

def is_empty(my_heap):
    if size(my_heap) == 0: 
        return True 
    else:
        return False
    

def default_compare_higher_value(father_node, child_node):
    if pqe.get_priority(father_node) >= pqe.get_priority(child_node):
        return True
    return False

def default_compare_lower_value(father_node, child_node):
    if pqe.get_priority(father_node) <= pqe.get_priority(child_node):
        return True
    return False


def priority(heap,parent, child):
    compare = heap['cmp_function']
    if compare == default_compare_higher_value:
        return default_compare_higher_value(parent, child)
    else: 
        return default_compare_lower_value(parent, child)
    
def exchange(heap, parent_pos, child_pos):
    heap_list = heap['elements']
    lt.exchange(heap_list, parent_pos, child_pos)
    return heap
    
def swim(heap, pos):
    if pos <= 1:
        return heap

    heap_list = heap['elements']
    child = lt.get_element(heap_list, pos)
    parent = lt.get_element(heap_list, pos // 2)
    
    if not priority(heap, parent, child):
        exchange(heap, pos // 2, pos)
    
    swim(heap, pos//2)

def insert(heap, priority, value):
    entry = pqe.new_pq_entry(priority, value)
    s = size(heap)
    heap_list = heap['elements']
    lt.add_last(heap_list, entry)
    heap['size'] += 1
    swim(heap, s)
    return heap

def sink(heap, pos):
    heap_list = heap['elements']
    parent = lt.get_element(heap_list, pos)
    child_1 = lt.get_element(heap_list, pos*2)
    child_2 = lt.get_element(heap_list, pos*2 + 1)
    
    if parent == None or (child_1 and child_2) == None:
        return heap
    
    if priority(heap, parent, child_1):
        exchange(heap, pos, pos * 2)
    
    if priority(heap, parent, child_2):
        exchange(heap, pos, pos * 2 + 1)
        
    sink(heap, pos * 2)
    sink(heap, pos * 2 + 1)

def remove(heap):
    if is_empty(heap):
        return None
    
    heap_list = heap['elements']
    ele = lt.get_element(heap_list, 1)
    lt.delete_element(heap_list, 1)
    heap['size'] -= 1
    sink(heap, 1)
    return pqe.get_value(ele)

def get_first_priority(heap):
    if is_empty(heap):
        return None
    
    heap_list = heap['elements']
    ele = lt.get_element(heap_list, 1)
    
    return pqe.get_value(ele)