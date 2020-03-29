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
		origCardList = []
		for c in self.finalCards:
			origCardList.append(c)
		cardList = []
		for v in origCardList:
			cardList.append(cardValues[v][0]+cardValues[v][1])
		print(cardList)
		return self.score

	def checkFlush():
	    tempDict = {'d':0,'h':0,'s':0,'c':0}
	    for k in self.finalCards:
	        for j in tempDict:
	            if cardValues[k][1] == j:
	                tempDict[j] += 1
	    #r = checkMatches()
	    for k in tempDict:
	        if tempDict[k] >= 5:
	            return k
	        else:
	            return False
	        

	def checkStrFlush(j):
	    #suite = j
	    suitedValues = []
	    tempSuitedValues = []
	    for k in self.finalCards:
	        if cardValues[k][1] == j:
	            suitedValues.append(cardValues[k][2])
	            tempSuitedValues.append(cardValues[k][2])
	    list.sort(suitedValues)
	    list.sort(tempSuitedValues)
	    if len(tempSuitedValues) >= 5:
	        if tempSuitedValues[-1] == 14: # checks is there is an Ace
	            tempSuitedValues.pop()
	            #print(tempSuitedValues)
	            checkList = [2,3,4,5]
	            isLowStr = 0
	            for k in checkList: # checks if the remaining four cards are 2,3,4,5
	                if k not in tempSuitedValues:
	                    #print("stop")
	                    break
	                else:
	                    isLowStr += 1
	            if isLowStr == 4:
	                #print("lowest straight flsh")
	                tempSuitedValues = checkList
	                tempSuitedValues.append(1) # adds Ace with the value of 1
	                list.sort(tempSuitedValues)
	                suitedValues = tempSuitedValues
	    oneCount = 0
	    oneInRow = 0
	    previousOne = 0
	    #print(suitedValues)
	    #print(np.diff(b))
	    for i in np.diff(suitedValues): # when sorting and running np.diff, the array will be [1,1,1,1] if there is a straight
	        if i == 1:
	            oneCount += 1
	            if previousOne == 1:
	                oneInRow += 1
	            previousOne = 1
	        else:
	            previousOne = 0
	    if oneInRow >= 3:
	        #print("this is a straight flsh")
	        if len(suitedValues) == 5:
	            pass
	        if len(suitedValues) == 6:
	            list.sort(suitedValues,reverse=True)
	            suitedValues.pop()
	        if len(suitedValues) == 7:
	            list.sort(suitedValues,reverse=True)
	            suitedValues.pop()
	            suitedValues.pop()
	        return suitedValues
	        #self.score += ###### need to set the straight flush level score here
	        
	        #print("there's a straight flush")
	    else:
	        return False

	def getValueList():
		origCardList = self.finalCards # self..
		cardList = []
		for v in origCardList:
			cardList.append(cardValues[v][0]+cardValues[v][1])
		#print(cardList)		
		valueList = []
		for a in cardList:
			if a.find('z') == 0:
				valueList.append(14)
				continue
			if a.find('y') == 0:
				valueList.append(13)
				continue
			if a.find('x') == 0:
				valueList.append(12)
				continue
			if a.find('w') == 0:
				valueList.append(11)
				continue
			valueList.append(cardValues[a][2])
		return valueList
		#print(valueList,"   value list")
	    
	def checkMatches():
	    b = getValueList()
	    list.sort(b)
	    zeroCount = 0
	    zeroInRow = 0
	    previousZero = 0
	    #print(np.diff(b))
	    for i in np.diff(b):
	        if i == 0:
	            zeroCount += 1
	            if previousZero == 1:
	                zeroInRow += 1
	            previousZero = 1
	        else:
	            previousZero = 0
	    if zeroCount == 3:
	        if zeroInRow == 2:
	            #print("four of a kind")
	            #self.score += ##### four fo a king score
	            return "FOAK" # four of a kind
	        if zeroInRow == 1:
	            #print("full house")
	            #self.score += ##### full house score
	            return "FH" # full house
	        if zeroInRow == 0:
	            if checkStr() == True:
	                #print("there's a straight")
	                return "STR" #straight
	            else:
	                #print("Two pair")
	                #self.score += ##### two pair score
	                return "TwoP" # two pair
	    if zeroCount == 2:
	        if zeroInRow == 1:
	            if checkStr() == True:
	                #print("there's a straight")
	                return "STR" #straight
	            else:
	                #print("Three of a kind")
	                #self.score += ##### three of a kind score
	                return "Three" # three of a kind
	        if zeroInRow == 0:
	            if checkStr() == True:
	                #print("there's a straight")
	                return "STR" #straight
	            else:
	                #print("Two pair")
	                #self.score += ##### two pair score
	                return "TwoP" # two pair
	    if zeroCount == 1:
	        if checkStr() == True:
	            #print("there's a straight")
	            return "STR" #straight
	        else:
	            #print("One pair")
	            #self.score += ##### One pair score
	            return "OneP" # One pair
	    if zeroCount == 0:
	        if checkStr() == True:
	            #print("there's a straight")
	            return "STR" #straight
	        else:
	            #print("High Card")
	            #self.score += ##### high card score
	            return "High" # high
	    #print(zeroCount," zerocount ",zeroInRow," inrow ")

	def checkStr():
	    values = []
	    tempValues = []
	    for i in getValueList():
	        values.append(i)
	        tempValues.append(i)
	    list.sort(values)
	    list.sort(tempValues)
	    if tempValues[-1] == 14: # checks is there is an Ace
	        tempValues.pop()
	        #print(tempValues)
	        checkList = [2,3,4,5]
	        isLowStr = 0
	        for k in checkList: # checks if the remaining four cards are 2,3,4,5
	            if k not in tempValues:
	                #print("stop")
	                break
	            else:
	                isLowStr += 1
	                #continue
	                #time.sleep(3)
	        if isLowStr == 4:
	            #print("lowest straight")
	            tempValues = checkList
	            tempValues.append(1) # adds Ace with the value of 1
	            list.sort(tempValues)
	            values = tempValues
	    #print(np.diff(values))
	    #print(values)
	    oneCount = 0
	    oneInRow = 0
	    previousOne = 0
	    #print(np.diff(b))
	    for i in np.diff(values): # when sorting and running np.diff, the array will be [1,1,1,1] if there is a straight
	        if i == 1:
	            oneCount += 1
	            if previousOne == 1:
	                oneInRow += 1
	            previousOne = 1
	        else:
	            previousOne = 0
	    if oneInRow >= 3:
	        #print("this is a straight")
	        if len(values) == 5:
	            pass
	        if len(values) == 6:
	            list.sort(values,reverse=True)
	            values.pop()
	        if len(values) == 7:
	            list.sort(values,reverse=True)
	            values.pop()
	            values.pop()
	        return True
	        #self.score += ###### need to set the straight level score here
	        
	        #print("there's a straight ")
	    else:
	        return False



		
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
			os.system("cls")
			if len(communityCards) == 6:
				tempComcards = []
				for c in communityCards:
					tempComcards.append(c)
				tempComcards.pop()
				print("\n\n\n\nCOMMUNITY CARDS\n=========================\n",tempComcards,"\n=========================\n")
			else:
				print("\n\n\n\nCOMMUNITY CARDS\n=========================\n",communityCards,"\n=========================\n")
			print("Call is on ",r.name,"\n")
			print("PLAYERS CARDS\n=========================\n",r.hand,"\n=========================\n")
			if r.bet == highestBet:
				try:
					playerFinalChoice = int(input(r.name," choose an option.\n[1] Check\n[2] Raise\n[3] Fold\n\n"))
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
				print(r.name," do you want to call for ",highestBet - r.bet,", raise or fold?\n\nChoose and option.\n")
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
		os.system("cls")
		print("\n\nDEALING THE RIVER\n\n")
		time.sleep(2)
		os.system("cls")
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
		os.system("cls")
		print("\n\nDEALING THE TURN\n\n")
		time.sleep(2)
		os.system("cls")
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
		os.system("cls")
		print("\n\nDEALING THE FLOP\n\n")
		time.sleep(2)
		os.system("cls")
		highestBet, PlayerID, haveFolded, totCount = checkBets()
		totCount = 0
		while totCount < len(activePlayers):
			betRound(highestBet,PlayerID)
			highestBet, PlayerID, haveFolded, totCount = checkBets()
			#print("highest bet = ",highestBet,"......... player ID = ", PlayerID, ".............have folded = ", haveFolded, "\n........total count = ", totCount,".......active players = ", len(activePlayers))
		updateBalances()
		checkWin(haveFolded)
		cardDeck.pop() # burn card before turn
		communityCards.append(cardDeck.pop()) # deal turn card
		time.sleep(1)
		# betRound()
		# continue
	if len(communityCards) < 3:
		os.system("cls")
		print("\n\nDEALING PLAYERS CARDS\n\n")
		time.sleep(2)
		os.system("cls")
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
							#print(d.hand,d.name,"       ",d.bet," = BET       ",d.money," = BALANCE        ",d.score," = score")
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
