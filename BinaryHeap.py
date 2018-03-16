class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
    
    def perc_up(self, i):
        while i//2 > 0:
            if self.heap_list[i] < self.heap_list [i //2]:
                tmp = self.heap_list[i // 2] 
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2
        
    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)

    def perc_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc
            
    def min_child(self, i):
        if (i * 2 + 1) > self.current_size:
            return i* 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
    
    def del_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val
        
    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while (i > 0):
            self.perc_down(i)
            i -= 1
            
heap = BinHeap()
heap.build_heap([9, 6, 5, 2, 3])
#heap.insert(5)
#heap.insert(3)
#heap.insert(9)
#heap.perc_down()
print("done")
