"""
'Python-is-Easy' Project #3 (Pick a Card Game)
DESCRIPTION: 
This is the third project in the 'Python is Easy' course from Pirple.

The assignment is to pick a favourite card game and create it using Python code.

I love poker, so I am going to create that game without considering how hard or easy it will be. 


Here goes!

"""



from random import shuffle
import os
import time


cardValues = {} # a dictionary showing each card as Key and a Tuple as value.  Tuple entities are (Card, Suit, Value).  Example: 2 of hearts is "2h":(2,'h',2)
Players = () # needs to be a tuple to keep the order of players consistent.
Pot = 0
communityCards = []
smallBlind = 10
bigBlind = 20


# create deck

def creatDeck():

	Deck = []

	faceValues = ["J","Q","K","A"]
	cardSuit = ["h","d","s","c"] # 4 suits.  h = heart, d = diamond, s = spade, c = clover


	for suit in cardSuit:
		for card in range(2,11):
			Deck.append(str(card)+(suit))
			cardValues[str(card)+(suit)] = (card,suit,int(card))
		for card in faceValues:
			Deck.append(card+suit)
			if card == "J":
				cardValues[card+suit] = (card,suit,11)
			if card == "Q":
				cardValues[card+suit] = (card,suit,12)
			if card == "K":
				cardValues[card+suit] = (card,suit,13)
			if card == "A":
				cardValues[card+suit] = (card,suit,14)
									
	shuffle(Deck)
	return Deck



cardDeck = creatDeck()

print(cardDeck,"\n\n")
print(cardValues)



class Player:
	"""docstring for Player"""
	def __init__(self, name, hand = [], money=1000, isDealer=0):
		self.name = name
		self.money = money
		self.hand = hand
		self.isDealer = isDealer
		# self.score = self.setScore()
		self.folded = 0
		self.bet = 0
	 	

	def __str__(self): #print (player)
		currentHand = ""
		for card in self.hand:
			currentHand += str(card) + " "
		# print(currentHand)		
		finalStatus = currentHand + "score: " + str(self.score)
		# finalStatus = self.name

		return finalStatus

	# def setScore(self):
	# 	self.score = 0
	# 	aceCounter = 0

	# 	for card in self.hand:
	# 		self.score += cardValues[card][2]
	# 		if card == "A":
	# 			aceCounter += 1
	# 		if self.score > 21 and aceCounter != 0:
	# 			self.score -= 10
	# 			aceCounter -= 1
	# 	return self.score

	def dealCard(self,card):
		self.hand.append(card)
 	 
	def betMoney(self,amount):
		# global Pot
		self.money -= amount #Money 100; (bet(20)
		self.bet += amount # Money 100->80 bet 0 ->20
		# Pot += amount

	# def pokerHand(self):


def setTable():
	setPlayersCount = input("Welcome to Texas Hold'em!\n\nHow many players are joining today? ")
	if 2 > setPlayersCount > 10:
		setPlayersCount = input("There should be at least TWO and not more than TEN players!\n\nHow many players are joining today?")
	PlayersList = []
	print("Great! Let's get all your names.\n\n")
	time.sleep(2)
	os.system("cls")
	
	for n in range(int(setPlayersCount)):
		print("Player ",n+1,end="")
		playersName = input(", please type in your name below: \n\n")
		PlayersList.append(playersName)
		# playersName = Player()
		time.sleep(1)
		os.system("cls")
	return PlayersList


