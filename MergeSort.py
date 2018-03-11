def merge_sort(a_list):
    if len(a_list) > 1:
        mid = len(a_list) // 2
        
        left_list = a_list[ :mid]
        right_list = a_list[mid: ]
        
        merge_sort(left_list)
        merge_sort(right_list)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                a_list[k] = left_list[i]
                i += 1
            else:
                a_list[k] = right_list[j]
                j += 1
            k += 1
        
        while i < len(left_list):
            a_list[k] = left_list[i]
            i += 1
            k += 1
        
        while j < len(right_list):
            a_list[k] = right_list[j]
            j += 1
            k += 1
    print("Merging ", a_list)   
        
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(a_list)
print(a_list)
        
