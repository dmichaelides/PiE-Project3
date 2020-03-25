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
import numpy as np


cardValues = {} # a dictionary showing each card as Key and a Tuple as value.  Tuple entities are (Card, Suit, Value).  Example: 2 of hearts is "2h":(2,'h',2)
Players = () # needs to be a tuple to keep the order of players consistent.
Pot = 0
communityCards = []
smallBlind = 10
bigBlind = 20
# dealer = 0


# create deck

def creatDeck():

	Deck = []

	faceValues = ["J","Q","K","A"]
	cardSuit = ["h","d","s","c"] # 4 suits.  h = heart, d = diamond, s = spade, c = clover


	for suit in cardSuit:
		for card in range(2,11):
			Deck.append(str(card)+(suit))
			cardValues[str(card)+(suit)] = (str(card),suit,int(card))
		for card in faceValues:
			Deck.append(card+suit)
			if card == "J":
				cardValues[card+suit] = ("w",suit,11)
			if card == "Q":
				cardValues[card+suit] = ("x",suit,12)
			if card == "K":
				cardValues[card+suit] = ("y",suit,13)
			if card == "A":
				cardValues[card+suit] = ("z",suit,14)
									
	shuffle(Deck)
	return Deck

cardDeck = creatDeck()
print(cardValues)

# print(cardDeck,"\n\n")
# print(cardValues)

