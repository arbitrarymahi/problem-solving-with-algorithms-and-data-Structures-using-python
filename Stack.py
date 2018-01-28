
# Top at the end of the list #
# Order of magnitude = O(1) #
class Stack:
    def __init__(self):
        self.items = []
        
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[len(self.items)-1]
        
    def is_empty(self):
        return self.items == []
        
    def size(self):
        return len(self.items)
        
    def __str__(self):
        return str(self.items) 
            
    def str_reverse(self,x):
        for char in x:
            self.push(char)
        
        self.items.reverse()
    
        return ''.join(self.items) 
"""
# Top at the beginning of the list #
# Order of magnitude = O(n) #

class Stack:
    def __init__(self):
        self.items = []
        
    def push(self,item):
        self.items.insert(0,item)
        
    def pop(self):
        return self.items.pop(0)
        
    def peek(self):
        return self.items[0]
        
    def is_empty(self):
        return self.items == []
        
    def size(self):
        return len(self.items)
        
    def __str__(self):
        return str(self.items)
"""
