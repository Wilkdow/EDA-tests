from DataStructures.List import single_linked_list as lt
from DataStructures.Tree import rbt_node as rbtn

def inorder(map, func):
    lst = lt.new_list()
    if (map is not None):
        lst = inorder_tree(map['root'], lst, func)
    return lst

def inorder_tree(node, lst, func):
    if node is not None:
        l_child = rbtn.get_left_child(node)
        if l_child:
            lst = inorder_tree(l_child, lst, func)
        lt.add_last(lst, func(node))
        r_child = rbtn.get_right_child(node)
        if r_child:
            lst = inorder_tree(r_child, lst, func)
    return lst