def betRound():
	highestBet, PlayerID, haveFolded = checkBets()
	# highestBet = 0
	# PlayerID = -1
	# for s in activePlayers:
	# 	if activePlayers[s].bet > highestBet:
	# 		highestBet = activePlayers[s].bet
	# 		PlayerID = int(s)
	if highestBet > 0:
		countTrip = 1 # this is used to check if the loop reaches the final player, and if the function needs to run again to collect bets from other players.
		# IDCheck = PlayerID
		while countTrip < len(activePlayers)+2 or haveFolded < len(activePlayers)-1:
			# print("after while looop ...... before for loop.....")
			for r in circle_iter(activePlayers,PlayerID+1):
				# print("after for loop.......	")
				# print("\n\nhighest bet is ",highestBet,"\n\nplayers bet is ",r.bet)
				# print("\n\n",activePlayers["1"].name," bet is ",activePlayers["1"].bet)
				# print("\n\n",activePlayers["2"].name," bet is ",activePlayers["2"].bet)
				# print("\n\n",activePlayers["3"].name," bet is ",activePlayers["3"].bet)
				# print("\n\n",activePlayers["4"].name," bet is ",activePlayers["4"].bet)
				# print("\n\n",activePlayers["5"].name," bet is ",activePlayers["5"].bet)
				# print("\n\n",activePlayers["6"].name," bet is ",activePlayers["6"].bet)
				# print("\n\n",activePlayers["0"].name," bet is ",activePlayers["0"].bet)
				if r.folded == 1:
					countTrip += 1
					continue
				if r.bet == highestBet:
					print("\n\n",r.name," The current bet is ", highestBet,"\n\n")
					playerFinalChoice = input("Choose an option.\n[1] Check\n[2] Raise\n[3] Fold\n\n")
					if playerFinalChoice == "1":
						print("1 final choice")
						updateBalances()
						countTrip = len(activePlayers)+3
						break
					if playerFinalChoice == "2":
						playerRaise = int(input("How much do you want to raise?\n\n"))
						if playerRaise < highestBet*1.5:
							print("Amount must be at least ",highestBet*1.5,"\n\n")
							playerRaise = int(input("How much do you want to raise?\n\n"))
						newBet = playerRaise - r.bet
						r.betMoney(newBet)
						highestBet = playerRaise
						print("2 final choice")
						highestBet, PlayerID = checkBets()
						countTrip = 1
						continue
					if playerFinalChoice == "3":
						r.folded = 1
						haveFolded += 1 
						print("3 final choice")
						updateBalances()
						countTrip = len(activePlayers)+3
						break
				if countTrip == len(activePlayers):
					print("count trip has been reacheeeeeeed")
					print("\n\n",r.name," The current bet is ", highestBet,"\n\n")
					playerChoice = input("Choose an option.\n[1] Call\n[2] Raise\n[3] Fold\n\n")
					if playerChoice == "2":
						playerRaise = int(input("How much do you want to raise?\n\n"))
						if playerRaise < highestBet*1.5:
							print("Amount must be at least ",highestBet*1.5,"\n\n")	
							playerRaise = int(input("How much do you want to raise?\n\n"))
						newBet = playerRaise - r.bet
						r.betMoney(newBet)
						highestBet = playerRaise
					if playerChoice == "1":
						callBet = highestBet - r.bet
						r.betMoney(callBet)
					if playerChoice == "3":
						r.folded = 1
						haveFolded += 1
						print("3 players choice fold")
						if haveFolded == len(activePlayers)-1:
							updateBalances()
							checkWin()
							countTrip = len(activePlayers)+3
							break
					countTrip = 1
					continue
				print("\n\n",r.name," The current bet is ", highestBet,"\n\n")
				playerChoice = input("Choose an option.\n[1] Call\n[2] Raise\n[3] Fold\n\n")
				if playerChoice == "2":
					playerRaise = int(input("How much do you want to raise?\n\n"))
					if playerRaise < highestBet*1.5:
						print("Amount must be at least ",highestBet*1.5,"\n\n")	
						playerRaise = int(input("How much do you want to raise?\n\n"))
					newBet = playerRaise - r.bet
					r.betMoney(newBet)
					highestBet = playerRaise
					countTrip += 1
				if playerChoice == "1":
					callBet = highestBet - r.bet
					r.betMoney(callBet)
					countTrip += 1
				if playerChoice == "3":
					r.folded = 1
					haveFolded += 1
					print("3 players choice fold")
					if haveFolded == len(activePlayers)-1:
						updateBalances()
						checkWin()
						countTrip = len(activePlayers)+3
						print("is this where it for stuck???????????????????")
						break
					countTrip += 1
	# if highestBet == 0:
	# 	countTrip = 1 # this is used to check if the loop reaches the final player, and if the function needs to run again to collect bets from other players.
	# 	# IDCheck = PlayerID
	# 	while countTrip < len(activePlayers)+2 or haveFolded < len(activePlayers)-1:
	# 		# print("after while looop ...... before for loop.....")
	# 		for r in circle_iter(activePlayers,PlayerID+1):
	# 			# print("after for loop.......	")
	# 			# print("\n\nhighest bet is ",highestBet,"\n\nplayers bet is ",r.bet)
	# 			# print("\n\n",activePlayers["1"].name," bet is ",activePlayers["1"].bet)
	# 			# print("\n\n",activePlayers["2"].name," bet is ",activePlayers["2"].bet)
	# 			# print("\n\n",activePlayers["3"].name," bet is ",activePlayers["3"].bet)
	# 			# print("\n\n",activePlayers["4"].name," bet is ",activePlayers["4"].bet)
	# 			# print("\n\n",activePlayers["5"].name," bet is ",activePlayers["5"].bet)
	# 			# print("\n\n",activePlayers["6"].name," bet is ",activePlayers["6"].bet)
	# 			# print("\n\n",activePlayers["0"].name," bet is ",activePlayers["0"].bet)
	# 			if r.folded == 1:
	# 				countTrip += 1
	# 				continue
	# 			if r.bet == highestBet:
	# 				print("\n\n",r.name," The current bet is ", highestBet,"\n\n")
	# 				playerFinalChoice = input("Choose an option.\n[1] Check\n[2] Raise\n[3] Fold\n\n")
	# 				if playerFinalChoice == "1":
	# 					print("1 final choice")
	# 					updateBalances()
	# 					countTrip = len(activePlayers)+3
	# 					continue
	# 				if playerFinalChoice == "2":
	# 					playerRaise = int(input("How much do you want to raise?\n\n"))
	# 					if playerRaise < highestBet*1.5:
	# 						print("Amount must be at least ",highestBet*1.5,"\n\n")
	# 						playerRaise = int(input("How much do you want to raise?\n\n"))
	# 					newBet = playerRaise - r.bet
	# 					r.betMoney(newBet)
	# 					highestBet = playerRaise
	# 					print("2 final choice")
	# 					highestBet, PlayerID = checkBets()
	# 					countTrip = 1
	# 					continue
	# 				if playerFinalChoice == "3":
	# 					r.folded = 1
	# 					haveFolded += 1 
	# 					print("3 final choice")
	# 					updateBalances()
	# 					countTrip = len(activePlayers)+3
	# 					continue
	# 			if countTrip == len(activePlayers):
	# 				print("count trip has been reacheeeeeeed")
	# 				print("\n\n",r.name," The current bet is ", highestBet,"\n\n")
	# 				playerChoice = input("Choose an option.\n[1] Call\n[2] Raise\n[3] Fold\n\n")
	# 				if playerChoice == "2":
	# 					playerRaise = int(input("How much do you want to raise?\n\n"))
	# 					if playerRaise < highestBet*1.5:
	# 						print("Amount must be at least ",highestBet*1.5,"\n\n")	
	# 						playerRaise = int(input("How much do you want to raise?\n\n"))
	# 					newBet = playerRaise - r.bet
	# 					r.betMoney(newBet)
	# 					highestBet = playerRaise
	# 				if playerChoice == "1":
	# 					callBet = highestBet - r.bet
	# 					r.betMoney(callBet)
	# 				if playerChoice == "3":
	# 					r.folded = 1
	# 					haveFolded += 1
	# 					print("3 players choice fold")
	# 					if haveFolded == len(activePlayers)-1:
	# 						updateBalances()
	# 						checkWin()
	# 						countTrip = len(activePlayers)+3
	# 						continue
	# 				countTrip = 1
	# 				continue
	# 			print("\n\n",r.name," The current bet is ", highestBet,"\n\n")
	# 			playerChoice = input("Choose an option.\n[1] Check\n[2] Bet\n[3] Fold\n\n")
	# 			if playerChoice == "2":
	# 				playerRaise = int(input("How much do you want to bet?\n\n"))
	# 				if playerRaise < highestBet*1.5:
	# 					print("Amount must be at least ",highestBet*1.5,"\n\n")	
	# 					playerRaise = int(input("How much do you want to raise?\n\n"))
	# 				newBet = playerRaise - r.bet
	# 				r.betMoney(newBet)
	# 				highestBet = playerRaise
	# 				countTrip += 1
	# 			if playerChoice == "1":
	# 				callBet = highestBet - r.bet
	# 				r.betMoney(callBet)
	# 				countTrip += 1
	# 			if playerChoice == "3":
	# 				r.folded = 1
	# 				haveFolded += 1
	# 				print("3 players choice fold")
	# 				if haveFolded == len(activePlayers)-1:
	# 					updateBalances()
	# 					checkWin()
	# 					countTrip = len(activePlayers)+3
	# 					continue
	# 				countTrip += 1

