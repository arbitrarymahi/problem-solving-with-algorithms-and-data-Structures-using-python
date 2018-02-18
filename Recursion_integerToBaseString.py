def to_str(no, base):
    char_str = '0123456789ABCDEF'
    if no<base: 
        return char_str[no]
    else:
        return to_str(no//base, base) + char_str[no%base]
        
print to_str(1453,16)
print to_str(769,10)
print to_str(11,2)

from Stack import Stack

def to_str(no, base):
    rec_stk = Stack()
    char_str = '0123456789ABCDEF'
    while no > 0:
        if no < base:
            rec_stk.push(char_str[no])
        else:
            rec_stk.push(char_str[no%base])
                  
        no = no // base
        
    string = ''
    while not rec_stk.is_empty():
        string = string + rec_stk.pop()
    return string                 

print to_str(1453,16)
print to_str(11,2)           
