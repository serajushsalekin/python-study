############## Queue(FIFO)  ####################  
class Queue():
  def __init__(self):
    self.queue = []
  def enque(self, value):
    self.queue.append(value)
  def deque(self):
    del self.queue[0]
  def show(self):
    return self.queue
  

q  = Queue()

q.enque(1)
q.enque(2)
q.enque(3)
q.enque(4)
print(q.show())
q.deque()
q.deque()
q.deque()
print(q.show())
##################  stack(LIFO) ################
li = []

li.append(1)
li.append(2)
li.append(3)
li.append(4)
print(li)
li.pop()
print(li)
