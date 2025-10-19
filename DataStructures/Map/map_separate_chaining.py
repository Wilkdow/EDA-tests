from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as sll
import random

def new_map(num_elements:int, load_factor:float, prime=109345121):
    n = num_elements/load_factor
    capacity = round(n)
    
    while not mf.is_prime(capacity):
        capacity += 1
    
    table = lt.new_list()
    for i in range(capacity):
        lt.add_last(table, sll.new_list())
    
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

def default_compare(key, element):
    
    n = 0
    if key > me.get_key(element):
        n = 1
    elif key < me.get_key(element):
        n = -1
    return n

def size(my_map):

    return my_map['size']

def is_empty(my_map):
    
    return my_map['size'] == 0

def rehash(my_map):
    
    org_capacity, org_load_factor, prime = my_map['capacity'], my_map['limit_factor'], my_map['prime']
    n_map = new_map(round(org_capacity * org_load_factor * 2), org_load_factor, prime)
    org_table = my_map['table']
    
    for i in range(lt.size(org_table)):
        bucket = lt.get_element(org_table, i)
        if not sll.is_empty(bucket):
            for i in range(sll.size(bucket)):
                ele = sll.get_element(bucket, i)
                key, value = me.get_key(ele), me.get_value(ele)
                n_map = put(n_map, key, value)
    return n_map

def put(my_map, key, value): # small issue with not assigning the pam into the pum (ex: map = put(....) works, but put(...) does not)
    
    table = my_map['table']
    hash_value = mf.hash_value(my_map, key)
    
    bucket = lt.get_element(table, hash_value)
    replaced = False
    for i in range(sll.size(bucket)):
        ele = sll.get_element(bucket, i)
        if default_compare(key, ele) == 0:
            replaced = True
            ele = me.set_value(ele, value)
            break
    
    if not replaced:
        sll.add_last(bucket, me.new_map_entry(key, value))
        my_map['size'] += 1
    
    my_map['current_factor'] = size(my_map) / my_map['capacity']
    if my_map['current_factor'] >= my_map['limit_factor']:
        n_map = rehash(my_map)
        for key in my_map.keys():
            my_map[key] = n_map[key]
    
    return my_map

def contains(my_map, key):
    
    hash_value = mf.hash_value(my_map, key)
    bucket = lt.get_element(my_map['table'], hash_value)
    for i in range(sll.size(bucket)):
        if default_compare(key, sll.get_element(bucket, i)) == 0:
            return True
    return False

def get(my_map, key):
    
    hash_value = mf.hash_value(my_map, key)
    bucket = lt.get_element(my_map['table'], hash_value)
    for i in range(sll.size(bucket)):
        if default_compare(key, sll.get_element(bucket, i)) == 0:
            return me.get_value(sll.get_element(bucket, i))
    return None

def remove(my_map, key):
    
    hash_value = mf.hash_value(my_map, key)
    bucket = lt.get_element(my_map['table'], hash_value)
    for i in range(sll.size(bucket)):
        if default_compare(key, sll.get_element(bucket, i)) == 0:
            sll.delete_element(bucket, i)
            my_map['size'] -= 1
            break
    return my_map

def key_set(my_map):
    
    l_keys = lt.new_list()
    table = my_map['table']
    for i in range(lt.size(table)):
        bucket = lt.get_element(table, i)
        if bucket is not None:
            for j in range(sll.size(bucket)):
                ele = sll.get_element(bucket, j)
                lt.add_last(l_keys, me.get_key(ele))
    return l_keys

def value_set(my_map):
    
    l_values = lt.new_list()
    table = my_map['table']
    for i in range(lt.size(table)):
        bucket = lt.get_element(table, i)
        if bucket is not None:
            for j in range(sll.size(bucket)):
                ele = sll.get_element(bucket, j)
                lt.add_last(l_values, me.get_value(ele))
    return l_values