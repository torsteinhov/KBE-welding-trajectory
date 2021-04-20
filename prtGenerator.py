import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences
import math
from datetime import datetime 

from shapes.Cylinder import Cylinder
from shapes.Sphere import Sphere

from partReading import loadPRTFile, getFaces
from lineSlicer import buildWeldingLines, removeBorderLines, findPoints, findBasePlane

from app.views import updatLogFile

aashild_path = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\KBE-welding-trajectory"
torstein_path = "C:\\Kode\GitHub\\KBE-welding-trajectory"
path = torstein_path

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

    partSaveStatus1 = workPart.SaveAs(path+filename)
    
    partSaveStatus1.Dispose()

def readlogFile():
    logfilePath = yourLocation + "\\LogOrder.txt" 
    if not path.exists(logfilePath):
        print("Error, logfile for production does not exist.")
        return
    f.open(logfilePath, "r")
    linesToBeGenerated = []
    for line in f:
        if (".prt") in line and ("None" in line):
            lineList = line.split(", ")
            linesToBeGenerated.append(lineList)
    f.close()
    
    return linesToBeGenerated

def updateLogFile(order, newLogLine):
    nowObj = datetime.now()
    nowStr = nowObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")

    newLineInFile = nowStr
    for i in range(len(1,order)):
        newLineInFile += order[i]
    
    


def main():
    global yourLocation
    linesToBeGenerated = readlogFile()

    for order in len(linesToBeGenerated):

        infile = linesToBeGenerated[order][-2]
        pathInFile = yourLocation + "\\prt\\"+ infile
        pathOutFile = yourLocation + "\\prtGenerated\\"
        outfile = infile.split(".")[0]+"_generated.prt"

        testPlane = findBasePlane(pathInFile) #BØR HA PATH SOM INPUT PARAMETER?
        basePlaneWithoutBorders = removeBorderLines(testPlane)
        buildWeldingLines(basePlaneWithoutBorders)
        
        saveGeneratedCADFile(pathOutFile, outfile) 
        #satser på at det går bra med flere filer
        newLogLine = order 
        newLogLine[-1] = outfile
        updateLogFile(order, newLogLine)
        print("Vi tar påskehelg")
        
