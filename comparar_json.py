import os
from datetime import datetime
import json

reportNameFile = 'file_' + datetime.now().strftime('%d_%m_%Y_%H_%M_%S_%f') + '_report'

def createReportTxtFile(firstFileName, secondFileName):
    file = open(reportNameFile  + '.txt', "w")
    file.write('Report referring to the comparison of inventories ' + firstFileName + ' and ' + secondFileName +'\n')
    file.close()

def writeReportTxtFile(nameTxtFile, txtData, ext = '.txt'):
    writeFile = open(reportNameFile + ext, "a+")
    writeFile.write(txtData + '\n')
    writeFile.close()

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
    auxListTwo = listTwo.copy()
    notMatchesInList = []
    for code in listOne:
        if (code in auxListTwo):
         auxListTwo.remove(code)
        # if (code not in listTwo):
        else:
            notMatchesInList.append(code)
    return notMatchesInList

def writeReport(dataText, fileName, notMatchesList = []):
    reportText = dataText + fileName + '\n' + json.dumps(notMatchesList, indent=4) + '\n'
    print(reportText)
    writeReportTxtFile(reportNameFile, reportText)

def verifyItemInList(firstJSONList, firstFileName, secondJSONList, secondFileName):
    codesListOne = extractCodes(firstJSONList)
    codesListTwo = extractCodes(secondJSONList)

    notMatchesListOne = checkCodesInNotList(codesListOne, codesListTwo)

    notMatchesListTwo = checkCodesInNotList(codesListTwo, codesListOne)

    if (len(notMatchesListOne) > 0):
        writeReport('\nThe following codes are only contained in the file: ', firstFileName, notMatchesListOne)

    if (len(notMatchesListTwo) > 0):
        writeReport('\nThe following codes are only contained in the file: ', secondFileName, notMatchesListTwo)



    # return { 'notMatchesListOne': notMatchesListOne, 'notMatchesListTwo': notMatchesListTwo }


def mainFunction():
    firstFileName = input('\nInsert a name of first file: ')
    firstJSONData = readJsonFile(firstFileName)
    
    secondFileName = input('\nInsert a name of second file: ')
    secondJSONData = readJsonFile(secondFileName)

    createReportTxtFile(firstFileName, secondFileName)

    # checkJSONLists = verifyItemInList(firstJSONData, secondJSONData)
    verifyItemInList(firstJSONData, firstFileName, secondJSONData, secondFileName)

    # if (len(checkJSONLists['notMatchesListOne']) > 0):
    #     print('\nThe following codes are only contained in the file:' + firstFileName +'\n' + 
    #     json.dumps(checkJSONLists['notMatchesListOne'], indent=4))
    #     input('--------Press any key-------')
    # if (len(checkJSONLists['notMatchesListTwo']) > 0):
    #     print('\nThe following codes are only contained in the file:' + secondFileName +'\n' + 
    #     json.dumps(checkJSONLists['notMatchesListTwo'], indent=4))
    #     input('--------Press any key-------')
    # else:
    #     print('\nBoth lists match')
    #     input('--------Press any key-------')

if __name__ == "__main__":
    try:
        mainFunction()
    except Exception as e:
        print(e)
