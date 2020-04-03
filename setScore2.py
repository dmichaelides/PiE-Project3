

import numpy as np
import collections,numpy
import time


#finalCards = ['3d', '8d', '5d', '2d', '4d', 'Ad', '9d'] # straight flush
#finalCards = ['3d', '3c', '3s', '3h', '4d', 'Kc', 'Ah'] # four kind
#finalCards = ['3d', '3c', '3s', '8c', '4d', 'Ac', 'Ah'] # full house
#finalCards = ['3d', '3c', 'As', '8c', '4d', 'Ac', 'Ah'] # full house
#finalCards = ['3d', '3c', '3s', '8c', '4d', 'Kc', 'Ah'] # three kind
#finalCards = ['2d', '3c', '3s', '3h', '4d', 'Kc', 'Ah'] # three kind
#finalCards = ['3d', '3c', '8s', '8c', '4d', '4c', 'Ah'] # two pair x3
#finalCards = ['3d', '3c', '8s', '8c', '4d', 'Kc', 'Ah'] # two pair
#finalCards = ['3d', '3c', '2s', '8c', '4d', 'Kc', 'Ah'] # one pair
#finalCards = ['3d', '2c', '5s', '8c', '4d', 'Kc', '6h'] # straight
#finalCards = ['7d', '2c', '5s', '8c', '4d', 'Kc', '6h'] # midd straight
#finalCards = ['3d', '2c', '5s', '8c', '4d', 'Kc', '9h'] # high card
finalCards = ['3h', '6h', '7h', '8h', '4h', 'Kd', 'Ah'] # flush
#finalCards = ['3d', '2c', '9s', '5c', '4d', 'Kc', 'Ah'] # low straight
#finalCards = ['Ad', 'Ac', '7s', '7c', '3d', 'Kc', '2h'] # two pair
cardValues = {'2h': ('2', 'h', 2), '3h': ('3', 'h', 3), '4h': ('4', 'h', 4), '5h': ('5', 'h', 5), '6h': ('6', 'h', 6), '7h': ('7', 'h', 7), '8h': ('8', 'h', 8), '9h': ('9', 'h', 9), '10h': ('10', 'h', 10), 'Jh': ('w', 'h', 11), 'Qh': ('x', 'h', 12), 'Kh': ('y', 'h', 13), 'Ah': ('z', 'h', 14), '2d': ('2', 'd', 2), '3d': ('3', 'd', 3), '4d': ('4', 'd', 4), '5d': ('5', 'd', 5), '6d': ('6', 'd', 6), '7d': ('7', 'd', 7), '8d': ('8', 'd', 8), '9d': ('9', 'd', 9), '10d': ('10', 'd', 10), 'Jd': ('w', 'd', 11), 'Qd': ('x', 'd', 12), 'Kd': ('y', 'd', 13), 'Ad': ('z', 'd', 14), '2s': ('2', 's', 2), '3s': ('3', 's', 3), '4s': ('4', 's', 4), '5s': ('5', 's', 5), '6s': ('6', 's', 6), '7s': ('7', 's', 7), '8s': ('8', 's', 8), '9s': ('9', 's', 9), '10s': ('10', 's', 10), 'Js': ('w', 's', 11), 'Qs': ('x', 's', 12), 'Ks': ('y', 's', 13), 'As': ('z', 's', 14), '2c': ('2', 'c', 2), '3c': ('3', 'c', 3), '4c': ('4', 'c', 4), '5c': ('5', 'c', 5), '6c': ('6', 'c', 6), '7c': ('7', 'c', 7), '8c': ('8', 'c', 8), '9c': ('9', 'c', 9), '10c': ('10', 'c', 10), 'Jc': ('w', 'c', 11), 'Qc': ('x', 'c', 12), 'Kc': ('y', 'c', 13), 'Ac': ('z', 'c', 14)}



