def insertion_sort(a_list):
    for index in range(1,len(a_list)):
        current_value = a_list[index]
        position = index
        
        while position > 0 and current_value < a_list[position - 1]:
            a_list[position]  = a_list[position - 1]
            position -= 1
        a_list[position] = current_value
        
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(a_list)
print(a_list)    
                    