def checkBets():
	highestBet = 0
	PlayerID = -1
	haveFolded = 0
	for s in activePlayers:
		if activePlayers[s].isDealer == 1:
			tempPlayerID = int(s)
		if activePlayers[s].folded == 1:
			haveFolded += 1
		if activePlayers[s].bet > highestBet:
			highestBet = activePlayers[s].bet
			PlayerID = int(s)
	if highestBet == 0:
		PlayerID = tempPlayerID
	return highestBet, PlayerID, haveFolded


def updateBalances():
	global Pot
	for b in activePlayers:
		Pot += activePlayers[b].bet
		activePlayers[b].bet = 0

def checkWin():
	global Pot
	for w in activePlayers:
		if activePlayers[w].folded == 0:
			# we need to check the score
			# if there is a tie, we need to split pot
			activePlayers[w].money += Pot
			print(activePlayers[w].name," has won ",Pot)
			Pot = 0





def circle_iter(items, start=1): # defines where the loop should start from active players in a round
	l = len(items)
	for i in items:
		yield items[str(start)]
		start += 1
		if start == l+1: start = 1



# Players = setTable()

Players = ("Jon","David","Simon", "George","Vange","basil")

print(Players)

# ind = 1
# for n in range(len(Players)):
# 	Player1 = Player(Player[n])
try:
	Player1 = Player(Players[0]) 
	Player2 = Player(Players[1])
	Player3 = Player(Players[2])
	Player4 = Player(Players[3])
	Player5 = Player(Players[4])
	Player6 = Player(Players[5])
	Player7 = Player(Players[6])
	Player8 = Player(Players[7])
	Player9 = Player(Players[8])
	Player10 = Player(Players[9])
