
import collections
from linkedQ import LinkedQ
from playingCards import Deck



class Solitaire():
	""" Gameplan with rules """
	def __init__(self, deck):
		#self.gameField = []
		self.gameField = collections.defaultdict(list)

	def __str__(self):
		s = ""
		i = 0
		for l in self.gameField:
			for j in self.gameField[i]:
				s = s + str(j)
				s = s + "\n"
			s = s + "*"
			i = i + 1
		return s
		

	def createGameField(self):
		for i in range(7):
			self.gameField[i] = '*'
			for j in range(2):
				self.gameField[i] = '-'
		#self.gameField[2][2] = '*'
		print(self.gameField)

	def createGameField1(self):
		""" Gamefield has seven rows """
		for i in range(7):
			self.gameField.append([])
		col = 0
		while col < 7:
			for row in range(0,col+1):
				print(row, col)
				card = deck.drawCard()
				# if it's the last card of that line, flip it
				if row == col:
					self.gameField[col].append(card.flipCard())
				else:
					self.gameField[col].append(card)
			col = col + 1


	def placeCards(self):
		# places the cards on the game field
		pass

	def drawCard(self):
		# draws one card from the deck
		pass


if __name__ == '__main__':
	deck = Deck()
	deck.createStdDeck()
	deck.printDeck()
	print("============= SHUFFLED DECK:")
	deck.shuffleDeck()
	deck.printDeck()

	game = Solitaire(deck)
	print("============= CREATED FIELD:")
	game.createGameField()
	#print(game)
