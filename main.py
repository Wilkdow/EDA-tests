from DataStructures.List import array_list as lt
from DataStructures.Map import map_linear_probing as lp
from DataStructures.Map import map_separate_chaining as sc
from DataStructures.Tree import binary_search_tree as bst
from DataStructures.Tree import red_black_tree as rbt
from DataStructures.Tree import rbt_node as rbtn
from DataStructures.Tree import tree_traversal as trav
import logic

map = rbt.new_map()
rbt.put(map, 4, '')
rbt.put(map, 7, '')
rbt.put(map, 12, '')
rbt.put(map, 15, '')
rbt.put(map, 3, '')
print(rbt.get(map, 7))