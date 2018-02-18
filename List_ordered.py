from List_node import Node

class OrderedList:
    def __init__(self):
       self.head = None
       
    def is_empty(self):
        return self.head == None
        
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.get_next()
            
        return count
        
    def __str__(self):
        current = self.head
        list1 = []
        while current != None:
            list1 = list1+[current.get_data()]
            current = current.get_next()
        
        return str(list1)
        
    def remove(self, item):
        current = self.head
        prev = None
        found = False
        print self.head
                
        while current != None and not found:
            print current
            print prev
            if item == current.get_data():
                found = True
            else:
                prev = current
                current = current.get_next()
            
        if prev == None:
            self.head = current.get_next()
        else:
            prev.set_next(current.get_next())
            
    def search(self, item):
        found = False
        current = self.head
        stop = False
        
        while current != None and not found and not stop:
            if item < current.get_data():
                stop = True
            elif item == current.get_data():
                found = True
            else:
                current = current.get_next()
        
        return found
        
    def add(self, item):
        current = self.head
        prev = None
        stop = False
        
        while current != None and not stop:
            if item < current.get_data():
                stop = True
            else:
                prev = current
                current = current.get_next()
        temp = Node(item)
        if prev == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.next = prev.get_next()
            prev.set_next(temp)
            
list1 = OrderedList()

print list1.is_empty()
list1.add(31)
list1.add(77)
list1.add(17)
list1.add(93)
list1.add(99)
print list1.size()
print(list1)
list1.remove(99)
#print list1.size()
#print list1.remove(54)
print list1.size()
print(list1)
print list1.search(77) 
print list1.search(7)          
    
                     
            
