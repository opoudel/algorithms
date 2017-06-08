class Heap(object):
	HEAP_SIZE = 10

	def __init__(self):
		self.heap = [0] * Heap.HEAP_SIZE
		self. curPos = -1

	def insert(self, item):
		if self.isFull():
			print ("Heap is full...")
			return

		self.curPos += 1
		self.heap[self.curPos] = item
		self.fixUp(self.curPos) 	

	def isFull(self):
		if self.curPos == Heap.HEAP_SIZE + 1:
			return True
		else:
			return False

	def fixUp(self, index):

		parentIndex = (index - 1)/2

		while parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]:
			temp = self.heap[index]
			self.heap[index] = self.heap[parentIndex]
			self.heap[parentIndex] = temp
			parentIndex = (index-1)//2

	def heapsort(self):
		for i in range(0, self.curPos+1):
			temp = self.heap[0]
			print("%d " % temp)
			self.heap[0] = self.heap[self.curPos - i]
			self.heap[self.curPos - i] = temp
			self.fixDown(0, self.curPos - i - 1)

	def fixDown(self, index, upTo):
		while index <= upTo:
			leftChild = 2*index + 1
			rightChild = 2*index + 2

			if leftChild < upTo:
				childToSwap = None
				if rightChild > upTo:
					childToSwap = leftChild
				else:
					if self.heap[leftChild] > self.heap[rightChild]:
						childToSwap = leftChild
					else:
						childToSwap = rightChild	

				if self.heap[index] < self.heap[childToSwap]:
					temp = self.heap[index]
					self.heap[index] = self.heap[childToSwap]
					self.heap[childToSwap] = temp
				else:
					break

				index = childToSwap
			else:
				break	

if __name__ == "__main__":

	heap = Heap()
	heap.insert(10)
	heap.insert(-20)
	heap.insert(0)
	heap.insert(2)

	heap.heapsort()