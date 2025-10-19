import bst_node as n

def new_map():
    return {"root": None}

def get(bst, key):
    return get_node(bst['root', key])

def get_node(node, key):
    if node is None:
        return None
    if n.get_key(node) == key:
        return n.get_value(node)
    else:
        if n.get_key(node) < key:
            get_node(node['left'])
        elif n.get_key(node) > key:
            get_node(node['right'])

def put(bst, key, value):
    bst['root'] = insert_node(bst['root'], key, value, [])
    return bst
    
def insert_node(node, key, value, list: list):
    
    if node is None:
        node = n.new_node(key, value)
        for parent in list:
            n.increase_size(parent)
        if list.is_empty():
            return node
        return list[0]
    if key == n.get_key(node):
        node = n.replace_value(node, value)
        if list.is_empty():
            return node
        return list[0]
    elif key < n.get_key(node):
        list.append(node)
        insert_node(node['left'], key, value, list)
    elif key > n.get_key(node):
        list.append(node)
        insert_node(node['right'], key, value, list)

def is_empty(my_bst):
    return my_bst['root'] == None