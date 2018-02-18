from Queue import Queue

def radixSort(x):
    main_bin = Queue()
    for num in x:
        main_bin.enqueue(int(num))
        
    print(main_bin)
        
    #zero,one,two,three,four,five,six,seven,eight,nine = Queue()
    dicts = {1:'one', 2:'two', 3:'three',
             4:'four', 5:'five', 6:'six',
             7:'seven', 8:'eight', 9:'nine',
             0:'zero'}
    """for value in dicts.values():
        print value
        value = Queue()
        print value
        """
    zero = Queue()
    one = Queue()
    two = Queue()
    three = Queue()
    four = Queue()
    five = Queue()
    six = Queue()
    seven = Queue()
    eight = Queue()
    nine = Queue()
        
    def main_enqueue():
        while not zero.is_empty():
            main_bin.enqueue(zero.dequeue())
        while not one.is_empty():
            main_bin.enqueue(one.dequeue())
        while not two.is_empty():
            main_bin.enqueue(two.dequeue())
        while not three.is_empty():
            main_bin.enqueue(three.dequeue())
        while not four.is_empty():
            main_bin.enqueue(four.dequeue()) 
        while not five.is_empty():
            main_bin.enqueue(five.dequeue())
        while not six.is_empty():
            main_bin.enqueue(six.dequeue())
        while not seven.is_empty():
            main_bin.enqueue(seven.dequeue())
        while not eight.is_empty():
            main_bin.enqueue(eight.dequeue())
        while not nine.is_empty():
            main_bin.enqueue(nine.dequeue())    
                
    def queue_sort(x,y):
        while not main_bin.is_empty():
            temp = main_bin.dequeue()
            if (temp%x)/y == 0:
                zero.enqueue(temp)
            elif (temp%x)/y == 1:
                one.enqueue(temp)
            elif (temp%x)/y == 2:
                two.enqueue(temp)
            elif (temp%x)/y == 3:
                three.enqueue(temp)
            elif (temp%x)/y == 4:
                four.enqueue(temp)
            elif (temp%x)/y == 5:
                five.enqueue(temp)
            elif (temp%x)/y == 6:
                six.enqueue(temp)
            elif (temp%x)/y == 7:
                seven.enqueue(temp)
            elif (temp%x)/y == 8:
                eight.enqueue(temp)
            elif (temp%x)/y == 9:
                nine.enqueue(temp)
                
    queue_sort(10,1)
    main_enqueue()  
    
    print(main_bin)
            
    queue_sort(100,10)  
    main_enqueue()
    
    print(main_bin)
            
    queue_sort(1000,100)  
    main_enqueue()  
    
    
            
    print(main_bin)
            
            
    main_enqueue()    
        
    print(main_bin)


            
radixSort([12,43,464,234,65,23,25,33,43,333])
