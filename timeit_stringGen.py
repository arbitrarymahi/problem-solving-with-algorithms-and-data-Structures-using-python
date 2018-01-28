def l1():
    l= []
    for i in range(1000):
        l = l + [i]
    return l    
def test2():
    l = []
    for i in range(1000):
        l.append(i)
    return l    
def test3():
    l = [i for  i in range(1000)]
    return l
def test4():
    l = list(range(1000))
    return l
def emp():
    None

# Import the timeit module
import timeit
# Import the Timer class defined in the module
from timeit import Timer
# If the above line is excluded, you need to replace Timer with timeit.Timer when defining a Timer object
t1 = Timer("l1()", "from __main__ import l1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number = 1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")
t4 = Timer("emp()", "from __main__ import emp")
print("list range ",t4.timeit(number=1000), "milliseconds")