except IndexError:
	pass


for p in range(len(Players)):
	if p == 9:
		activePlayers = {"1":Player1,"2":Player2,"3":Player3,"4":Player4,"5":Player5,"6":Player6,"7":Player7,"8":Player8,"9":Player9,"10":Player10}
	if p == 8:
		activePlayers = {"1":Player1,"2":Player2,"3":Player3,"4":Player4,"5":Player5,"6":Player6,"7":Player7,"8":Player8,"9":Player9}
	if p == 7:
		activePlayers = {"1":Player1,"2":Player2,"3":Player3,"4":Player4,"5":Player5,"6":Player6,"7":Player7,"8":Player8}
	if p == 6:
		activePlayers = {"1":Player1,"2":Player2,"3":Player3,"4":Player4,"5":Player5,"6":Player6,"7":Player7}
	if p == 5:
		activePlayers = {"1":Player1,"2":Player2,"3":Player3,"4":Player4,"5":Player5,"6":Player6}
	if p == 4:
		activePlayers = {"1":Player1,"2":Player2,"3":Player3,"4":Player4,"5":Player5}
	if p == 3:
		activePlayers = {"1":Player1,"2":Player2,"3":Player3,"4":Player4}
	if p == 2:
		activePlayers = {"1":Player1,"2":Player2,"3":Player3}
	if p == 1:
		activePlayers = {"1":Player1,"2":Player2}


