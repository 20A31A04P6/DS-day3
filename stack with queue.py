from queue import LifoQueue
s=LifoQueue(maxsize=3)
print(s.qsize())
s.put('a')
s.put('b')
s.put('c')
print(s.full())
print(s.qsize())
print(s.get())
print(s.get())
print(s.get())
print(s.empty())
      
