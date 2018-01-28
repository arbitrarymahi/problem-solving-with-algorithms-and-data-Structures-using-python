from Stack import Stack
s = Stack()

print (s.is_empty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.is_empty())
print(s)
s.push(8.4)
s.push(44)

print(s.pop())
print(s.pop())
print(s.size())
"""
m = Stack()
m.push('x')
m.push('y')
m.push('z')
while not m.is_empty():
    m.pop()
    m.pop()
print(m)
"""