def setScore():
	# finalCards
	addScore = 0
	# pokerHand = ""
	origCardList = []
	for c in finalCards:
		origCardList.append(c)
	cardList = []
	Rank = ""
	fValues = [0]
	for v in origCardList:
		cardList.append(cardValues[v][0]+cardValues[v][1])
	if checkMatches()[1] == "High":
		Rank = "High Card"
		fValues = checkMatches()[0]
	if checkMatches()[1] == "OneP":
		Rank = "One Pair"
		fValues = checkMatches()[0]
	if checkMatches()[1] == "TwoP":
		Rank = "Two pairs"
		fValues = checkMatches()[0]
	if checkMatches()[1] == "Three":
		Rank = "Three of a Kind"
		fValues = checkMatches()[0]
	if checkMatches()[1] == "STR":
		Rank = "Straight"
		fValues = checkMatches()[0]
	if checkFlush() != False:
		Rank = "Flush"
		suitedValues = []
		tempfValues = []
		s = checkFlush()
		for v in origCardList:
			if cardValues[v][1] == s:
				suitedValues.append(cardValues[v][2])
		suitedValues.sort(reverse=True)
		for i in range(5):
			tempfValues.append(suitedValues[i])
		fValues = tempfValues
	if checkMatches()[1] == "FH":
		Rank = "Full house"
		fValues = checkMatches()[0]
	if checkMatches()[1] == "FOAK":
		Rank = "Four of a Kind"
		fValues = checkMatches()[0]
	if checkStrFlush(checkFlush()) != False:
		Rank = "staightFlush"
		fValues = checkStrFlush(checkFlush())
	addScore = np.sum(fValues)
	try:
		if Rank == "High Card":
			#s = np.sum(fValues)
			#score += np.sum(fValues)
			addScore += 0
		if Rank == "One Pair":
			#s = np.sum(fValues)
			#score += np.sum(fValues)
			addScore += 1000
		if Rank == "Two pairs":
			#s = np.sum(fValues)
			#score += np.sum(fValues)
			addScore += 2000
		if Rank == "Three of a Kind":
			#s = np.sum(fValues)
			#score += np.sum(fValues)
			addScore += 3000
		if Rank == "Straight":
			#s = np.sum(fValues)
			#score += np.sum(fValues)
			addScore += 4000
		if Rank == "Flush":
			#s = np.sum(fValues)
			#score += np.sum(fValues)
			addScore += 5000
		if Rank == "Full house":
			#s = np.sum(fValues)
			#score += np.sum(fValues)
			addScore += 6000
		if Rank == "Four of a Kind":
			#s = np.sum(fValues)
			#score += np.sum(fValues)
			addScore += 7000
		if Rank == "staightFlush":
			#s = np.sum(fValues)
			#score += np.sum(fValues)
			addScore += 8000
	except TypeError:
		pass
	print(" has a ", Rank," with total score of ", addScore)
	print(fValues," these are the final values")
	time.sleep(3)
	return addScore

def checkFlush():
    tempDict = {'d':0,'h':0,'s':0,'c':0}
    flushKey = "x"
    for k in finalCards:
    	print(tempDict)
    	for j in tempDict:
    		if cardValues[k][1] == j:
    			tempDict[j] += 1
    #r = checkMatches()
    print(tempDict)
    for k in tempDict:
    	if tempDict[k] >= 5:
    		flushKey = k
    if flushKey != "x":
    	return flushKey	
    else:
    	return False
        

def checkStrFlush(j):
    #suite = j
    suitedValues = []
    tempSuitedValues = []
    for k in finalCards:
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
                if 6 in tempSuitedValues:
                	suitedValues = [2,3,4,5,6]
                else:
                	suitedValues = [1,2,3,4,5]
    oneCount = 0
    oneInRow = 0
    previousOne = 0
    #print(suitedValues)
    #print(np.diff(b))
    peakStraight = 0
    valuesIndex = 0
    for i in np.diff(suitedValues): # when sorting and running np.diff, the array will be [1,1,1,1] if there is a straight
    	valuesIndex += 1
    	if i == 1:
    		oneCount += 1
    		if previousOne == 1:
    			oneInRow += 1
    			if oneInRow >= 3:
    				peakStraight = suitedValues[valuesIndex]
    		previousOne = 1
    	else:
    		previousOne = 0
    if oneInRow >= 3:
    	#print("this is a straight")
    	newValues = []
    	for n in range(5):
    		newValues.append(peakStraight)
    		peakStraight -= 1
    	suitedValues = newValues
    	return suitedValues
        #score += ###### need to set the straight flush level score here
        #print("there's a straight flush")
    else:
        return False

