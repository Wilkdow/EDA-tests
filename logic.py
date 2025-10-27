from DataStructures.Tree import bst_node
from DataStructures.Tree import binary_search_tree as bst
from DataStructures.List import single_linked_list as lt

def visualize_tree(tree):
    if bst.is_empty(tree):
        return None
    return '\n'.join(visualize_tree_recursive(tree['root']))
        
def visualize_tree_recursive(node, str_nodes:list = [], n= 0):
    if len(str_nodes) >= n:
        str_nodes.append('')
    str_nodes[n] += f"{bst_node.get_key(node)}, {bst_node.get_value(node)}\t"
    if node['left'] is not None:
        str_nodes = indent_string(str_nodes)
        str_nodes = visualize_tree_recursive(node['left'], str_nodes, n+1)
    else:
        str_nodes = indent_string(str_nodes, 2)
    if node['right'] is not None:
        str_nodes = visualize_tree_recursive(node['right'], str_nodes, n+1)
    return str_nodes

def indent_string(l_string:list, times = 1, tab:str= '  '):
    indented_lines = [tab * times + line for line in l_string if not line.isspace()]
    return indented_lines