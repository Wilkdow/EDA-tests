from DataStructures.List import array_list as lt
from DataStructures.Map import map_linear_probing as lp
from DataStructures.Map import map_separate_chaining as sc
from DataStructures.Tree import binary_search_tree as bst

map = bst.new_map()
bst.put(map, '2020', 'uno')
bst.put(map, '2021', 'dos')
bst.put(map, '2020', 'one')
print(bst.get_max(map))