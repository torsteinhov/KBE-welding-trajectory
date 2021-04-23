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

#aashild_path = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\KBE-welding-trajectory"
#torstein_path = "C:\\Kode\GitHub\\KBE-welding-trajectory"
processEngineer_path = <YOUR_PATH_HERE>
yourLocation = processEngineer_path

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

def updateLogFile(order, newLogLine, yourLocation):
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
            newLineInFile += newLogLine[i] + ".\n"
        else:
            newLineInFile += newLogLine[i] + ", "

    logfilePath = yourLocation + "\\LogOrder.txt" 
    f = open(logfilePath, "r") # opening the file
    lines = f.readlines() # stores the content in a list
    f.close() #close the file

    g = open(logfilePath, "w") # opening the file with writing premissions
    print("\nold line: ", oldLineInFile)
    print("\nnew line: ", newLineInFile)
    for line in lines:

        if line.strip("\n") != oldLineInFile:
            g.write(line)
    
    g.close()
    f = open(logfilePath,"a")
    f.write(newLineInFile)
    f.close

def main():
    global yourLocation
    linesToBeGenerated = readlogFile(yourLocation)

    for order in range(len(linesToBeGenerated)):
        print("\nNew order: ", linesToBeGenerated[order])
        infile = linesToBeGenerated[order][-2]
        pathInFile = yourLocation + "\\prt\\"+ infile
        pathOutFile = yourLocation + "\\prtGenerated\\"
        outfile = infile.split(".")[0]+"_generated"
        
        testPlane = findBasePlane(pathInFile)
        basePlaneWithoutBorders = removeBorderLines(testPlane)
        buildWeldingLines(basePlaneWithoutBorders)
        
        saveGeneratedCADFile(pathOutFile, outfile) 
        
        newLogLine = linesToBeGenerated[order].copy()
        
        newLogLine[-1] = outfile + ".prt"
        
        updateLogFile(linesToBeGenerated[order], newLogLine, yourLocation)
        print("\nVi tar påskehelg")
        
if __name__ == '__main__':
    main()
