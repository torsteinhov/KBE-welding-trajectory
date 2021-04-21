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

#order = ['20-Apr-2021 (08:03:25.532371)', 'Mats PER', 'mats@PER.no', 'PER AS', 'Mats_PERPER_ASnr2.prt', 'None.\n']
order = ['21-Apr-2021 (17:10:12.217403), Mats PER', 'mats@PER.no', 'PER AS', 'Mats_PERPER_ASnr2.prt', 'None.\n']
         #21-Apr-2021 (17:10:12.217403), Mats PER, mats@PER.no, PER AS, Mats_PERPER_ASnr2.prt, None.

newLogLine = ['20-Apr-2021 (08:03:25.532371)', 'Mats PER', 'mats@PER.no', 'PER AS', 'Mats_PERPER_ASnr2.prt', 'Mats_PERPER_ASnr2_generated.prt']

def updateLogFile(order, newLogLine):
    nowObj = datetime.now()
    nowStr = nowObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")

    newLineInFile = nowStr + ", "
    oldLineInFile = ""
    for i in range(len(order)):
        if i == len(order)-1:
            oldLineInFile+=order[i].strip("\n")
        else:
            oldLineInFile+=order[i] + ", "
    for i in range(1,len(newLogLine)):
        if i == len(newLogLine)-1:
            newLineInFile += newLogLine[i] + "."
        else:
            newLineInFile += newLogLine[i] + ", "

    logfilePath = yourLocation + "\\LogOrder.txt" 
    f = open(logfilePath, "r") # opening the file
    lines = f.readlines() # stores the content in a list
    f.close() #close the file

    g = open(logfilePath, "w") # opening the file with writing premissions
    print("old line: ", oldLineInFile)
    print("new line: ", newLineInFile)
    for line in lines:

        if line.strip("\n") != oldLineInFile:#"21-Apr-2021 (17:10:12.217403), Mats PER, mats@PER.no, PER AS, Mats_PERPER_ASnr2.prt, None.": # NOT WORKING
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
"""
a_file = open("sample.txt", "r")


lines = a_file.readlines()
a_file.close()

new_file = open("sample.txt", "w")
for line in lines:
    if line.strip("\n") != "hvordan har du det?":
#Delete "line2" from new_file

        new_file.write(line)

new_file.close()
"""