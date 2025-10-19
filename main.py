from DataStructures.List import array_list as lt
from DataStructures.Map import map_linear_probing as lp
from DataStructures.Map import map_separate_chaining as sc
from DataStructures.Tree import binary_search_tree as bst

map = bst.new_map()
print(bst.size(map))
bst.put(map, 1, 'uno')
bst.put(map, 2, 'dos')
bst.put(map, 1, 'one')
bst.put(map, 7, 'dos')
bst.put(map, 5, 'dos')
bst.put(map, 0, 'dos')
print(map)