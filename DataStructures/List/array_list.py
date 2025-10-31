def new_list():
    newlist = {
        "elements": [],
        "size": 0
    }
    return newlist

def get_element(my_list, index):
    
    if index >= size(my_list):
        return None
    return my_list["elements"][index]

def default_compare(element1, element2):
    
    if element1 == element2:
        return 0
    elif element1 > element2:
        return 1
    return -1

def is_present(my_list, element, cmp_function= default_compare):
    
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list, element):
    
    n_list = my_list
    n_list["elements"].insert(0, element)
    n_list["size"] += 1
    return n_list

def add_last(my_list, element):
    
    n_list = my_list
    n_list["elements"].append(element)
    n_list["size"] += 1
    return n_list

def first_element(my_list):
    
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list["elements"][0]

def is_empty(my_list):
    
    return True if my_list["size"] == 0 else False

def size(my_list):
    
    return my_list["size"]

def last_element(my_list):
    
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list["elements"][size(my_list) - 1]
    
def delete_element(my_list, pos):
    
    n_list = my_list
    if pos >= size(n_list) or pos < 0:
        raise Exception('IndexError: list index out of range')
    
    n_list["elements"].pop(pos)
    n_list["size"] -= 1
    return n_list
    
def remove_first(my_list):
    
    n_list = my_list
    if is_empty(n_list):
        raise Exception('IndexError: list index out of range')
    
    del_element = n_list["elements"].pop(0)
    n_list["size"] -= 1
    return del_element
    
def remove_last(my_list):
    
    n_list = my_list
    if is_empty(n_list):
        raise Exception('IndexError: list index out of range')
    
    del_element = n_list["elements"].pop(size(n_list) - 1)
    n_list["size"] -= 1
    return del_element
    
def insert_element(my_list, element, pos):
    
    n_list = my_list
    if pos > size(n_list) or pos < 0:
        raise Exception('IndexError: list index out of range')
    
    n_list["elements"].insert(pos, element)
    n_list["size"] += 1
    return n_list
    
def change_info(my_list, pos, new_info):
    
    n_list = my_list
    if pos >= size(n_list) or pos < 0:
        raise Exception('IndexError: list index out of range')
    
    n_list["elements"][pos] = new_info
    return n_list
    
def exchange(my_list, pos_1, pos_2):
    
    n_list = my_list
    if (pos_1 or pos_2) >= size(n_list) or (pos_1 or pos_2) < 0:
        raise Exception('IndexError: list index out of range')
    
    temp = n_list["elements"][pos_1]
    n_list["elements"][pos_1] = n_list["elements"][pos_2]
    n_list["elements"][pos_2] = temp
    return n_list
    
def sub_list(my_list, pos_i, num_elements):
    
    if pos_i >= size(my_list) or pos_i < 0:
        raise Exception('IndexError: list index out of range')
    
    n_list = new_list()
    if pos_i + num_elements > size(my_list):
        n_list["elements"] = my_list["elements"][pos_i:size(my_list)]
        n_list["size"] = size(my_list) - pos_i
        return n_list
    else:
        n_list["elements"] = my_list["elements"][pos_i:pos_i + num_elements]
        n_list["size"] = num_elements
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