def new_node(key, value):
    return {
        "key": key,
        "value": value,
        "size": 1,
        "left": None,
        "right": None
    }

def get_value(my_node):
    return my_node['value']

def get_key(my_node):
    return my_node['key']

def replace_value(my_node, value):
    my_node['value'] = value
    return my_node

def increase_size(my_node):
    my_node['size'] += 1
    return my_node