import queue
L=queue.Queue(maxsize=5)
L.put(10)
L.put(20)
print(type(L))
print(L.get())
print(L.get())
