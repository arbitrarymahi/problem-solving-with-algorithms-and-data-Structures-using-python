from Queue import Queue

q = Queue()

print(q.is_empty())
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
print(q.dequeue())
print(q.is_empty())
q.enqueue(8.4)

print(q.dequeue())