class Player:
	"""docstring for Player"""
	def __init__(self, name, hand = [], finalCards = [], money=1000, isDealer=0):
		self.name = name
		self.money = money
		self.hand = hand
		self.isDealer = isDealer
		self.finalCards = finalCards
		self.score = self.setScore()
		self.pokerHand = ""
		self.folded = 0
		self.bet = 0
	 	
	def __str__(self): #print (player)
		currentHand = ""
		for card in self.hand:
			currentHand += str(card) + " "
		# print(currentHand)		
		finalStatus = currentHand + "score: "# + str(self.score)
		# finalStatus = self.name

		return finalStatus


	# def setGrade(self,cardList):
	# 	self.cardList = cardList
	# 	newCardList = []
	# 	for v in cardList:
	# 		newCardList.append(cardValues[v][0]+cardValues[v][1])
		# list.sort(newCardList)
	# 	valueList = []
	# 	suitList = []
	# 	valueSuitList = []
	# 	for a in newCardList:
	# 		if a.find('z') == 0:
	# 			valueList.append(14)
	# 			if a.find('h') == 1:
	# 				suitList.append('h')
	# 			if a.find('d') == 1:
	# 				suitList.append('d')
	# 			if a.find('s') == 1:
	# 				suitList.append('s')
	# 			if a.find('c') == 1:
	# 				suitList.append('c')
	# 			continue
	# 		if a.find('y') == 0:
	# 			valueList.append(13)
	# 			if a.find('h') == 1:
	# 				suitList.append('h')
	# 			if a.find('d') == 1:
	# 				suitList.append('d')
	# 			if a.find('s') == 1:
	# 				suitList.append('s')
	# 			if a.find('c') == 1:
	# 				suitList.append('c')
	# 			continue
	# 		if a.find('x') == 0:
	# 			valueList.append(12)
	# 			if a.find('h') == 1:
	# 				suitList.append('h')
	# 			if a.find('d') == 1:
	# 				suitList.append('d')
	# 			if a.find('s') == 1:
	# 				suitList.append('s')
	# 			if a.find('c') == 1:
	# 				suitList.append('c')
	# 			continue
	# 		if a.find('w') == 0:
	# 			valueList.append(11)
	# 			if a.find('h') == 1:
	# 				suitList.append('h')
	# 			if a.find('d') == 1:
	# 				suitList.append('d')
	# 			if a.find('s') == 1:
	# 				suitList.append('s')
	# 			if a.find('c') == 1:
	# 				suitList.append('c')
	# 			continue
	# 		valueList.append(cardValues[a][2])
	# 		suitList.append(cardValues[a][1])
	# 	for v in suitList:
	# 		if v == 'd':
	# 			valueSuitList.append(1)
	# 		if v == 's':
	# 			valueSuitList.append(2)
	# 		if v == 'c':
	# 			valueSuitList.append(3)
	# 		if v == 'h':
	# 			valueSuitList.append(4)
	# 	gradeScore = 0
	# 	pokerHand = ""
	# 	handArray = np.diff(valueList)
	# 	suitArray = np.diff(valueSuitList)
	# 	print(handArray," hand array")
	# 	print(suitArray," suit array")
        
	# 	return gradeScore,pokerHand

	def colFinalCards(self):
		self.finalCards = [] 
		for card in communityCards:
			self.finalCards.append(card)
		for card in self.hand:
			self.finalCards.append(card)


	def setScore(self):
		# self.finalCards
		self.score = 0
		# self.pokerHand = ""
		origCardList = self.finalCards
		cardList = []
		for v in origCardList:
			cardList.append(cardValues[v][0]+cardValues[v][1])
		# print(cardList)		
		valueList = []
		suitList = []
		valueSuitList = []
		valueTupleList = []
		suitStrFlsh = []
		for a in cardList:
			if a.find('z') == 0:
				valueList.append(14)
				if a.find('h') == 1:
					suitList.append('h')
				if a.find('d') == 1:
					suitList.append('d')
				if a.find('s') == 1:
					suitList.append('s')
				if a.find('c') == 1:
					suitList.append('c')
				continue
			if a.find('y') == 0:
				valueList.append(13)
				if a.find('h') == 1:
					suitList.append('h')
				if a.find('d') == 1:
					suitList.append('d')
				if a.find('s') == 1:
					suitList.append('s')
				if a.find('c') == 1:
					suitList.append('c')
				continue
			if a.find('x') == 0:
				valueList.append(12)
				if a.find('h') == 1:
					suitList.append('h')
				if a.find('d') == 1:
					suitList.append('d')
				if a.find('s') == 1:
					suitList.append('s')
				if a.find('c') == 1:
					suitList.append('c')
				continue
			if a.find('w') == 0:
				valueList.append(11)
				if a.find('h') == 1:
					suitList.append('h')
				if a.find('d') == 1:
					suitList.append('d')
				if a.find('s') == 1:
					suitList.append('s')
				if a.find('c') == 1:
					suitList.append('c')
				continue
			valueList.append(cardValues[a][2])
			suitList.append(cardValues[a][1])
		for v in suitList:
			if v == 'd':
				valueSuitList.append(1)
			if v == 's':
				valueSuitList.append(2)
			if v == 'c':
				valueSuitList.append(3)
			if v == 'h':
				valueSuitList.append(4)
		try:
			for s in range(7):
				valueTupleList.append((valueList[s],valueSuitList[s]))
		except IndexError:
			pass
		list.sort(valueTupleList)
		#print(valueTupleList)
		for s in valueTupleList:
			suitStrFlsh.append(s[1])
		list.sort(valueList)
		list.sort(valueSuitList)
		print(valueList,"   value list")
		print(valueSuitList,"    value suitList")
		print(suitStrFlsh,"    suitStrFlsh")
		# gradeScore = 0
		# self.pokerHand = ""
		handArray = np.diff(valueList)
		suitArray = np.diff(valueSuitList)
		strFlshArray = np.diff(suitStrFlsh)
		print(handArray,"  ==== hand array")
		print(strFlshArray," ==== str Flush Array")
		print(suitArray,"  ==== suit array")
		# define how the array looks when there is a straight, flush. straight flush, pairs, trips or full house.
		# Poker hands starting from highest
		# royal flush, straight flush, four of a kind, full house, flush, straight, three of a kind, 2 pairs, 1 pair, high card
		# royal flush hand array [# # 1 1 1 1] strFlshArray [# # 0 0 0 0] .. and sum of the numbers in straight == 60
		# straight flush hand array [# # 1 1 1 1] strFlshArray [# # 0 0 0 0] or any 4 in a row hand == [# 1 1 1 1 #] and strFlshArray ==[# 0 0 0 0 #].. sum numbers in straight < 60
		# four of a kind === [2,2,2,2,4,5]  hand array [0 0 0 0 # #] ... or any 4 zeros in a row example = [# 0 0 0 0 #]
		# full house === [2,2,2,5,5,6,14] [0 0 3 0 1 8]
		# self.score += gradeScore
		return self.score


		
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

def circle_iter(items, start=1): # defines where the loop should start from active players in a round
	l = len(items)
	for i in items:
		yield items[str(start)]
		start += 1
		if start == l+1: start = 1

def updateBalances():
	global Pot
	for b in activePlayers:
		Pot += activePlayers[b].bet
		activePlayers[b].bet = 0

def checkWin(haveFolded = 0):
	global Pot
	highestScore = 0
	foldedCount = haveFolded 
	for s in activePlayers:
		if activePlayers[s].score > highestScore:
			highestScore = activePlayers[s].score
	if len(activePlayers)-1 == foldedCount:
		# resetRound()
		for w in activePlayers:
			# print(activePlayers[w].isDealer," is dealer in checkwin........................................")
			if activePlayers[w].folded == 0: 
				# we need to check the score
				# if there is a tie, we need to split pot
				activePlayers[w].money += Pot
				print(activePlayers[w].name," wins ",Pot)
				Pot = 0
		resetRound()
	if len(communityCards) == 6:
		for w in activePlayers:
			if activePlayers[w].folded == 1:
				continue
			if activePlayers[w].score > highestScore - 1000:
				print("....need to finish score code here .... ") # all players who qualify here split pot. 
		resetRound()

