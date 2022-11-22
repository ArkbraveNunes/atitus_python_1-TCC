import os
from datetime import datetime
import json

baseJsonStructure = []
nameFileJson = ''

def createJsonFile():
    file = open(nameFileJson, "w")
    file.write(json.dumps(baseJsonStructure, indent=4))
    file.close()

def writeJsonFile(jsonData):
    writeFile = open(nameFileJson, "w")
    writeFile.write(json.dumps(jsonData, indent=4))
    writeFile.close()

def readJsonFile():
    readFile = open(nameFileJson, "r")
    jsonData = json.load(readFile)
    readFile.close()
    return jsonData

def saveData(codex, datex):
    jsonData = readJsonFile()
    print(jsonData)
    jsonData.append(dict(code=codex, date=datex))
    writeJsonFile(jsonData)



def mainFunction():
    while True:
        code = input('\nInsert a code:')
        date=datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        saveData(code, date)

if __name__ == "__main__":
    try:
        nameFileJson = 'file_' + datetime.now().strftime('%d%m%Y%H%M%S%f') + '.json'
        createJsonFile()
        mainFunction()
    except Exception as e:
        print(e)

