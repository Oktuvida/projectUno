from deck import colorCards

# Identifica si en la baraja de un jugador hay alguna carta válida para jugar
def findEqualCard(playerDeck:list, aDict):
    for element in playerDeck: 
        if (isEqual(element, aDict)==True):
            return True
    return False

# Identifica si una carta es válida para jugar con otra carta.
def isEqual(playerDict, aDict):
    try:
        playerDictCon = dict(list(playerDict.values())[0])
        playerKey = list(playerDictCon.keys())[0]
        playerValue = list(playerDictCon.values())[0]
    except:
        return True

    try:
        aDictCon = dict(list(aDict.values())[0])
        aKey = list(aDictCon.keys())[0]
        aValue = list(aDictCon.values())[0]
    except:
        if list(aDict.values())[0] == playerKey:
            return True
        elif isinstance(aDict, str) and aDict == playerKey:
            return True
        else:
            return False
    
    if not ("+2") in aValue and ((playerKey == aKey) or (playerValue == aValue)):
        
        return True
    elif ("+2" in aValue or "+4" in aValue) and aValue == playerValue:
        return True
    else:
        return False

# Identifica si la carta jugada es cambio de color.
def changeColor(a):
    b = list(a.values())[0]
    if isinstance(b, str) and "change color" in b.lower():
        return True
    else:
        return False

# Identifica si la carta jugada es +4
def isPlusFour(a):
    b = list(a.values())[0]
    if isinstance(b, str) and "+4" in b:
        return True
    else:
        return False

# Identifica si la carta jugada es block
def blockCard(a, counter):
    b = list(a.values())[0]
    aBool = False
    if isinstance(b, dict):
        bValues = list(b.values())[0]
        if bValues == "Block" and counter%2==0:
            counter +=1
            aBool = True
            return counter, aBool
    return counter, aBool

# Identifica si la carta jugada es inverse
def reverseCard(a, counter):
    b = list(a.values())[0]
    aBool = False
    if isinstance(b, dict):
        bValues = list(b.values())[0]
        if bValues == "Change direction" and counter%2==0:
            counter +=1
            aBool = True
            return counter, aBool
    return counter, aBool