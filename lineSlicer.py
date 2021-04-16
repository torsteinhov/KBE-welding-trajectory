import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences

from partReading import loadPRTFile, getFaces

aashild_path = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\KBE-welding-trajectory\\prt\\maze_test_3D.prt"
torstein_path = "C:\\Kode\GitHub\\KBE-welding-trajectory\\prt\\maze_test_3D.prt"
path = aashild_path

# find the face with most lines
def findBasePlane():
    theSession = loadPRTFile(path)
    objects = getFaces(theSession)
    aPoint= objects[0][0][0][0][0]
    print("a Point: ", aPoint)

    basePlane = []
    for parts in objects:
        for faces in parts:
            for lines_in_face in faces:
                print("len(lines_in_face): ", len(lines_in_face))
                if len(lines_in_face) > len(basePlane):
                    basePlane= lines_in_face

    print("basePlan: \n", basePlane)
    print("len(baseplan): ", len(basePlane))
    return basePlane

#iterates through a list of two NXOpen 3DPoint Objects and returns start and end point of the line in format [[X,Y,Z],[X,Y,Z]]
def findPoints(line):
    twoPoints = []
    print("line in find points: ", line)
    print("type: ", type(line))
    for point in line:
        strPoint = str(point)
        strPoint = strPoint.split(",")
        pointList = []
        for i in strPoint:
            pkt = i.split("=")[1]
            if pkt.find("]"):
                pkt =pkt.split("]")[0]
            pointList.append(round(float(pkt),1))
        print("pointList: ",pointList)
        twoPoints.append(pointList)
    
    return twoPoints

#basePlane = [line,line,line,line,line]
#line = [[x=50,y=100,z=0],[x=50,y=100,z=0],[x=50,y=100,z=0]]
#point = [x=50,y=100,z=0]



def removeBorderLine(basePlane):
    basePlaneCopy = basePlane
    lineNumberIndex = 0
    x_val = 0
    for i, line in enumerate(basePlane):
        
        points = findPoints(line)
        for j in points:
            if j[0] > x_val:
                lineNumberIndex = i
                basePlaneCopy.pop(i)
    borderLines = [] #[line, line]
    borderLine1 = basePlane[lineNumberIndex]
    borderLines.append(borderLine1)
    
    borderUnCompleted = True
    
    while borderUnCompleted:
        for i, line in basePlaneCopy:
            lineNum = findPoints(line)
            if lineNum[1] == borderLines[0][0]: #borderLine1[1] # if endpoint of last line is the same as the startpoint on next line
                borderLine2 = lineNum
                borderLines.append(borderLine2)
                basePlaneCopy.pop(i)
                break
        if borderLines[0][0] == borderLines[-1][1]:
            borderUnCompleted = True
    
    return basePlaneCopy #the base plane without borders
    
########testing123############
testPlane = findBasePlane()
basePlaneWithoutBorders = removeBorderLine(testPlane)