print(Player4.name,"\n\n========")
Player1.isDealer = 1 #start off with Player 1 as the dealer

# deal2test = [cardDeck.pop(),cardDeck.pop()]

time.sleep(1)


# Player1.hand = [cardDeck.pop()]
# activePlayers["2"].hand = cardDeck.pop()

# Player1.dealCard(cardDeck.pop())



# print(Player1.hand)
# print(Player2.hand)
# # for i in range(2):

# print(activePlayers)

# for n in activePlayers:
# 	print(activePlayers[n].isDealer,activePlayers[n].name)
# 	activePlayers[n].hand = cardDeck.pop()

# print(cardDeck)

# for p in activePlayers:
# 	print(activePlayers[p].hand, activePlayers[p].name)



# for p in Players:
# 	p = Player(cardDeck.pop())


# highestBet = max(p.bet in Players)

# print(highestBet)

# def betRound():
# 	while(True):

# for i in range(3): # deal the flop
# 	communityCards.append(cardDeck.pop())

print(str(len(communityCards))," = cards on the floor")



while(True):
	dealer = 0
	# print("how about this????????????????")
	while dealer < len(Players)+1:
		if len(communityCards) == 5:
			print(communityCards)
			# define the winner of the round
			# adjust losers and winner/s balance
			# cardDeck = creatDeck()
			communityCards = []
			dealer += 1
			for p in activePlayers:
				if activePlayers[p].isDealer == 1:
					activePlayers[p].isDealer = 0
					if p == str(len(Players)+1):
						p = -1
					activePlayers[str(int(p)+1)].isDealer = 1
			print("========= in the river=============")
		if len(communityCards) == 4:
			# if Pot == 0:
			# 	continue
			cardDeck.pop() # brun card before river
			communityCards.append(cardDeck.pop()) # deal river card
			print("========= in the turn=============")
			print(communityCards)
			betRound()
			continue
		if len(communityCards) == 3:
			# if Pot == 0:
			# 	break
			cardDeck.pop() # burn card before turn
			communityCards.append(cardDeck.pop()) # deal turn card
			print("========= in the flop=============")
			print(communityCards)
			betRound()
			continue
		else:
			for p in activePlayers:
				if activePlayers[p].isDealer == 1:
					if len(Players) - dealer == 2:
						small = int(p)
						big = 1
					if len(Players) - dealer == 1:
						small = 1
						big = 2
					else:
						small = int(p)+1
						big = int(p)+2
					activePlayers[str(small)].betMoney(smallBlind)
					activePlayers[str(big)].betMoney(bigBlind)
					for dealCards in range(2): #deal two card to each player
						for d in circle_iter(activePlayers,int(p)+1):
							if dealCards == 0:
								d.hand = [cardDeck.pop()]
							else:
								d.dealCard(cardDeck.pop())
								print(d.hand,d.name,d.bet," = BET",d.money," = BALANCE")
								# time.sleep(1)
					# dealer += 1
					# activePlayers[p].isDealer = 0
					# if p == str(len(Players)+1):
					# 	p = -1
					# activePlayers[str(int(p)+1)].isDealer = 1
					break
			cardDeck.pop() # burn one card before the flop
			for i in range(3): # deal the flop
				communityCards.append(cardDeck.pop())
			print(communityCards)
			# time.sleep(1)
			betRound()
			print("do you reach this??????????????")



# 	Player1.play(firstHand)
# 	House.play(secondHand)

# 	Bet = int(input("Please enter your bet: "))

# 	Player1.betMoney(Bet)

# 	print(cardDeck)
# 	print(Player1,Player1.money)
# 	printHouse(House)

