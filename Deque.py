class Deque:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
        
    def add_front(self, item):
        self.items.append(item)
        
    def add_rear(self, item):
        self.items.insert(0, item)
        
    def remove_front(self):
        return self.items.pop()
        
    def remove_rear(self):  
        return self.items.pop(0)
        
    def size(self):
        return len(self.items)
        
    def __str__(self):
        return (str(self.items))
