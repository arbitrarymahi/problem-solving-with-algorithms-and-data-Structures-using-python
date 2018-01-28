class Node:
    def __init__(self,init_data):
        self.data = init_data
        self.next = None
        
    def get_data(self):
        return self.data
        
    def get_next(self):
        return self.next
        
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next
        
class UnorderedList:
    def __init__(self):
        self.head = None
                
    def is_empty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp
               
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.get_next()
            
        return count
        
    def search(self, item):
        loc = None
        count = 0
        found = False
        current = self.head
               
        while current != None and not found:
            if item == current.get_data():
                found = True
                loc = count
            current = current.get_next()
            count += 1
        
        if found:
            return str("item found at position %r"%(loc))
        else:
            return "item not found"
            
    def remove(self, item):
        prev = None
        found = False
        current = self.head
               
        while current != None and not found:
            if item == current.get_data():
                found = True
            else:
                prev = current
                current = current.get_next()
                    
        if prev == None:
            self.head = current.get_next()
        else:
            prev.set_next(current.get_next())
            
    def append(self, item):
        prev = None
        found = False
        current = self.head
               
        while current != None and not found:
            
                prev = current
                current = current.get_next()
                
        temp = Node(item)
        prev.set_next(temp)
    
    
list1 = UnorderedList()

print list1.is_empty()
list1.add(31)
list1.add(77)
list1.add(17)
print list1.size()
list1.add(93)
list1.add(54)
print list1.size()
print list1.remove(31)
print list1.size()
print list1.remove(54)
print list1.size()
list1.append(73)
print list1.size()
list1.append(799)
print list1.size()
