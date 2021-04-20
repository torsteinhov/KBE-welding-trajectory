import os
import os.path
from os import path
from datetime import datetime
aashild_path = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\KBE-welding-trajectory"
yourLocation = aashild_path

def readlogFile():
    logfilePath = yourLocation + "\\LogOrder.txt" 
    if not path.exists(logfilePath):
        print("Error, logfile for production does not exist.")
        return
    f=open(logfilePath, "r")
    linesToBeGenerated = []
    for line in f:
        if (".prt") in line and ("None" in line):
            lineList = line.split(", ")
            linesToBeGenerated.append(lineList)

    f.close()
    
    return linesToBeGenerated

test = readlogFile()
print(test)

order = ['20-Apr-2021 (08:03:25.532371)', 'Mats PER', 'mats@PER.no', 'PER AS', 'Mats_PERPER_ASnr2.prt', 'None.\n']
newLogLine = ['20-Apr-2021 (08:03:25.532371)', 'Mats PER', 'mats@PER.no', 'PER AS', 'Mats_PERPER_ASnr2.prt', 'Mats_PERPER_ASnr2_generated.prt']

def updateLogFile(order, newLogLine):
    nowObj = datetime.now()
    nowStr = nowObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")

    newLineInFile = "\n"+ nowStr + ", "
    oldLineInFile = ""
    for i in range(len(order)):
        if i == len(order)-1:
            oldLineInFile+=order[i] + "."
        else:
            oldLineInFile+=order[i] + ", "
    for i in range(1,len(newLogLine)):
        if i == len(newLogLine)-1:
            newLineInFile += newLogLine[i]+"."
        else:
            newLineInFile += newLogLine[i] + ", "

    logfilePath = yourLocation + "\\LogOrder.txt" 
    f = open(logfilePath, "r") 
    lines = f.readlines()
    f.close()
    g = open(logfilePath, "w")
    print("old line: ", oldLineInFile)
    print("new line: ", newLineInFile)
    for line in lines:

        if oldLineInFile != line: # NOT WORKING
            print("ikke det vi vil slette: ", line)
            g.write(line)
    
    g.close()
    f = open(logfilePath,"a")
    f.write(newLineInFile)
    f.close

updateLogFile(order, newLogLine)

"""
testList = ["hei", "hallo"]
for i in range(len(testList)):
    if "a" in testList[i]:
        testList.pop(i)
print(testList)

testSTR = "HeiPåDeg"
if "Hei" in testSTR:
    testSTR = "sant"
print(testSTR)
matsG ="20-Apr-2021 (08:03:25.532371), Mats PER, mats@PER.no, PER AS, Mats_PERPER_ASnr2.prt, None."
matsN = " Mats PER, mats@PER.no, PER AS, Mats_PERPER_ASnr2.prt, None."

if matsN not in matsG:
    print("hei")
else: 
    print("hallo")
"""
oldLine =   "20-Apr-2021 (08:03:25.532371), Mats PER, mats@PER.no, PER AS, Mats_PERPER_ASnr2.prt, None."
wantToRemove ="20-Apr-2021 (08:03:25.532371), Mats PER, mats@PER.no, PER AS, Mats_PERPER_ASnr2.prt, None."

if oldLine == wantToRemove:
    print("DE ER LIKE")