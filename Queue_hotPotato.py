from Queue import Queue

def hot_potato(nameList, num):
    nameQueue = Queue()
    for name in nameList:
        nameQueue.enqueue(name)
        
    while nameQueue.size() > 1:
        for i in range(num):
            nameQueue.enqueue(nameQueue.dequeue())
        
        nameQueue.dequeue()
        
    return nameQueue.dequeue()


names = ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'] 
print(hot_potato(names, 5))
