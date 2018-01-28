import timeit
from timeit import Timer

#x = list(range(2000000))

pop_zero = Timer("x.pop(0)","from __main__ import x")
#print(pop_zero.timeit(number = 1000))

pop_last = Timer("x.pop()","from __main__ import x")
#print(pop_last.timeit(number = 1000))

print("pop(0) pop()")

for i in range(1000000,100000001,100000):
    x = list(range(i))
    pz = pop_zero.timeit(number = 1000)
    x = list(range(i))
    pl = pop_last.timeit(number = 1000)
    
    print("%5.15f   %5.15f "%(pz,pl))
