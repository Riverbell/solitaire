
import collections
from linkedQ import LinkedQ
from stackQ import StackQ
from playingCards import Card
from playingCards import Deck
import re
import sys


class Solitaire():
	""" Gameplan with rules """
	def __init__(self, deck):
		self.gameField = []
		self.deck = deck
		self.currentCard = None
		self.wastePile = StackQ()
		self.emptyCardSlot = '   '

	def __str__(self):
		gameField = ""
		lastRow = "-----------------------------" + "\n" + " 0   1   2   3   4   5   6  "
		rowCount = 0
		colCount = 0
		emptyCount = 0
		for row in self.gameField: 
			for col in self.gameField[rowCount]: # for each row check each col
				if rowCount == 1 and colCount != 7:
					gameField = gameField + str(col) + "-" # creating a solid line
				else:
					gameField = gameField + str(col) + " "	# adds value of that column to the gamefield
				# checks for a whole empty row
				if str(col) == "   " or str(col) == "| " + str(rowCount):
					emptyCount = emptyCount + 1
				else:
					emptyCount = 0
				if emptyCount == 9:		# if a whole row is empty, don't print it!
					return gameField + "\n" + lastRow
				colCount = colCount + 1
				

			# adds new line after each row
			gameField = gameField + "\n"
			rowCount = rowCount + 1
			colCount = 0
			#emptyCount = 0
		return gameField + lastRow
		
	def createGameField(self):
		#creates a grid 
		colNum = 8
		rowNum = 22
		i = 0
		for row in range(rowNum): 
			self.gameField.append([])
			for col in range(colNum):
				self.gameField[row].append([])
				#s = str(row) + str(col)
				if col == 7: # creates a vertical line with numbers for each row
					s = '| ' + str(i)
				elif row == 1:
					s = '---'
				else:
					s = self.emptyCardSlot
				self.gameField[row][col] = s
			i = i + 1


	def placeCards(self):
		# places the cards on the game field
		for row in range(2,len(self.gameField)):
			for col in range(len(self.gameField[0])-1):
				if row == col+2: # +2 since the gamefield has been pushed down two rows
					card = self.deck.getCard()
					self.gameField[row][col] = card.flipCard()
				elif row < col+2:
					card = self.deck.getCard()
					self.gameField[row][col] = card
				else:
					self.gameField[row][col] = self.emptyCardSlot

		self.currentCard = self.deck.getCard().flipCard()
		self.gameField[0][0] = '***'
		self.gameField[0][1] = self.currentCard
		self.gameField[0][3] = Card(0, 'clubs').flipCard()
		self.gameField[0][4] = Card(0, 'diamonds').flipCard()
		self.gameField[0][5] = Card(0, 'hearts').flipCard()
		self.gameField[0][6] = Card(0, 'spades').flipCard()


	def printGame(self):
		print("")
		print(self)
		print("")

	def printDeck(self):
		print("PRINTS THE DECK")
		print(self.deck)

	def printInstructions(self):
		# prints the instructions of use
		pass

	def drawCard(self):
		# if the deck is not empty:
		# draws one card from the deck and places it face up
		# face up is in the self.currentCard
		# for each draw, call putToWaste with the previous currentCard

		if self.currentCard != "!":
			if self.currentCard != None and self.currentCard != self.emptyCardSlot:
				self.putToWaste(self.currentCard)

			self.currentCard = self.deck.getCard() # draws a new card

			if self.currentCard == "!": # if the deck is empty, it's time to recycle
				print("Deck is empty!")
				self.currentCard = None 
				self.recycleWaste()
			else:
				#print("Deck is not empty! Draws current card:")
				#print(self.currentCard.flipCard())
				self.gameField[0][1] = self.currentCard.flipCard() # places the current card face up on the field


	def putToWaste(self, card):
		# puts the card into the waste pile
		self.wastePile.put(card)
		print("Wastepile:")
		if self.wastePile.isEmpty():
			print("Wastepile empty")
		else:
			print(self.wastePile)
		#print("Wastepile:")
		#for card in self.wastePile:
		#	print(card)

	def recycleWaste(self):
		# called if the deck is empty
		# puts the cards in waste pile back into the deck 
		print("Empty deck - time to recycle!")
		tempWaste = StackQ()
		while self.wastePile.isEmpty() != True:
			card = self.wastePile.get()
			tempWaste.put(card)
		while tempWaste.isEmpty() != True:
			card = tempWaste.get()
			self.deck.putCard(card.flipCard())

		print("Recycling done. Wastepile:")
		print(self.wastePile)
		print("Deck:")
		print(self.deck)
		self.drawCard()


	def checkIfValidMove(self,r1,c1,r2,c2):
		# checks if the prompted move is valid
		# the moved card must be one rank lower and different color
		# if valid move, fire moveCard
		# IMPORTANT!! Coordinates needs to be translated later, depending on what coordinates the user inputs
		validMove = None
		movingCard = self.gameField[r1][c1]
		destination = self.gameField[r2][c2]
		destinationParent = self.gameField[r2-1][c2]
		if destination == self.emptyCardSlot:
			destinationEmpty = True
		else:
			destinationEmpty = False
		if destinationParent != self.emptyCardSlot and destinationParent != '---': # if the destination parent is not empty, check the colors
			if destinationEmpty == True and movingCard.color == destinationParent.color:
				sameColor = True
			elif destinationEmpty == True and movingCard.color != destinationParent.color:
				sameColor = False
		else:
			sameColor = None

		# a version of this should be in the checkUserInput

		# if the card is being placed in one of the foundations
		# here can only a card of same suit and one rank higher be placed
		if r2 == 0 and c2 >= 3 and c2 <= 6:
			#print("You're trying to put a card into one of the foundations")
			if movingCard.suit == destination.suit:
				if movingCard.rank == destination.rank + 1:
					validMove = True
				else:
					validMove = False
			else:
				validMove = False
		# anywhere on the field, the goal spot needs to be after a card
		# the card being placed must be of the opposite color, and one rank lower
		# if it's the 'first' row, kings can be placed on an empty sport
		elif r2 >= 2 and c2 >= 0 and c2 <= 6:
			if r2 == 2 and destinationEmpty == True and movingCard.rank == 13:
				#print("You're trying to put a king into and empty spot")
				validMove = True
			elif destinationEmpty == True and sameColor == False and movingCard.rank == destinationParent.rank -1:
				#print("yo")
				validMove = True
			else: 
				#print("Hmm")
				validMove = False
		else:
			validMove = False

		# this should be here
		if validMove == True:
			print("It was a valid move")
			self.moveCard(r1,c1,r2,c2)
		elif validMove == False:
			print("It was not a valid move")
		print("Wastepile:")
		if self.wastePile.isEmpty():
			print("Wastepile empty")
		else:
			print(self.wastePile)

	def moveCard(self,r1,c1,r2,c2):
		# places a card on top of the other
		# only fired if the move is valid
		# if it's the 'currentCard' being moved, show th previous 'currentCard'
		# removes the movingCard from its original position
		movingCard = self.gameField[r1][c1]
		if r1 == 0 and c1 == 1:
			if not self.wastePile.isEmpty():
				self.currentCard = self.wastePile.get()
			elif self.wastePile.isEmpty():
				self.currentCard = self.emptyCardSlot
			self.gameField[r1][c1] = self.currentCard
		else:
			self.gameField[r1][c1] = self.emptyCardSlot
			self.openPrevCard(r1,c1)
		self.gameField[r2][c2] = movingCard
		

	def checkCardChildren(self):
		# or moveCardChilrden??
		# checks if the card to move has children 
		# if so, moves them along
		# maybe moveCard can check for children? if so fire this func
		pass

	def openPrevCard(self,r,c):
		if self.gameField[r-1][c] != '---':
			self.gameField[r-1][c].flipCard()


	def getuserInput(self):
		# prompts the user for input
		# fires checkUserInput
		validInput = False
		while validInput == False:
			print("\nWhat is your move?")
			print("In the form: 'rowNumber,colNumber-rowNumber,colNumber' or 'draw'")
			userInput = str(raw_input("Your move: "))
			validInput = self.checkUserInput(userInput)

	def checkUserInput(self,userInput):
		# checks if the user input is valid
		# if the coordinates are valid coordinates
		
		if userInput == "draw" or userInput == "Draw" or userInput == "D" or userInput == "d":
			self.drawCard()
			return True
		elif userInput == "exit" or userInput == "Exit" or userInput == "e" or userInput == "E":
			self.endGame()
			return True
		#elif userInput:
		#	pass
		else:
			coord = re.split(r'[\D](?=[\d])', userInput)
			#print(coord)
			try:
				self.checkIfValidMove(int(coord[0]),int(coord[1]),int(coord[2]),int(coord[3]))
				return True
			except:
				print("Those were not valid coordinates")
				return False

	def checkWin(self):
		# checks after each move if the user has won the game
		# if game won, end the game
		if self.gameField[0][3].rank == 13 and self.gameField[0][4].rank == 13 and self.gameField[0][5].rank == 13 and self.gameField[0][6].rank == 13:
			return True
		else:
			return False

	def endGame(self):
		# ends the game 
		print("Exits game.")
		sys.exit()


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
