def bubble_sort(a_list):
    exchanges = True
    pass_num = len(a_list)-1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i  in range(pass_num):
            if a_list[i] > a_list[i+1]:
                exchanges = True
                #swapping
                a_list[i],a_list[i+1] = a_list[i+1],a_list[i]
        pass_num -= 1
a_list = [54,26,93,17,77,31,44,55,20,3]
bubble_sort(a_list)
print(a_list)
