class Stack:
	def __init__(self):
		self.list = []

	def push(self, element):
		self.list.append(element)

	def pop(self):
		return self.list.pop()	# or return self.list.pop(-1)

	def peek(self):
		return self.list[-1]

	def isEmpty(self):
		return self.list == []

	def size(self):
		return len(self.list)
