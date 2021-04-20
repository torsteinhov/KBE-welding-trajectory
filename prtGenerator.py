import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences
import math

from shapes.Cylinder import Cylinder
from shapes.Sphere import Sphere

from partReading import loadPRTFile, getFaces
from lineSlicer import buildWeldingLines, removeBorderLines, findPoints, findBasePlane

from app.views import updatLogFile

aashild_path = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\KBE-welding-trajectory\\prt\\maze_test_3D.prt"
torstein_path = "C:\\Kode\GitHub\\KBE-welding-trajectory\\prt\\maze_v4.prt"
path = torstein_path

#testPlane = findBasePlane()
#basePlaneWithoutBorders = removeBorderLines(testPlane)
#buildWeldingLines(basePlaneWithoutBorders)
#print("Vi tar påskehelg")
read logfile
loop for running  through new files

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
        if (".prt") in line and ("None" in file):
            lineList = line.split(", ")
            linesToBeGenerated.append(lineList)
    
    return linesToBeGenerated

def main():
    linesToBeGenerated = readlogFile():

    for order in len(linesToBeGenerated):

        infile = linesToBeGenerated[order][-2]
        pathInFile = yourLocation + "\\prt\\"+ infile
        pathOutFile = yourLocation + "\\prtGenerated\\"
        outfile = infile.split(".")[]+"_generated.prt"

        testPlane = findBasePlane() #BØR HA PATH SOM INPUT PARAMETER?
        basePlaneWithoutBorders = removeBorderLines(testPlane)
        buildWeldingLines(basePlaneWithoutBorders)
        
        saveGeneratedCADFile(pathOutFile, outfile)

        print("Vi tar påskehelg")
        
