from DataStructures.Tree import rbt_node as rbtn
from DataStructures.List import single_linked_list as lt
from DataStructures.Tree import tree_traversal as trav

def new_map():
    return {
        'root': None,
        'type': 'RBT'
    }

def put(rbt, key, value):
    rbt['root'] = insert_node(rbt['root'], key, value)
    if rbtn.is_red(rbt['root']):
        rbtn.flip_node_color(rbt['root'])
    return rbt

def insert_node(node, key, value):
    if node is None:
        node = rbtn.new_node(key, value)
        return node
    
    if key == rbtn.get_key(node):
        node = rbtn.replace_value(node, value)
        return node                                                 
        
    elif key < rbtn.get_key(node):
        node['left'] = insert_node(node['left'], key, value)
        rbtn.update_size(node)
        
    elif key > rbtn.get_key(node):
        node['right'] = insert_node(node['right'], key, value)
        rbtn.update_size(node)
    
    r_child = rbtn.get_right_child(node)
    l_child = rbtn.get_left_child(node)
    
    if rbtn.is_red(r_child) and (l_child == None or rbtn.is_black(l_child)):
        node = rotate_left(node)
        
    elif rbtn.is_red(l_child) and rbtn.is_red(node):
        node = rotate_right(node)
        rbtn.flip_colors(node)
    
    elif rbtn.is_red(l_child) and rbtn.is_red(r_child):
        rbtn.flip_colors(node)
    
    return node

def rotate_left(node):
    r_node = rbtn.get_right_child(node)
    b_node = rbtn.get_left_child(r_node)
    node['right'] = b_node
    r_node['left'] = None
    
    rbtn.update_size(node)
    rbtn.update_size(r_node)
    
    temp = node
    node = r_node
    rbtn.change_color(node, temp['color'])
    if rbtn.is_black(temp):
        rbtn.flip_node_color(temp)
    node['left'] = temp
    rbtn.update_size(node)
    
    return node

def rotate_right(node):
    l_node = rbtn.get_left_child(node)
    b_node = rbtn.get_left_child(l_node)
    node['left'] = b_node
    l_node['right'] = None
    
    rbtn.update_size(node)
    rbtn.update_size(l_node)
    
    temp = node
    node = l_node
    node['right'] = temp
    rbtn.update_size(node)
    
    return node

def is_empty(rbt):
    if rbt['root'] == None:
        return True
    return False

def get(rbt, key):
    return get_node(rbt['root'], key)

def get_node(root, key):
    if root is None:
        return None
    else:
        if root['key'] == key:
            return root['value']
        elif root['key'] > key:
            return get_node(root['left'], key)
        elif root['key'] < key:
            return get_node(root['right'], key)

def contains(rbt, key):
    if get(rbt,key) is None:
        return False
    else:
        return True

def height(rbt):
    if is_empty(rbt):
        return 0
    return height_tree(rbt['root'])

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
        
def get_min(rbt):
    if rbt is not None:
        return get_min_node(rbt['root'])
    else: 
        return None

def get_min_node(node):
    if node is not None:
        while node['left'] is not None: 
            node = node['left']

        return node['key']

def get_max(rbt):
    if rbt is not None:
        return get_max_node(rbt['root'])
    else: 
        return None 

def get_max_node(node):
    if node is not None:
        while node['right'] is not None: 
            node = node['right']       
        return node['key']

def key_set(rbt):
    return trav.inorder(rbt, rbtn.get_key)

def value_set(rbt):
    return trav.inorder(rbt, rbtn.get_value)

def size(rbt):
    return size_tree(rbt['root'])

def size_tree(node):
    n = 0
    if node is not None:
        n = node['size']
    return n

def keys(rbt, key_initial, key_final):
    lst = lt.new_list()
    if not is_empty(rbt):
        lst = keys_range(rbt['root'], key_initial, key_final, lst)
    return lst

def keys_range(root, key_initial,key_final, lst):
    if root is not None:
        if rbtn.get_key(root) >= key_initial and rbtn.get_key(root) <= key_final:
            lt.add_last(lst, rbtn.get_key(root))
        if rbtn.get_key(root) >= key_initial:
            lst = keys_range(root['left'], key_initial,key_final, lst)
        if rbtn.get_key(root) <= key_final:
            lst = keys_range(root['right'], key_initial,key_final, lst)
    return lst

def values(rbt, key_initial, key_final):
    lst = lt.new_list()
    if not is_empty(rbt):
        lst = values_range(rbt['root'], key_initial,key_final, lst)
    return lst

def values_range(root, key_initial,key_final, lst):
    if root is not None:
        if rbtn.get_key(root) >= key_initial and rbtn.get_key(root) <= key_final:
            lt.add_last(lst, rbtn.get_value(root))
        if rbtn.get_key(root) >= key_initial:
            lst = keys_range(root['left'], key_initial,key_final, lst)
        if rbtn.get_key(root) <= key_final:
            lst = keys_range(root['right'], key_initial,key_final, lst)
    return lst

def remove(my_bst, key):
    my_bst['root'] = remove_node(my_bst['root'], key)
    return my_bst

def remove_node(root, key):
    if root is None:
        return None
    if key == rbtn.get_key(root):
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
                temp_l = root['left']
                temp_r = root['right']
                sucesor['right'] = temp_r
                sucesor['left'] = temp_l
                rbtn.update_size(sucesor)
                root['right'] = None
                root['left'] = None
                return sucesor
            
    elif key < rbtn.get_key(root):
        root['left'] = remove_node(root['left'], key)
        rbtn.update_size(root)
        return root
    
    elif key > rbtn.get_key(root):
        root['right'] = remove_node(root['right'], key)
        rbtn.update_size(root)
        return root
    
    r_child = rbtn.get_right_child(node)
    l_child = rbtn.get_left_child(node)
    
    if rbtn.is_red(r_child) and (l_child == None or rbtn.is_black(l_child)):
        node = rotate_left(node)
        
    elif rbtn.is_red(l_child) and rbtn.is_red(node):
        node = rotate_right(node)
        rbtn.flip_colors(node)
    
    elif rbtn.is_red(l_child) and rbtn.is_red(r_child):
        rbtn.flip_colors(node)
    
    return node

def ceiling(my_bst, key):
    return ceiling_key(my_bst['root'], key)

def ceiling_key(root, key):
    if root is None:
        return None
    elif rbtn.get_key(root) == key:
        return rbtn.get_key(root)
    elif rbtn.get_key(root) > key:
        if ceiling_key(root['left'], key) is not None:
            return ceiling_key(root['left'], key)
        else:
            return rbtn.get_key(root)
    elif rbtn.get_key(root) < key:
        return ceiling_key(root['right'], key)

def floor(my_bst, key):
    return floor_key(my_bst['root'], key)

def floor_key(root, key):
    if root is None:
        return None
    elif rbtn.get_key(root) == key:
        return rbtn.get_key(root)
    elif rbtn.get_key(root) > key:
        return floor_key(root['left'], key)
    elif rbtn.get_key(root) < key:
        if floor_key(root['right'], key) is not None:
            return floor_key(root['right'], key)
        else:
            return rbtn.get_key(root)
        
def rank(rbt,key):
    return rank_keys(rbt['root'], key)

def rank_keys(root, key):
    if root is None: 
        return 0
    else:
        node = get_node(root, key)
        if node is not None:
            return size_tree(node['left'])