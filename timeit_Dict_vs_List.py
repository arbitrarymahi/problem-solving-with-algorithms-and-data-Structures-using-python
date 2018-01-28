import timeit
import random
for i in range(10000,1000001,20000):
    t = timeit.Timer("x[random.randrange(%d) in x]"%i,
                        "from __main__ import random,x")
    x = list(range(i))
    lst_time = t.timeit(number = 1000)


    
    x = {j:None for j in range(i)}
    dct_time = t.timeit(number = 1000)
    print("%d,  %10.3f   %10.3f"%(i, lst_time, dct_time))

# to  check that list has constant time for indexing operation
t = timeit.Timer("x[random.randint(0,%d)]"%i,
                        "from __main__ import random,x")


 