def getValueList():
	origCardList = finalCards # .
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
    valueListIndex = 0
    FOAK = []
    FH = []
    Three = []
    TwoP = []
    OneP = []
    #print(np.diff(b))
    for i in np.diff(b):
        valueListIndex += 1
        if i == 0:
            zeroCount += 1
            TwoP.append(b[valueListIndex])
            OneP.append(b[valueListIndex])
            if previousZero == 1:
                Three.append(b[valueListIndex])
                zeroInRow += 1
                if zeroCount == 3:
                	FH.append(b[valueListIndex])
                	if zeroInRow == 2:
                		FOAK.append(b[valueListIndex])
            previousZero = 1
        else:
            previousZero = 0
    if zeroCount == 3:
        if zeroInRow == 2:
            print(FOAK,"four of a kind")
            fNum = FOAK[0] # this is the four of a kind value
            rVal = [] # compose list of remaing values to eliminate smallest
            values = []
            for n in b:
                if n != fNum:
                    rVal.append(n)
            rVal.sort(reverse=True)
            rVal.pop()
            rVal.pop()
            for v in range(4):
                values.append(fNum)
            for f in rVal:
                values.append(f)
            print(values,"four of a kind")
            #score += ##### four fo a king score
            return values,"FOAK" # four of a kind
        if zeroInRow == 1:
            print(FH,"full house")
            a = FH[3]
            b = FH[0]
            values = []
            if collections.Counter(FH)[a] == 3:
                FH.append(b)
            if collections.Counter(FH)[b] == 3:
                FH.append(a)
            print(FH,"full full house")
            #score += ##### full house score
            return FH,"FH" # full house
        if zeroInRow == 0:
            if checkStr() != False:
            	values = checkStr()
            	print("there's a straight")
            	return values,"STR" #straight
            else:
                print(TwoP,"two pair")
                fList = TwoP
                fList.sort(reverse=True)
                if len(fList) == 3:
                    fList.pop()
                rVal = []
                values = []
                for n in b:
                    if n not in fList:
                        rVal.append(n)
                rVal.sort(reverse=True)
                rVal.pop()
                rVal.pop()
                for v in range(2):
                    values.append(fList[0])
                    values.append(fList[1])
                for f in rVal:
                    values.append(f)
                print(values)
                #score += ##### two pair score
                return values,"TwoP" # two pair
    if zeroCount == 2:
        if zeroInRow == 1:
            if checkStr() != False:
            	values = checkStr()
            	print("there's a straight")
            	return values,"STR" #straight
            else:
                print(Three,"three of a kind")
                fNum = Three[0] # this is the four of a kind value
                rVal = [] # compose list of remaing values to eliminate smallest
                values = []
                for n in b:
                	if n != fNum:
                		rVal.append(n)
                rVal.sort(reverse=True)
                rVal.pop()
                rVal.pop()
                for v in range(3):
                	values.append(fNum)
                for f in rVal:
                	values.append(f)
                print(values,"three of a kind")
                #score += ##### three of a kind score
                return values,"Three" # three of a kind
        if zeroInRow == 0:
            if checkStr() != False:
            	values = checkStr()
            	print("there's a straight")
            	return values,"STR" #straight
            else:
                print(TwoP,"two pair")
                fList = TwoP
                fList.sort(reverse=True)
                if len(fList) == 3:
                    fList.pop()
                rVal = []
                values = []
                for n in b:
                    if n not in fList:
                        rVal.append(n)
                rVal.sort(reverse=True)
                rVal.pop()
                rVal.pop()
                for v in range(2):
                    values.append(fList[0])
                    values.append(fList[1])
                for f in rVal:
                    values.append(f)
                print(values)
                #score += ##### two pair score
                return values,"TwoP" # two pair
    if zeroCount == 1:
        if checkStr() != False:
        	values = checkStr()
        	print("there's a straight")
        	return values,"STR" #straight
        else:
            fNum = OneP[0] # this is the one pair of a kind value
            rVal = [] # compose list of remaing values to eliminate smallest
            values = []
            for n in b:
                if n != fNum:
                    rVal.append(n)
            rVal.sort(reverse=True)
            rVal.pop()
            rVal.pop()
            for v in range(2):
                values.append(fNum)
            for f in rVal:
                values.append(f)
            print(values,"one pair")
            return values,"OneP" # one pair
    if zeroCount == 0:
        if checkStr() != False:
        	values = checkStr()
        	print("there's a straight")
        	return values,"STR" #straight
        else:
            print("high card")
            values = b
            values.sort(reverse=True)
            values.pop()
            values.pop()
            #score += ##### high card score
            return values,"High" # high
    #print(zeroCount," zerocount ",zeroInRow," inrow ")

def checkStr():
	try:
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
				if 6 in tempValues:
					values = [2,3,4,5,6]
				else:
					values = [1,2,3,4,5]
		#print(np.diff(values))
		#print(values)
		oneCount = 0
		oneInRow = 0
		previousOne = 0
		peakStraight = 0
		valuesIndex = 0
		#print(np.diff(b))
		for i in np.diff(values): # when sorting and running np.diff, the array will be [1,1,1,1] if there is a straight
			valuesIndex += 1
			if i == 1:
				oneCount += 1
				if previousOne == 1:
					oneInRow += 1
					if oneInRow >= 3:
						peakStraight = values[valuesIndex]
				previousOne = 1
			else:
				previousOne = 0
		if oneInRow >= 3:
			#print("this is a straight")
			newValues = []
			for n in range(5):
				newValues.append(peakStraight)
				peakStraight -= 1
			values = newValues
			return True
			#score += ###### need to set the straight level score here
			#print("there's a straight ")
		else:
			return False		
	except IndexError:
		pass



setScore()