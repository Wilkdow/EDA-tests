def new_list ():
    newlist ={
        "first": None,
        "last": None,
        "size": 0,
    }
    
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]
        
def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None: 
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    
    n_list = my_list
    temp = n_list["first"]
    n_list["first"] = {
        "info": element,
        "next": None
    }
    n_list["first"]["next"] = temp
    
    if n_list["last"] == None:
        n_list["last"] = n_list["first"]
    
    n_list["size"] += 1
    return n_list

def add_last(my_list, element):
    
    n_list = my_list
    if n_list["last"] != None:
        n_list["last"]["next"] = {
            "info": element,
            "next": None
        }
        n_list["last"] = n_list["last"]["next"]
    else:
        n_list["first"] = {
            "info": element,
            "next": None
        }
        n_list["last"] = n_list["first"]
    
    n_list["size"] += 1
    return n_list

def size(my_list):
    
    return my_list["size"]

def first_element(my_list):
    
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list["first"]["info"]

def is_empty(my_list):
    
    return True if (my_list["size"] == 0) else False

def last_element(my_list):
    
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list["last"]["info"]

def delete_element(my_list, pos):
    
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    n_list = my_list
    
    node_bef = n_list["first"]
    node = n_list["first"]
    found = False
    i = 0
    while node is not None and not found:
        if i == pos:
            if node == n_list["first"]:
                n_list["first"] = n_list["first"]["next"]
            else:
                if node == n_list["last"]:
                    n_list["last"] = node_bef
                temp = node["next"]
                node_bef["next"] = temp
            
            node["next"] = None
            n_list["size"] -= 1
            found = True
        node_bef = node
        node = node["next"]
        i += 1
    return n_list

def remove_first(my_list):
    
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    
    node = my_list["first"]["info"]
    my_list["first"] = my_list["first"]["next"]
    my_list["size"] -= 1
    return node

def remove_last(my_list):
    
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    
    del_node = my_list["last"]
    del_node_info = my_list["last"]['info']
    node_before = my_list["first"]
    node = my_list["first"]
    while node is not None:
        if node == del_node:
            node_before["next"] = None
            my_list['last'] = node_before
            my_list['size'] -= 1
        node_before = node
        node = node['next']
    return del_node_info

def insert_element(my_list, element, pos):
    
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    
    i = 0
    found = False
    node = my_list['first']
    node_before = None
    while node is not None and not found:
        if i == pos:
            if node == my_list['first']:
                my_list = add_first(my_list, element)
                found = True
            else:
                node_before['next'] = {
                    'info': element,
                    'next': node
                }
                my_list['size'] += 1
                found = True
        node_before = node
        node = node['next']
        i += 1
    
    if not found:
        my_list = add_last(my_list, element)
        found = True
    return my_list

def change_info(my_list, pos, new_info):
    
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    i = 0
    node = my_list['first']
    found = False
    while node is not None and not found:
        if i == pos:
            node['info'] = new_info
            found = True
        node = node['next']
        i += 1
    return my_list

def exchange(my_list, pos_1, pos_2):
    
    if (pos_1 or pos_2) < 0 or (pos_1 or pos_2) >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    i = 0
    node = my_list['first']
    changed = False
    temp_node = None
    while node is not None and not changed:
        if i == pos_1 or i == pos_2:
            if temp_node == None:
                temp_node = node
            else:
                temp = node['info']
                node['info'] = temp_node['info']
                temp_node['info'] = temp
                changed = True
        node = node['next']
        i += 1
    return my_list

def sub_list(my_list, pos, num_elements):
    
    if pos < 0  or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    n_list = new_list()
    n_node = None
    
    i = 0
    j = num_elements
    node = my_list['first']
    while node is not None and j > 0:
        if i >= pos:
            n_list = add_last(n_list, node['info'])
            if n_node is None:
                n_node = n_list['first']
            n_node = n_node['next']
            j -= 1
        
        node = node['next']
        i += 1
    return n_list

def default_sort_criteria(element_1, element_2):
    
    is_sorted = False
    
    if float(element_1) < float(element_2):
        is_sorted = True
        
    return is_sorted

def selection_sort(list, sort_criteria):
    
    l_size = size(list)
    for i in range(l_size):
        min = i
        ele1 = get_element(list, i)
        for j in range(i+1, l_size):
            ele2 = get_element(list, j)
            if sort_criteria(ele1, ele2):
                min = j
                ele1 = get_element(list, min)
        if min != i:
            list = exchange(list, i, min)
    return list

def insertion_sort(list, sort_criteria):
    
    l_size = size(list)
    for i in range(1, l_size):
        k = i
        while k > 0 and (sort_criteria(get_element(list, k-1), get_element(list, k))):
            exchange(list, k-1, k)
            k -= 1
    return list

def shell_sort(list, sort_criteria):
    
    l_size = size(list)
    
    inc = 1
    while inc < l_size/3:
        inc = 3 * inc + 1
    
    while inc > 0:
        for i in range(l_size):
            k = i + inc
            while k < l_size:
                if sort_criteria(get_element(list, i), get_element(list, k)):
                    exchange(list, i, k)
                k += inc
        inc = inc // 3
    return list

def merge_sort(list, sort_criteria):
    
    l_size = size(list)
    
    if l_size <= 1:
        return list
    
    array1 = sub_list(list, 0, l_size//2)
    array2 = sub_list(list, l_size//2, int(l_size))
    
    array1 = merge_sort(array1, sort_criteria)
    array2 = merge_sort(array2, sort_criteria)
    
    return merge(array1, array2, sort_criteria)

def merge(array1, array2, sort_criteria):
    
    n_array = new_list()
    
    while (not is_empty(array1)) and (not is_empty(array2)):
        ele1 = first_element(array1)
        ele2 = first_element(array2)
        
        if sort_criteria(ele1, ele2):
            add_last(n_array, ele2)
            remove_first(array2)
        else:
            add_last(n_array, ele1)
            remove_first(array1)
    
    while not is_empty(array1):
        ele = first_element(array1)
        add_last(n_array, ele)
        remove_first(array1)
    
    while not is_empty(array2):
        ele = first_element(array2)
        add_last(n_array, ele)
        remove_first(array2)
    
    return n_array

def partition(list, sort_criteria, lo, hi):
    
    pivot_index = lo
    pivot = get_element(list, hi)

    for i in range(lo, hi):
        if not sort_criteria(get_element(list, i), pivot):
            exchange(list, i, pivot_index)
            pivot_index += 1
    
    exchange(list, pivot_index, hi)    
    return pivot_index    

def quick_sort(list, sort_criteria):
    
    quick_sort_recursive(list, sort_criteria, 0, size(list)-1)
    return list

def quick_sort_recursive(list, sort_criteria, low, high):
    
    if low < high:
        pivot_i = partition(list, sort_criteria, low, high)
        quick_sort_recursive(list, sort_criteria, low, pivot_i - 1)
        quick_sort_recursive(list, sort_criteria, pivot_i + 1, high)
