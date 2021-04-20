import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences
import math
from datetime import datetime 
import os
import os.path
from os import path

from shapes.Cylinder import Cylinder
from shapes.Sphere import Sphere

from partReading import loadPRTFile, getFaces
from lineSlicer import buildWeldingLines, removeBorderLines, findPoints, findBasePlane



aashild_path = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\KBE-welding-trajectory"
torstein_path = "C:\\Kode\GitHub\\KBE-welding-trajectory"
yourLocation = aashild_path

#testPlane = findBasePlane()
#basePlaneWithoutBorders = removeBorderLines(testPlane)
#buildWeldingLines(basePlaneWithoutBorders)
#print("Vi tar påskehelg")
#read logfile
#loop for running  through new files

def saveGeneratedCADFile(path, filename):
    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    save = path+"\\"+filename
    print("SAVE: ", save)
    partSaveStatus1 = workPart.SaveAs(save)
    
    partSaveStatus1.Dispose()

def readlogFile(yourLocation):
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

def updateLogFile(order, newLogLine,yourLocation):
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

def main():
    global yourLocation
    linesToBeGenerated = readlogFile(yourLocation)

    for order in range(len(linesToBeGenerated)):

        infile = linesToBeGenerated[order][-2]
        pathInFile = yourLocation + "\\prt\\"+ infile
        pathOutFile = yourLocation + "\\prtGenerated\\"
        outfile = infile.split(".")[0]+"_generated"

        testPlane = findBasePlane(pathInFile) #BØR HA PATH SOM INPUT PARAMETER?
        basePlaneWithoutBorders = removeBorderLines(testPlane)
        buildWeldingLines(basePlaneWithoutBorders)
        
        saveGeneratedCADFile(pathOutFile, outfile) 
        #satser på at det går bra med flere filer
        newLogLine = linesToBeGenerated[order]
        newLogLine[-1] = outfile
        updateLogFile(linesToBeGenerated[order], newLogLine, yourLocation)
        print("Vi tar påskehelg")
        
if __name__ == '__main__':
    main()
