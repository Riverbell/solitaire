from random import shuffle
from linkedQ import LinkedQ

class Card():
	""" Creates the card 
		Attributes: 
			rank (number), 
			color (red/black), 
			suit (heart/clubs etc)
			face card (jacks, queens, kings)
		Creates on initialization
	"""
	def __init__(self, rank, suit):
		# create card on initialiation
		self.checkRank(rank)
		self.checkSuit(suit)
		self.checkColor()
		self.checkFace()
		self.faceDown = True

	def __str__(self):
		""" Returns the attributes of the object as a string """
		if self.faceDown == False:
			if len(str(self.rank)) == 1:
				s = ' ' + str(self.rank) + str(self.suit)[0].upper()
			else:
				s =  str(self.rank) + str(self.suit)[0].upper()
			#+ " (" + str(self.color) + str(self.faceCard) + ") "
		elif self.faceDown == True:
			s = "***"
		return s

	def checkRank(self, rank):
		# checks if the rank of the card is valid
		try:
			rank = int(rank)
			if rank < 14 and rank > 0:
				self.rank = rank
			else: 
				raise ValueError('That is not a valid card rank')
		except ValueError as error:
			print('caught this error: ' + error)


	def checkSuit(self, suit):
		# checks if the suit of the card is valid
		try: 
			if suit == 'clubs' or suit == 'club':
				self.suit = 'clubs'
			elif suit == 'diamonds' or suit == 'diamond':
				self.suit = 'diamonds'
			elif suit == 'hearts' or suit == 'heart':
				self.suit = 'hearts'
			elif suit == 'spades' or suit == 'spade':
				self.suit = 'spades'
			else:
				raise ValueError('That is not a valid suit')
		except ValueError as error:
			print('Caught this error: ' + error)


	def checkColor(self):
		# sets the color of the card, based on its suit
		if self.suit == 'diamonds' or self.suit == 'hearts':
			self.color = 'red'
		elif self.suit == 'clubs' or self.suit == 'spades':
			self.color = 'black'

	def checkFace(self):
		# sets the attribute faceCard to true or false depending on its rank 
		if self.rank > 10:
			self.faceCard = True
		elif self.rank < 11:
			self.faceCard = False

	def flipCard(self):
		if self.faceDown == True:
			self.faceDown = False
		elif self.faceDown == False:
			self.faceDown = True
		return self


class Deck():
	""" Creates the Deck
		52 cards
		4 suits (clubs diamonds hearts spades)
		1-13 in rank
	"""
	def __init__(self):
		#temporary deck to be able to use shuffle
		self.tempDeck = []
		self.deck = LinkedQ()

	def printDeck(self):
		print(self.deck)

	def createStdDeck(self):
		# Creates a standard deck, with 52 cards in four suits
		suits = ['clubs', 'diamonds', 'hearts', 'spades']
		for suit in suits:
			for i in range(1,14):
				newCard = Card(i, suit)
				self.tempDeck.append(newCard)
				self.deck.put(newCard)

	def shuffleDeck(self):
		# Shuffles the deck randomly
		shuffle(self.tempDeck)
		self.deck = LinkedQ()
		for card in self.tempDeck:
			self.deck.put(card)

	def sortDeck(self):
		pass

	def drawCard(self):
		card = self.deck.get()
		#print(card)
		return card