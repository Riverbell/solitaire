
import collections
from linkedQ import LinkedQ
from playingCards import Deck


class Solitaire():
	""" Gameplan with rules """
	def __init__(self, deck):
		self.gameField = []

	def __str__(self):
		s = ""
		count = 0
		for row in self.gameField:
			for col in self.gameField[count]:
				s = s + str(col) + " "
			# adds new line after each row
			s = s + "\n"
			count = count + 1
		return s
		
	def createGameField(self):
		#creates a grid with 7 columns and 9 rows
		colNum = 7
		rowNum = 9
		for row in range(rowNum):
			self.gameField.append([])
			for col in range(colNum):
				self.gameField[row].append([])
				#s = str(row) + str(col)
				s = '   '
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

	def printInstructions(self):
		# prints the instructions of use
		pass

	def drawCard(self):
		# draws one card from the deck and places it face up
		pass

	def checkIfValidMove(self):
		# checks if the prompted move is valid
		# the moved card must be one rank lower and different color
		# if valid move, fire moveCard
		pass

	def moveCard(self):
		# places a card on top of the other
		# only fired if the move is valid
		pass

	def checkCardChildren(self):
		# or moveCardChilrden??
		# checks if the card to move has children 
		# if so, moves them along
		# maybe moveCard can check for children? if so fire this func
		pass

	def getuserInput(self):
		# prompts the user for input
		# fires checkUserInput
		pass

	def checkUserInput(self):
		# checks if the user input is valid
		# if the coordinates are valid coordinates
		pass

	def checkWin(self):
		# checks after each move if the user has won the game
		# if game won, end the game
		pass

	def endGame(self):
		# ends the game 
		pass


if __name__ == '__main__':
	deck = Deck()
	deck.createStdDeck()
	#deck.printDeck()
	#print("============= SHUFFLED DECK:")
	deck.shuffleDeck()
	#deck.printDeck()

	game = Solitaire(deck)
	print("============= CREATED FIELD:")
	print()
	game.createGameField()
	game.placeCards()
	game.printGame()
