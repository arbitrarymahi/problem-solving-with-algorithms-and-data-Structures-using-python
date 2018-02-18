from Stack import Stack
"""
       
def deciToBin(number):
    s=Stack()
    while number > 0:
        rem = number % 2
        s.push(rem)
        number = number // 2
    
    binary = ""
    while not s.is_empty():
        binary = binary + str(s.pop())
    
   
    return binary 
    """
    
def deciToBase(deci,base):
    s=Stack()
    digits = '0123456789ABCDEF'
    
    while deci > 0:
        rem = deci % base
        s.push(rem)
        deci = deci // base
    
    
    newString = ""
    while not s.is_empty():
        newString = newString + digits[s.pop()]
    
   
    return newString
        
print(deciToBase(17,2))
print(deciToBase(45,2))
print(deciToBase(96,2))
print(deciToBase(8,8))
print(deciToBase(2,2))
