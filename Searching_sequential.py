def sequential_search(a_list, item):
    pointer = 0
    found = False
    
    while not found and pointer < len(a_list):
        if item == a_list[pointer]:
            found = True
        else:
            pointer += 1
      
    return found   
    
def ordered_sequential_search(a_list, item):
    pointer = 0
    found = False
    stop = False
    while not found and pointer < len(a_list) and not stop:
        if item == a_list[pointer]:
            found = True
        elif item < a_list[pointer]:
            stop = True
        else:
            pointer += 1
      
    return found    

test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search(test_list, 3))
print(sequential_search(test_list, 13))

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(ordered_sequential_search(test_list, 3))
print(ordered_sequential_search(test_list, 13))
