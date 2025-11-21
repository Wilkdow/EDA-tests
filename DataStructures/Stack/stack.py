from DataStructures.List import array_list as lt

def new_stack():
    
    return lt.new_list()

def push(my_stack, element):
    
    return lt.add_first(my_stack, element)

def pop(my_stack):
    
    if is_empty(my_stack):
        raise Exception('EmptyStructureError: stack is empty')
    
    return lt.remove_first(my_stack)

def is_empty(my_stack):
    
    return True if lt.size(my_stack) == 0 else False

def size(my_stack):
    
    return lt.size(my_stack)

def top(my_stack):
    
    return lt.first_element(my_stack)