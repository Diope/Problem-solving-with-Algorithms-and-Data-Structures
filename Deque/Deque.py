class Deque:
	def __init__(self):
		self.items = []

	def is_enpty():
		return self.items == []

	def add_front(self, item):
		self.items.append(item)

	def add_rear(self, item):
		self.items.insert(0,item)

	def remove_front(self):
		return self.items.pop()

	def remove_rear(self):
		return self.items.pop(0)
		#I don't think this will work.

	def size(self):
		return len(self.items)