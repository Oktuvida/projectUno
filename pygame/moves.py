from deck import colorCards

def findEqualCard(playerDeck:list, aDict):
    for element in playerDeck: 
        if (isEqual(element, aDict)==True):
            return True
    return False


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
        correctWord = False
        while not correctWord:
            try:
                aKey = str(input("Digite un color: ")).capitalize()
                if "+4" in aDict:
                    aValue = "+4"
                else:
                    aValue = None                   
                if not (aKey in colorCards()):
                    print("Error. Color o palabra no disponible.\n")
                    continue
            except ValueError:
                print("Usted no digitó un color o palabra.\n")
            else:
                correctWord = True

    if (playerKey == aKey) or (playerValue == aValue):
        return True
    else:
        return False