def resetRound():
	global communityCards,cardDeck
	communityCards = []
	cardDeck = creatDeck()
	dealer = -1
	for p in activePlayers:
		if activePlayers[p].isDealer == 1:
			dealer = p
	tempCount = 0
	for b in circle_iter(activePlayers,int(dealer)):
		b.folded = 0
		if tempCount == 0:
			b.isDealer = 0
		if tempCount == 1:
			b.isDealer = 1
		tempCount += 1
		if b.money < smallBlind:
			b.folded = 1

def checkBets():
	highestBet = 0
	PlayerID = -1
	haveFolded = 0
	betMatch = 0
	totCount = 0
	for s in activePlayers:
		# print(s)
		if activePlayers[s].bet >= highestBet:
			highestBet = activePlayers[s].bet
			PlayerID = int(s)
		if activePlayers[s].isDealer == 1:
			tempPlayerID = int(s)
		if activePlayers[s].folded == 1:
			haveFolded += 1
	for s in activePlayers:
		if activePlayers[s].bet == highestBet and activePlayers[s].folded == 0:
			betMatch += 1
			# betMatch +=1
	if highestBet == 0:
		tempCount = 0
		for i in circle_iter(activePlayers,int(tempPlayerID)):
			if tempCount == 0:
				PlayerID = int(list(activePlayers.keys())[list(activePlayers.values()).index(i)])
			tempCount += 1
	if highestBet > 0: # improvement needed here, code needs to be able to stop on the person who made the raise during the betRound function. 
		tempCount = 0
		for k in circle_iter(activePlayers,int(PlayerID)):
			if tempCount == 1:
				PlayerID = int(list(activePlayers.keys())[list(activePlayers.values()).index(k)])
			tempCount += 1
	totCount = haveFolded + betMatch
	return highestBet, PlayerID, haveFolded, totCount

def betRound(highestBet=0, PlayerID=-1):
	highestBet = highestBet
	PlayerID = PlayerID
	for r in circle_iter(activePlayers,PlayerID):
		if r.folded == 0:
		# print(r.name," do you want to check or raise")
			print("\n\n",r.name," The current bet is ", highestBet,"\n\n")
			if r.bet == highestBet:
				try:
					playerFinalChoice = int(input("Choose an option.\n[1] Check\n[2] Raise\n[3] Fold\n\n"))
					if 1 > playerFinalChoice or playerFinalChoice > 3:
						raise ValueError
				except Exception:
					print("Choice should be a number: '1', '2' or '3'.\n\n")
					playerFinalChoice = int(input("Choose an option.\n[1] Check\n[2] Raise\n[3] Fold\n\n"))
				if playerFinalChoice == 1:
					print("1 final choice")
				if playerFinalChoice == 2:
					playerRaise = int(input("How much do you want to raise?\n\n"))
					if playerRaise < highestBet*1.5:
						print("Amount must be at least ",highestBet*1.5,"\n\n")
						playerRaise = int(input("How much do you want to raise?\n\n"))
					newBet = playerRaise - r.bet
					r.betMoney(newBet)
					highestBet = playerRaise
					print("2 final choice")
				if playerFinalChoice == 3:
					r.folded = 1
					print("3 final choice")
				time.sleep(1)
			if r.bet < highestBet:
				print("Do you want to call for ",highestBet - r.bet,", raise or fold?\n\nChoose and option.\n")
				try:
					playerFinalChoice = int(input("[1] Call\n[2] Raise\n[3] Fold\n\n"))
					if 1 > playerFinalChoice or playerFinalChoice > 3:
						raise ValueError
				except Exception:
					print("Choice should be a number: '1', '2' or '3'.\n\n")
					playerFinalChoice = int(input("[1] Call\n[2] Raise\n[3] Fold\n\n"))
				if playerFinalChoice == 1:
					newBet = highestBet - r.bet
					r.betMoney(newBet)			
					print("1 final choice")
				if playerFinalChoice == 2:
					playerRaise = int(input("How much do you want to raise?\n\n"))
					if playerRaise < highestBet*1.5:
						print("Amount must be at least ",highestBet*1.5,"\n\n")
						playerRaise = int(input("How much do you want to raise?\n\n"))
					newBet = playerRaise - r.bet
					r.betMoney(newBet)
					highestBet = playerRaise
					print("2 final choice")
				if playerFinalChoice == 3:
					r.folded = 1
					print("3 final choice")
				time.sleep(1)

