class UndirectedGraph:
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
			self.graph[to_edge] = [from_edge]
		else:
			self.graph[to_edge].append(from_edge)

	def delete_edge(self, from_edge, to_edge):
		self.graph[from_edge].remove(to_edge)
		self.graph[to_edge].remove(from_edge)

	def print_graph(self):
		for key, value_list in self.graph.items():
			print(key, ":", value_list)
		print()

graph = UndirectedGraph()

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

graph.print_graph()
