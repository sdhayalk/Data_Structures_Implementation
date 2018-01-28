class TrieNode:
	def __init__(self, data, end_of_word=False):
		self.data = data
		self.children_map = {}
		self.end_of_word = end_of_word

	def create_child(self, data, end_of_word=False):
		if data not in self.children_map:
			self.children_map[data] = TrieNode(data, end_of_word=end_of_word)

	def attach_child(self, child):
		if child.data not in self.children_map:
			self.children_map[child.data] = child

	def update_end_of_word(self, new_end_of_word):
		self.end_of_word = new_end_of_word

	def get_data(self):
		return self.data
