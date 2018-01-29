class DirectedGraph:
	def __init__(self):
		self.graph = {}

	def add_vertex(self, vertex):
		if vertex not in self.graph:
			self.graph[vertex] = []

	def delete_vertex(self, vertex):
		self.graph.pop(vertex, None)

		try:
			for key, value_list in self.graph.items():
				value_list.remove(vertex)
		except:
			pass	# vertex not present in value_list

	def add_edge(self, from_edge, to_edge):
		if from_edge not in self.graph:
			self.graph[from_edge] = [to_edge]
		else:
			self.graph[from_edge].append(to_edge)

		if to_edge not in self.graph:
			self.graph[to_edge] = []

	def delete_edge(self, from_edge, to_edge):
		self.graph[from_edge].remove(to_edge)

	def print_graph(self):
		for key, value_list in self.graph.items():
			print(key, ":", value_list)
		print()

	def BFS(self, start_vertex, end_vertex):
		queue = [start_vertex]
		visited = [start_vertex]
		trace = ""

		while(len(queue) != 0):
			popped = queue.pop(0)
			trace = trace + " " + str(popped) 

			if popped == end_vertex:
				return [True, trace]

			for adjacent_edge in self.graph[popped]:
				if adjacent_edge not in visited:
					visited.append(adjacent_edge)
					queue.append(adjacent_edge)

		return [False, trace]

	def DFS(self, start_vertex, end_vertex):
		stack = [start_vertex]
		visited = [start_vertex]
		trace = ""

		while(len(stack) != 0):
			popped = stack.pop(-1)
			trace = trace + " " + str(popped)

			if popped == end_vertex:
				return [True, trace]

			for adjacent_edge in self.graph[popped]:
				if adjacent_edge not in visited:
					visited.append(adjacent_edge)
					stack.append(adjacent_edge)

		return [False, trace]

	def detect_cycle(self, start_vertex):
		stack = [start_vertex]

		while(len(stack) != 0):
			popped = stack.pop(-1)

			
			for adjacent_edge in self.graph[popped]:
				if adjacent_edge in stack:
					return True
				
				stack.append(adjacent_edge)

		return False

graph = DirectedGraph()

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(4, 5)
graph.add_edge(5, 6)

graph.print_graph()

isPath = graph.BFS(0, 5)
print(isPath)
isPath = graph.BFS(0, 3)
print(isPath)
isPath = graph.BFS(3, 0)
print(isPath)

isPath = graph.BFS(0, 5)
print(isPath)
isPath = graph.BFS(0, 3)
print(isPath)
isPath = graph.BFS(3, 0)
print(isPath)

graph.add_edge(2, 0)
isCycle = graph.detect_cycle(0)
print(isCycle)
isCycle = graph.detect_cycle(5)
print(isCycle)
