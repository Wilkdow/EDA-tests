from DataStructures.Tree import rbt_node as rbtn

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