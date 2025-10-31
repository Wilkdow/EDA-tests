from DataStructures.Tree import bst_node
from DataStructures.List import single_linked_list as lt

def new_map():
    return {"root": None}

def get(bst, key):
    return get_node(bst['root'], key)

def get_node(node, key):
    if node is None:
        return None
    elif bst_node.get_key(node) == key:
        return bst_node.get_value(node)
    else:
        if bst_node.get_key(node) > key:
            return get_node(node['left'], key)
        elif bst_node.get_key(node) < key:
            return get_node(node['right'], key)

def put(bst, key, value):
    bst['root'] = insert_node(bst['root'], key, value)
    return bst
    
def insert_node(node, key, value):
    
    if node is None:
        node = bst_node.new_node(key, value)
        bst_node.increase_size(node)
        return node
    if key == bst_node.get_key(node):
        node = bst_node.replace_value(node, value)
        return node
    elif key < bst_node.get_key(node):
        node['left'] = insert_node(node['left'], key, value)
        bst_node.update_size(node)
    elif key > bst_node.get_key(node):
        node['right'] = insert_node(node['right'], key, value)
        bst_node.update_size(node)
    return node

def is_empty(my_bst):
    return my_bst['root'] == None

def contains(my_bst, key):
    presente = False
    gett=get(my_bst,key)
    if gett == None:
        presente = True
    return presente

def get_min(my_bst):
    if is_empty(my_bst):
        return None
    return get_min_node(my_bst['root'])
    
def get_min_node(root):

    while root['left'] != None:
        root = root['left']
    return root['key']

def get_max(my_bst):
    if is_empty(my_bst):
        return None
    return get_max_node(my_bst['root'])
    
def get_max_node(root):

    while root['right'] != None:
        root = root['right']
    return root['key']

def size(my_bst):
    return size_tree(my_bst['root'])

def size_tree(root):
    n = 0
    if root is not None:
        n += root['size']
    return n

def key_set(my_bst):
    lst = lt.new_list()
    if not is_empty(my_bst):
        lst = preorder_tree(my_bst['root'], lst, bst_node.get_key)
    return lst

def value_set(my_bst):
    lst = lt.new_list()
    if not is_empty(my_bst):
        lst = preorder_tree(my_bst['root'], lst, bst_node.get_value)
    return lst

def preorder_tree(root, lst, func):
    if root is not None:
        lt.add_last(lst, func(root))
        lst = preorder_tree(root['left'], lst, func)
        lst = preorder_tree(root['right'], lst, func)
    return lst

def delete_min(my_bst):
    if not is_empty(my_bst):
        my_bst['root'] = delete_min_tree(my_bst['root'])
    return my_bst

def delete_min_tree(node):
    if node is None:
        return None
    if node['left'] is None:
        return node['right']
    else:
        node['size'] -= 1
        return delete_min_tree(node['left'])

def delete_max(my_bst):
    if not is_empty(my_bst):
        my_bst['root'] = delete_max_tree(my_bst['root'])
    return my_bst

def delete_max_tree(node):
    if node is None:
        return None
    if node['right'] is None:
        return node['left']
    else:
        node['size'] -= 1
        return delete_max_tree(node['right'])

def height(my_best):
    if is_empty(my_best):
        return 0
    return height_tree(my_best['root'])

def height_tree(root, n=1):
    if root['left'] is None and root['right'] is None:
        return n
    n += 1
    r_height, l_height = 0, 0
    if root['right'] is not None:
        r_height = height_tree(root['right'], n)
    if root['left'] is not None:
        l_height = height_tree(root['left'], n)
    return max(r_height, l_height)
def keys(my_bst, key_initial, key_final):
    lst = lt.new_list()
    if not is_empty(my_bst):
        lst = keys_range(my_bst['root'], key_initial,key_final, lst)
    return lst

def keys_range(root, key_initial,key_final, lst):
    if root is not None:
        if bst_node.get_key(root) >= key_initial and bst_node.get_key(root) <= key_final:
            lt.add_last(lst, bst_node.get_key(root))
        if bst_node.get_key(root) >= key_initial:
            lst = keys_range(root['left'], key_initial,key_final, lst)
        if bst_node.get_key(root) <= key_final:
            lst = keys_range(root['right'], key_initial,key_final, lst)
    return lst

def values(my_bst, key_initial, key_final):
    lst = lt.new_list()
    if not is_empty(my_bst):
        lst = values_range(my_bst['root'], key_initial,key_final, lst)
    return lst

def values_range(root, key_initial,key_final, lst):
    if root is not None:
        if bst_node.get_key(root) >= key_initial and bst_node.get_key(root) <= key_final:
            lt.add_last(lst, bst_node.get_value(root))
        if bst_node.get_key(root) >= key_initial:
            lst = values_range(root['left'], key_initial,key_final, lst)
        if bst_node.get_key(root) <= key_final:
            lst = values_range(root['right'], key_initial,key_final, lst)
    return lst

def remove(my_bst, key):
    my_bst['root'] = remove_node(my_bst['root'], key)
    return my_bst

def remove_node(root, key):
    if root is None:
        return None
    if key == bst_node.get_key(root):
        if root['right'] is None and root['left'] is None:
            return None
        else:
            if root['left'] is not None and root['right'] is None:
                temp = root['left']
                root['left'] = None
                return temp
            elif root['left'] is None and root['right'] is not None:
                temp = root['right']
                root['right'] = None
                return temp
            else:
                sucesor = get_min_node(root['right'])
                root['right'] = delete_min_tree(root['right'])
                temp_l = root['left']
                temp_r = root['right']
                sucesor['right'] = temp_r
                sucesor['left'] = temp_l
                bst_node.update_size(sucesor)
                root['right'] = None
                root['left'] = None
                return sucesor
    
    elif key < bst_node.get_key(root):
        root['left'] = remove_node(root['left'], key)
        bst_node.update_size(root)
        return root
    
    elif key > bst_node.get_key(root):
        root['right'] = remove_node(root['right'], key)
        bst_node.update_size(root)
        return root

def ceiling(my_bst, key):
    return ceiling_key(my_bst['root'], key)

def ceiling_key(root, key):
    if root is None:
        return None
    elif bst_node.get_key(root) == key:
        return bst_node.get_key(root)
    elif bst_node.get_key(root) > key:
        if ceiling_key(root['left'], key) is not None:
            return ceiling_key(root['left'], key)
        else:
            return bst_node.get_key(root)
    elif bst_node.get_key(root) < key:
        return ceiling_key(root['right'], key)

def floor(my_bst, key):
    return floor_key(my_bst['root'], key)

def floor_key(root, key):
    if root is None:
        return None
    elif bst_node.get_key(root) == key:
        return bst_node.get_key(root)
    elif bst_node.get_key(root) > key:
        return floor_key(root['left'], key)
    elif bst_node.get_key(root) < key:
        if floor_key(root['right'], key) is not None:
            return floor_key(root['right'], key)
        else:
            return bst_node.get_key(root)