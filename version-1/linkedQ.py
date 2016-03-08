class Node():
	"""Klassen består av noder som håller ihop listan genom att peka på nästa nod."""
	def __init__(self, value, next = None):
		"""Skapar klassens attribut."""
		self.value = value
		self.next = next

class LinkedQ():
	"""Arrangerar en kö."""
	def __init__(self, first = None, last = None):
		"""Vi skapar klassens attribut."""
		self.first = first
		self.last = last

	def __str__(self):
		"""Metoden returnerar en sträng som innehåller användarens inmatade kort."""
		s = ""
		p = self.first
		while p != None:
			s = s + str(p.value) + " "
			p = p.next
		return s

	def put(self,x):
		"""Metoden tar emot variabeln x och placerar den sist i kön."""
		if self.isEmpty(): # Om lista är tom skapar vi en nod som är listans första och sista nod. 
			newNode = Node(x)
			self.first = newNode
			self.last = newNode
		else: # Om listan inte är tom skapar vi en ny nod. Noden är den sista i listan och pekar på None.
			newNode = Node(x)
			self.last.next = newNode
			self.last = newNode

	def get(self):
		"""Metoden plockar ut och returnerar det som står först i listan, dvs i kön."""
		if not self.isEmpty(): # Om listan inte är tom sparar vi det första elementet i listan som variabeln 'first' och ersätter det genom att ge 
			first = self.first # elementet nummer 2 första platsen.
			self.first = self.first.next
			return first.value # Vi returnerar det första elementet.
		elif self.isEmpty():
			return "!"

	def peek(self):
		if not self.isEmpty():  
			first = self.first 
			return first.value 
		else:
			return "!"

	def isEmpty(self):
		"""Metoden tar emot en lista och returnerar True om kön (listan) är tom, i övriga fall returnerar metoden False."""
		if self.first == None: # Om listan saknar ett första element är listan tom och metoden returnerar 'True'.
			return True
		else:
			return False # I övriga fall returnerar metoden 'False'.
