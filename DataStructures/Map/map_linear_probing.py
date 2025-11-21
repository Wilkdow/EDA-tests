from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.List import array_list as lt
import random

def new_map(num_elements:int, load_factor:float, prime=109345121):
    n = num_elements/load_factor
    capacity = round(n)
    
    while not mf.is_prime(capacity):
        capacity += 1
    
    table = lt.new_list()
    for i in range(capacity):
        lt.add_last(table, me.new_map_entry(None, None))
    
    n_map = {
        "prime": prime,
        'capacity': capacity,
        "scale": random.randint(1, prime-1),
        "shift": random.randint(0, prime-1),
        "table": table,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0
    }
    return n_map

def is_available(table, pos):
    
    my_entry = lt.get_element(table, pos)
    if me.get_key(my_entry) is None or me.get_key(my_entry) == "__EMPTY__":
        return True
    return False

def size(my_map):
    
    return my_map['size']

def is_empty(my_map):
    
    return size(my_map) == 0

def default_compare(key, my_entry):
    
    n = 0
    if key > me.get_key(my_entry):
        n = 1
    elif key < me.get_key(my_entry):
        n = -1
    return n

def find_slot(my_map, key, hash_value):
    
    first_avail = None
    found = False
    occupied = False
    table = my_map['table']
    while not found:
        if is_available(table, hash_value):
            if first_avail is None:
                first_avail = hash_value
            my_entry = lt.get_element(table, hash_value)
            if me.get_key(my_entry) is None:
                found = True
        elif default_compare(key, lt.get_element(table, hash_value)) == 0:
            first_avail = hash_value
            found = True
            occupied = True
        hash_value = (hash_value + 1) % my_map['capacity']
        
    return occupied, first_avail

def rehash(my_map):
    
    org_capacity, org_load_factor = my_map['capacity'], my_map['limit_factor']
    n_map = new_map(round(org_capacity * org_load_factor * 2), org_load_factor, my_map['prime'])
    org_table = my_map['table']
    for i in range(size(org_table)):
        if is_available(org_table, i):
            continue
        ele = lt.get_element(org_table, i)
        key, value = me.get_key(ele), me.get_value(ele)
        n_map = put(n_map, key, value)
    return n_map

def put(my_map, key, value):
    
    if my_map['current_factor'] >= my_map['limit_factor']:
        my_map = rehash(my_map)

    table = my_map['table']
    hash_value = mf.hash_value(my_map, key)
    occupied, slot = find_slot(my_map, key, hash_value)
    if not occupied:
        my_map['size'] += 1
        my_map['current_factor'] = size(my_map)/my_map['capacity']
    n_entry = me.new_map_entry(key, value)
    lt.change_info(table, slot, n_entry)
    
    if my_map['current_factor'] >= my_map['limit_factor']:
        my_map = rehash(my_map)
        my_map['current_factor'] = size(my_map)/my_map['capacity']
    
    return my_map

def contains(my_map, key):
    
    hash_value = mf.hash_value(my_map, key)
    return find_slot(my_map, key, hash_value)[0]

def get(my_map, key):
    
    table = my_map['table']
    ret = None
    hash_value = mf.hash_value(my_map, key)
    occupied, slot = find_slot(my_map, key, hash_value)
    if occupied:
        ele = lt.get_element(table, slot)
        ret = me.get_value(ele)
    return ret

def remove(my_map, key):
    
    table = my_map['table']
    hash_value = mf.hash_value(my_map, key)
    occupied, slot = find_slot(my_map, key, hash_value)
    if occupied:
        ele = lt.get_element(table, slot)
        me.set_key(ele, None)
        me.set_value(ele, None)
        my_map['size'] -= 1
    return my_map

def key_set(my_map):
    
    l_keys = lt.new_list()
    table = my_map['table']
    for i in range(lt.size(table)):
        ele = lt.get_element(table, i)
        key = me.get_key(ele)
        if key is not None and key != "__EMPTY__":
            lt.add_last(l_keys, key)
    return l_keys

def value_set(my_map):
    
    l_values = lt.new_list()
    table = my_map['table']
    for i in range(lt.size(table)):
        ele = lt.get_element(table, i)
        value = me.get_value(ele)
        if value is not None and value != "__EMPTY__":
            lt.add_last(l_values, value)
    return l_values