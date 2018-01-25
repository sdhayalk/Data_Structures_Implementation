class Queue:
	def __init__(self):
		self.list = []

	def enqueue(self, element):
		self.list.append(element)

	def dequeue(self):
		return self.list.pop(0)

	def front(self):
		return self.list[0]

	def rear(self):
		return self.list[-1]

	def isEmpty(self):
		return self.list == []

	def size(self):
		return len(self.list)