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
    heap_list = lt.exchange(heap_list, parent_pos, child_pos)
    return heap

def swim(heap, pos):
    heap_list = heap['elements']
    while pos > 1:
        parent_pos = pos // 2
        child = lt.get_element(heap_list, pos)
        parent = lt.get_element(heap_list, parent_pos)
        
        if priority(heap, parent, child):
            break
        
        exchange(heap, parent_pos, pos)
        pos = parent_pos
    
    return heap

def insert(heap, priority, value):
    entry = pqe.new_pq_entry(priority, value)
    heap_list = heap['elements']
    lt.add_last(heap_list, entry)
    heap['size'] += 1
    swim(heap, heap['size'])
    return heap

def sink(heap, pos):
    heap_list = heap['elements']
    
    while pos * 2 < size(heap):
        child_pos = pos * 2
        child = lt.get_element(heap_list, child_pos)
        if pos * 2 + 1 < size(heap):
            child_pos_2 = child_pos + 1
            child_2 = lt.get_element(heap_list, child_pos_2)
            if not priority(heap, child, child_2):
                child = child_2
                child_pos = child_pos_2
        
        parent = lt.get_element(heap_list, pos)
        
        if priority(heap, parent, child):
            break
        
        exchange(heap, pos, child_pos)
        pos = child_pos
    
    return heap

def remove(heap):
    if is_empty(heap):
        return None
    
    heap_list = heap['elements']
    exchange(heap, 1, size(heap))
    ele = lt.remove_last(heap_list)
    heap['size'] -= 1
    sink(heap, 1)
    return pqe.get_value(ele)

def get_first_priority(heap):
    if is_empty(heap):
        return None
    
    heap_list = heap['elements']
    ele = lt.get_element(heap_list, 1)
    
    return pqe.get_value(ele)

def is_present_value(heap, value):
    
    heap_list = heap['elements']
    size = lt.size(heap_list)
    for i in range(size):
        ele = lt.get_element(heap_list, i)
        if ele and pqe.get_value(ele) == value:
            return i
    return -1

def contains(heap, value):
    if is_present_value(heap,value) == -1:
        return False
    else: 
        return True

def improve_priority(heap, priority, value):
    pos= is_present_value(heap,value)
    if pos == -1:
        return heap
    else:
        nod=lt.get_element(heap['elements'], pos)
        nod['priority'] += priority
        
        swim(heap,pos)
    return heap

def improve_priority_set_amount(heap, priority, value):
    pos= is_present_value(heap,value)
    if pos == -1:
        return heap
    else:
        nod=lt.get_element(heap['elements'], pos)
        nod['priority'] = priority
        
        swim(heap,pos)
    return heap
    

def compare_values(ele1,ele2):
    if ele1['value'] == ele2['value']:
        return 0
    elif ele1['value'] > ele2['value']:
       return 1
    else:
        return -1
    