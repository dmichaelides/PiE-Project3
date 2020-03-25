# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 11:29:18 2020

@author: User
"""

import numpy as np
#finalCards = ['Kd', '6h', 'Jd', 'Ad', 'Qd', '2c', '10d'] # royal flush
#finalCards = ['3d', '8d', '5d', '2d', '4d', 'Ad', '9d'] # straight flush
#finalCards = ['3d', '3c', '3s', '3h', '4d', 'Kc', 'Ah'] # four kind
#finalCards = ['Ah', '3c', '3s', '3h', '4d', '2c', '3d'] # four kind
#finalCards = ['3d', '3c', '3s', '8c', '4d', 'Ac', 'Ah'] # full house
#finalCards = ['3d', '3c', '3s', '8c', '4d', 'Kc', 'Ah'] # three kind
#finalCards = ['2d', '3c', '3s', '3h', '4d', 'Kc', 'Ah'] # three kind
#finalCards = ['3d', '3c', '8s', '8c', '4d', '4c', 'Ah'] # two pair x3
#finalCards = ['3d', '3c', '8s', '8c', '4d', 'Kc', 'Ah'] # two pair
#finalCards = ['3d', '3c', '2s', '8c', '4d', 'Kc', 'Ah'] # one pair
finalCards = ['3d', '2c', '5s', '8c', '4d', 'Kc', '6h'] # straight
#finalCards = ['3d', '3c', '3s', '8c', '4d', 'Kc', 'Ah']
#finalCards = ['3d', '3c', '3s', '8c', '4d', 'Kc', 'Ah']
#finalCards = ['3d', '3c', '3s', '8c', '4d', 'Kc', 'Ah']
#finalCards = ['3d', '3c', '3s', '8c', '4d', 'Kc', 'Ah']
cardValues = {'2h': ('2', 'h', 2), '3h': ('3', 'h', 3), '4h': ('4', 'h', 4), '5h': ('5', 'h', 5), '6h': ('6', 'h', 6), '7h': ('7', 'h', 7), '8h': ('8', 'h', 8), '9h': ('9', 'h', 9), '10h': ('10', 'h', 10), 'Jh': ('w', 'h', 11), 'Qh': ('x', 'h', 12), 'Kh': ('y', 'h', 13), 'Ah': ('z', 'h', 14), '2d': ('2', 'd', 2), '3d': ('3', 'd', 3), '4d': ('4', 'd', 4), '5d': ('5', 'd', 5), '6d': ('6', 'd', 6), '7d': ('7', 'd', 7), '8d': ('8', 'd', 8), '9d': ('9', 'd', 9), '10d': ('10', 'd', 10), 'Jd': ('w', 'd', 11), 'Qd': ('x', 'd', 12), 'Kd': ('y', 'd', 13), 'Ad': ('z', 'd', 14), '2s': ('2', 's', 2), '3s': ('3', 's', 3), '4s': ('4', 's', 4), '5s': ('5', 's', 5), '6s': ('6', 's', 6), '7s': ('7', 's', 7), '8s': ('8', 's', 8), '9s': ('9', 's', 9), '10s': ('10', 's', 10), 'Js': ('w', 's', 11), 'Qs': ('x', 's', 12), 'Ks': ('y', 's', 13), 'As': ('z', 's', 14), '2c': ('2', 'c', 2), '3c': ('3', 'c', 3), '4c': ('4', 'c', 4), '5c': ('5', 'c', 5), '6c': ('6', 'c', 6), '7c': ('7', 'c', 7), '8c': ('8', 'c', 8), '9c': ('9', 'c', 9), '10c': ('10', 'c', 10), 'Jc': ('w', 'c', 11), 'Qc': ('x', 'c', 12), 'Kc': ('y', 'c', 13), 'Ac': ('z', 'c', 14)}

tempDict = {'d':0,'h':0,'s':0,'c':0}

def checkFlush():
    for k in finalCards:
        for j in tempDict:
            if cardValues[k][1] == j:
                tempDict[j] += 1
    for k in tempDict:
        if tempDict[k] >= 5:
            if checkStrFlush(k) == True:
                print("there's a straight flush")
                 # self.score += #######  set the score for a straight or royal flush
            else:
                checkMatches()
                print("there is NO straight flush")
            return j

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
            if len(tempSuitedValues) == 6:
                tempSuitedValues.pop()
                tempSuitedValues.pop()
            if len(tempSuitedValues) == 5:
                tempSuitedValues.pop()
            if np.sum(tempSuitedValues) == 14: # checks if the remaining four cards are 2,3,4,5
                tempSuitedValues.append(1) # adds Ace with the value of 1
                list.sort(tempSuitedValues)
                suitedValues = tempSuitedValues
                print("lowest straight")
    b = 4 # when sorting and running np.diff, the array will be [1,1,1,1] if there is a straight
    for a in np.diff(suitedValues):
        if a == 1:
            b -= 1
    if b <= 0:
        if len(suitedValues) == 5:
            pass
        if len(suitedValues) == 6:
            list.sort(suitedValues,reversed=True)
            suitedValues.pop()
        if len(suitedValues) == 7:
            list.sort(suitedValues,reversed=True)
            suitedValues.pop()
            suitedValues.pop()
        #self.score += ###### need to set the straight flush level score here
        
        #print("there's a straight flush")
    else:
        return False

def getValueList():
	origCardList = finalCards # self..
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
            print("four of a kind")
            #self.score += ##### four fo a king score
        if zeroInRow == 1:
            print("full house")
            #self.score += ##### full house score
        if zeroInRow == 0:
            print("Two pair")
            #self.score += ##### two pair score
            checkStr()
    if zeroCount == 2:
        if zeroInRow == 1:
            print("Three of a kind")
            #self.score += ###### three of a kind score
            checkStr()
        if zeroInRow == 0:
            print("two pair")
            #self.score += ###### two pari score
            checkStr()
    if zeroCount == 1:
        print("one pair")
        #self.score += ###### one pair score
        checkStr()
        

        
        
    
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
        tempValues.pop()
        tempValues.pop()
        if np.sum(tempValues) == 14: # checks if the remaining four cards are 2,3,4,5
            tempValues.append(1) # adds Ace with the value of 1
            list.sort(tempValues)
            values = tempValues
            print("lowest straight")
    b = 4 # when sorting and running np.diff, the array will be [1,1,1,1] if there is a straight
    for a in np.diff(values):
        if a == 1:
            b -= 1
    if b <= 0:
        print("this is a straight")
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


checkFlush()
checkStr()
#checkMatches()
#print(checkStr())




'''
	define how the array looks when there is a straight, flush. straight flush, pairs, trips or full house.
	Poker hands starting from highest
	
2       royal flush,
      suit check
        
2       straight flush, 
      suit check
        
3        four of a kind,
            3 zerocount 2 inrow
        
4        full house, 
            3 zero count 1 in row
        
1       flush,
      suit check
        
       straight, 
        
6       three of a kind, 
            2 zero count 1 in row
        
7       2 pairs, 
            3 zero count 0 in row
            2 zero count 0 in row
        
8        1 pair, 
            1 zero count 0 in row
        
        high card
    
	

'''
    





































