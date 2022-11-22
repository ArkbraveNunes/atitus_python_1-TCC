import os
from datetime import datetime
import json

def readJsonFile(nameJsonfile, ext = '.json'):
    readFile = open(nameJsonfile + ext, "r")
    jsonData = json.load(readFile)
    readFile.close()
    return jsonData

def extractCodes(codeObjectList):
    listCodes = []
    for item in codeObjectList:
        listCodes.append(item['code'])
    return listCodes

def checkCodesInNotList(listOne, listTwo):
    notMatchesInList = []
    for code in listOne:
        if (code not in listTwo):
            notMatchesInList.append(code)
    return notMatchesInList


def verifyItemInList(firstJSONList, secondJSONList):
    codesListOne = extractCodes(firstJSONList)
    codesListTwo = extractCodes(secondJSONList)

    notMatchesListOne = checkCodesInNotList(codesListOne, codesListTwo)

    notMatchesListTwo = checkCodesInNotList(codesListTwo, codesListOne)

    return { 'notMatchesListOne': notMatchesListOne, 'notMatchesListTwo': notMatchesListTwo }


def mainFunction():
    firstFileName = input('\nInsert a name of first file:')
    firstJSONData = readJsonFile(firstFileName)
    
    secondFileName = input('\nInsert a name of second file:')
    secondJSONData = readJsonFile(secondFileName)

    checkJSONLists = verifyItemInList(firstJSONData, secondJSONData)

    if (len(checkJSONLists['notMatchesListOne']) > 0):
        print('\nThe following codes are only contained in the file:' + firstFileName +'\n' + json.dumps(checkJSONLists['notMatchesListOne'], indent=4))
        input('--------Press any key-------')
    elif (len(checkJSONLists['notMatchesListTwo']) > 0):
        print('\nThe following codes are only contained in the file:' + secondFileName +'\n' + json.dumps(checkJSONLists['notMatchesListTwo'], indent=4))
        input('--------Press any key-------')
    else:
        print('\nBoth lists match')
        input('--------Press any key-------')

if __name__ == "__main__":
    try:
        mainFunction()
    except Exception as e:
        print(e)