Players = ("Jon","David","Simon", "George")

print(Players)

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

activePlayers["1"].isDealer = 1

while(True):
	if len(communityCards) == 5:
		print(communityCards)
		print("========= in the river=============")
		for d in activePlayers:
			activePlayers[d].colFinalCards()
			activePlayers[d].setScore()
		for d in activePlayers:
			print(activePlayers[d].finalCards)
		communityCards.append(cardDeck.pop()) # deal extra card to trigger round reset in the checkWin funtion
		highestBet, PlayerID, haveFolded, totCount = checkBets()
		totCount = 0
		while totCount < len(activePlayers):
			betRound(highestBet,PlayerID)
			highestBet, PlayerID, haveFolded, totCount = checkBets()
		updateBalances()
		checkWin(haveFolded)
		time.sleep(1)
	if len(communityCards) == 4:
		print("========= in the turn=============")
		print(communityCards)
		highestBet, PlayerID, haveFolded, totCount = checkBets()
		totCount = 0
		while totCount < len(activePlayers):
			betRound(highestBet,PlayerID)
			highestBet, PlayerID, haveFolded, totCount = checkBets()
		updateBalances()
		checkWin(haveFolded)
		cardDeck.pop() # brun card before river
		communityCards.append(cardDeck.pop()) # deal river card
		print("this is the length of the community cars",len(communityCards))
		time.sleep(1)
		# betRound()
		# continue
	if len(communityCards) == 3:
		# 	break
		print("========= in the flop=============")
		print(communityCards)
		highestBet, PlayerID, haveFolded, totCount = checkBets()
		totCount = 0
		while totCount < len(activePlayers):
			betRound(highestBet,PlayerID)
			highestBet, PlayerID, haveFolded, totCount = checkBets()
			print("highest bet = ",highestBet,"......... player ID = ", PlayerID, ".............have folded = ", haveFolded, "\n........total count = ", totCount,".......active players = ", len(activePlayers))
		updateBalances()
		checkWin(haveFolded)
		cardDeck.pop() # burn card before turn
		communityCards.append(cardDeck.pop()) # deal turn card
		time.sleep(1)
		# betRound()
		# continue
	if len(communityCards) < 3:
		print("============this is preflop===============")
		time.sleep(1)
		for p in activePlayers:
			if activePlayers[p].isDealer == 1:
				tempCount = 0
				for blinds in circle_iter(activePlayers,int(p)):
					if tempCount == 0:
						blinds.betMoney(smallBlind)
					if tempCount == 1:
						blinds.betMoney(bigBlind)
					tempCount += 1 
				for dealCards in range(2): #deal two card to each player
					for d in circle_iter(activePlayers,int(p)):
						if dealCards == 0:
							d.hand = [cardDeck.pop()]
						else:
							d.dealCard(cardDeck.pop())
							# d.setScore()
							print(d.hand,d.name,"       ",d.bet," = BET       ",d.money," = BALANCE        ",d.score," = score")
							# time.sleep(1)
				break
		# print(communityCards)
		# print(cardValues)
		# time.sleep(1)
		# betRound()
		highestBet, PlayerID, haveFolded, totCount = checkBets()
		while totCount < len(activePlayers):
			betRound(highestBet,PlayerID)
			# print("===================AFTER ROUND BEFORE SECOND CHECK==========================")
			# print(highestBet," is highestBet") 
			# print(PlayerID," is playersid")
			# print(haveFolded," haveFolded")
			# print(totCount," is totCount")
			# print(len(activePlayers)," is len of activePlayers")
			# for d in circle_iter(activePlayers,int(p)):
			# 	print(d.hand,d.name,d.bet," = BET......",d.money," = BALANCE......",d.score," = score")
			highestBet, PlayerID, haveFolded, totCount = checkBets()
			# print(highestBet," is highestBet") 
			# print(PlayerID," is playersid")
			# print(haveFolded," haveFolded")
			# print(totCount," is totCount")
			# print(len(activePlayers)," is len of activePlayers")
			# for d in circle_iter(activePlayers,int(p)):
			# 	print(d.hand,d.name,d.bet," = BET......",d.money," = BALANCE......",d.score," = score")
		updateBalances()
		checkWin(haveFolded)
		cardDeck.pop() # burn one card before the flop
		for i in range(3): # deal the flop
			communityCards.append(cardDeck.pop())


########## need to fix .. kept two players in the game, checking all the way and the round was not reset.  The community cards added up to more that 5.
####### need to fix ... when folding everyone off, the last person remaining does not get paid the pot - but a new round does begin.
