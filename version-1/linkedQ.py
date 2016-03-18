class Node():
	"""Nodes have a value and a pointer. The pointer keeps the list (queue) together"""
	def __init__(self, value, next = None):
		self.value = value
		self.next = next

class LinkedQ():
	"""Arranges a queue"""
	def __init__(self, first = None, last = None):
		self.first = first
		self.last = last

	def __str__(self):
		"""Returns a string with the users input"""
		s = ""
		p = self.first
		while p != None:
			s = s + str(p.value) + " "
			p = p.next
		return s

	def put(self,x):
		"""Takes the variable x as parameter and places it last in the queue"""
		if self.isEmpty(): # If the list is empty, create a node which is the first and last node in the list
			newNode = Node(x)
			self.first = newNode
			self.last = newNode
		else: # If the list isn't empty, create new node. Last in the list and points to None
			newNode = Node(x)
			self.last.next = newNode
			self.last = newNode

	def get(self):
		"""Takes the first item of the list out of the list and returns it"""
		if not self.isEmpty(): 
			first = self.first 
			self.first = self.first.next
			return first.value 
		elif self.isEmpty():
			return "!"

	def peek(self):
		if not self.isEmpty():  
			first = self.first 
			return first.value 
		else:
			return "!"

	def isEmpty(self):
		"""Takes a list and checks if it's empty or not"""
		if self.first == None: 
			return True
		else:
			return False 
