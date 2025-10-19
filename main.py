from DataStructures.List import array_list as lt
from DataStructures.Map import map_linear_probing as lp
from DataStructures.Map import map_separate_chaining as sc
from DataStructures.Tree import binary_search_tree as bst

map = bst.new_map()
bst.put(map, '2020', 'uno')
bst.put(map, '2021', 'dos')
bst.put(map, '2020', 'one')
bst.put(map, '2023', 'one')
bst.put(map, '2024', 'one')
bst.put(map, '2025', 'one')
bst.put(map, '2026', 'one')
bst.put(map, '2027', 'one')
bst.put(map, '2028', 'one')
print(bst.height(map))