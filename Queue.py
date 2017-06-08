class Queue:
	def __init__(self):
		self.queue = []

	def isEmpty(self):
		return self.queue == []

	def enqueue(self, data):
		self.queue.append(data)

	def dequeue(self):
		data = self.queue[0]
		del self.queue[0]
		return data			

	def peek(self):
		return self.queue[0]

	def sizeQueue(self):
		return len(self.queue)	


stack = Queue()	
stack.enqueue(10)
stack.enqueue(20)
stack.enqueue(30)
print(stack.sizeQueue())
stack.dequeue()
stack.dequeue()
print(stack.sizeQueue())
print(stack.peek())
print(stack.sizeQueue())