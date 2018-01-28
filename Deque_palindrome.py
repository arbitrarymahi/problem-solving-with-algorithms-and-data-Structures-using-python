from Deque import Deque

def pal_checker(test_string):
    tst_str = Deque()
    
    for ch in test_string:
        tst_str.add_front(ch)
       
    pal_flag = True
    
    while tst_str.size() > 1 and pal_flag:
        first_c = tst_str.remove_front()
        last_c = tst_str.remove_rear()
                
        if first_c != last_c:
            pal_flag = False
           
    return pal_flag
    
print(pal_checker('qasdfghfdsa'))
print(pal_checker('asdfggfdsa'))
print(pal_checker('asdfgfdsa'))
print(pal_checker('1234321'))
