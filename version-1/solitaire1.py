
import collections
from linkedQ import LinkedQ
from playingCards import Deck


class Solitaire():
	""" Gameplan with rules """
	def __init__(self, deck):
		self.gameField = []
		#self.gameField = collections.defaultdict(list)

	def __str__(self):
		s = ""
		i = 0
		for l in self.gameField:
			for j in self.gameField[i]:
				s = s + str(j) + " "
				#s = s + "\n"
			s = s + "\n"
			i = i + 1
		return s
		
	def createGameField(self):
		#creates a grid
		colNum = 7
		rowNum = 9
		for row in range(rowNum):
			self.gameField.append([])
			for col in range(colNum):
				self.gameField[row].append([])
				#s = str(row) + str(col)
				s = ' - '
				self.gameField[row][col] = s


	def placeCards(self):
		# places the cards on the game field
		for row in range(2,len(self.gameField)):
			for col in range(len(self.gameField[0])):
				card = deck.drawCard()
				if row == col+2: # +2 since the gamefield has been pushed down two rows
					self.gameField[row][col] = card.flipCard()
				elif row < col+2:
					self.gameField[row][col] = card
				else:
					self.gameField[row][col] = '   '

		self.gameField[0][0] = '***'
		self.gameField[0][1] = deck.drawCard().flipCard()
		self.gameField[0][3] = ' C '
		self.gameField[0][4] = ' D '
		self.gameField[0][5] = ' H '
		self.gameField[0][6] = ' S '


	def printGame(self):
		print(self)

	def drawCard(self):
		# draws one card from the deck and places it face up
		pass

	def checkIfValidMove(self):
		# checks if the prompted move is valid
		pass

	def placeCard(self):
		# places a card on top of the other
		pass


	def userInput(self):
		pass

	def checkUserInput(self):
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
	print()
	game.createGameField()
	game.placeCards()
	game.printGame()
