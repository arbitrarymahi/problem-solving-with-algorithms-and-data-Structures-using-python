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
        
print(deciToBase(25,8))
print(deciToBase(256,16))
print(deciToBase(16,16))
print(deciToBase(8,8))
print(deciToBase(2,2))
