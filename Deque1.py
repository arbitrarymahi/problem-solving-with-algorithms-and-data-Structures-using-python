from Deque import Deque

dq = Deque()

print(dq.is_empty())
print(dq.add_rear(4))
print(dq.add_rear('dog'))
print(dq.add_front('cat'))
print(dq.add_front(True))
print(dq.size())
print(dq.is_empty())
print(dq.add_rear(8.4))
print(dq.remove_rear())
print(dq.remove_front())