# 	if Player1.hasBlackjack():
# 		if House.hasBlackjack():
# 			Player1.draw()
# 		else:
# 			Player1.win(True)
# 	else:
# 		while(Player1.score < 21):
# 			action = input("Do you want another card? (y/n)?: ")
# 			if action == "y":
# 				Player1.hit(cardDeck.pop())
# 				print(Player1)
# 				printHouse(House)
# 			else:
# 				break
# 		while (House.score < 17):
# 			print(House)
# 			House.hit(cardDeck.pop())
		
# 		if Player1.score > 21:
# 			if House.score > 21:
# 				Player1.draw()
# 			else:
# 				Player1.win(False)
		
# 		elif Player1.score > House.score:
# 			Player1.win(True)

# 		elif Player1.score == House.score:
# 			Player1.draw()

# 		else:
# 			if House.score > 21:
# 				Player1.win(True)
# 			else:
# 				Player1.win(False)







'''


##############  BLACKJACK BELOW   ##############




class Player:

	def __init__ (self,hand = [] ,money = 100):
		self.hand = hand
		self.score = self.setScore()
		self.money = money
		self.bet = 0

	def __str__(self): #print (player)
		currentHand = ""
		for card in self.hand:
			currentHand += str(card) + " "

		finalStatus = currentHand + "score: " + str(self.score)

		return finalStatus

	def setScore(self):

		self.score = 0
		aceCounter = 0

		faceCardsDict = {"A":11,"J":10,"K":10,"Q":10,"10":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2}
		for card in self.hand:
			self.score += faceCardsDict[card]
			if card == "A":
				aceCounter += 1
			if self.score > 21 and aceCounter != 0:
				self.score -= 10
				aceCounter -= 1
		return self.score

	def hit(self,card):
		self.hand.append(card)
		self.score = self.setScore()

	def play(self,newHand):
		self.hand = newHand
		self.score = self.setScore()

	def betMoney(self,amount):
		self.money -= amount #Money 100; (bet(20)
		self.bet += amount # Money 100->80 bet 0 ->20

	def win(self,result):
		if result == True:
			if self.score == 21 and len(self.hand) == 2:
				self.money += 2.5*self.bet
			else:
				self.money += 2*self.bet
			self.bet = 0
		else:
			self.bet = 0
	def draw(self):
		self.money += self.bet
		self.bet = 0

	def hasBlackjack(self):
		if self.score == 21 and len(self.hand) == 2:
			return True
		else:
			return False

def printHouse(House):
	for card in range(len(House.hand)):
		if card == 0:
			print("#",end=" ")
		elif card == len(House.hand) - 1:
			print(House.hand[card])
		else:
			print(House.hand[card],end=" ")


cardDeck = creatDeck()

firstHand = [cardDeck.pop(),cardDeck.pop()]
secondHand = [cardDeck.pop(),cardDeck.pop()]

Player1 = Player(firstHand)
House = Player(secondHand)

cardDeck = creatDeck()

while(True):
	if len(cardDeck) < 20:
		cardDeck = creatDeck()
	firstHand = [cardDeck.pop(),cardDeck.pop()]
	secondHand = [cardDeck.pop(),cardDeck.pop()]

	Player1.play(firstHand)
	House.play(secondHand)

	Bet = int(input("Please enter your bet: "))

	Player1.betMoney(Bet)

	print(cardDeck)
	print(Player1,Player1.money)
	printHouse(House)

	if Player1.hasBlackjack():
		if House.hasBlackjack():
			Player1.draw()
		else:
			Player1.win(True)
	else:
		while(Player1.score < 21):
			action = input("Do you want another card? (y/n)?: ")
			if action == "y":
				Player1.hit(cardDeck.pop())
				print(Player1)
				printHouse(House)
			else:
				break
		while (House.score < 17):
			print(House)
			House.hit(cardDeck.pop())
		
		if Player1.score > 21:
			if House.score > 21:
				Player1.draw()
			else:
				Player1.win(False)
		
		elif Player1.score > House.score:
			Player1.win(True)

		elif Player1.score == House.score:
			Player1.draw()

		else:
			if House.score > 21:
				Player1.win(True)
			else:
				Player1.win(False)



	print(House)
	print(Player1.money)	

'''