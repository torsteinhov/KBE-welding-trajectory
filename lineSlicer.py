import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences

from partReading import loadPRTFile, getFaces

aashild_path = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\KBE-welding-trajectory\\prt\\maze_test_3D.prt"
torstein_path = "C:\\Kode\GitHub\\KBE-welding-trajectory\\prt\\maze_test_3D.prt"
path = torstein_path

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
    #must make point a iterable object
    for j in range(2): #point in line:

        #securety
        #if type(line) == <class 'NXOpen.Point3d'>:
        #    print("NÅ ER DET NOE GALT IGJEN") 
        strPoint = str(line[j])
        strPoint = strPoint.split(",")
        pointList = []
        #print("strPoint: ", strPoint)
        for i in strPoint:
            pkt = i.split("=")[1]
            if pkt.find("]"):
                pkt =pkt.split("]")[0]
            pointList.append(round(float(pkt),1))
        #print("pointList: ",pointList)
        twoPoints.append(pointList)
    
    return twoPoints

#basePlane = [line,line,line,line,line]
#line = [[x=50,y=100,z=0],[x=50,y=100,z=0],[x=50,y=100,z=0]]
#point = [x=50,y=100,z=0]


"""
#this is not working
def removeBorderLine(basePlane):
    basePlaneCopy = basePlane
    lineNumberIndex = 0
    x_val = 0
    for i, line in enumerate(basePlane):
        print("Line(removeBorderLine): ", line)
        points = findPoints(line)
        for j in points:
            if j[0] > x_val:
                x_val = j[0]
                lineNumberIndex = i
    print("lineNumberIndex: ", lineNumberIndex)
    borderLines = [] #[line, line]
    borderLines.append(findPoints(basePlaneCopy.pop(lineNumberIndex)))
    print("Borderlines: ", borderLines)
    print("BasePlaneCopy: ", basePlaneCopy)
    
    #borderLine1 = basePlane[lineNumberIndex]
    #borderLines.append(borderLine1)
    
    borderUnCompleted = True
    
    while borderUnCompleted:
        for i, line in enumerate(basePlaneCopy):
            print("line in borderUnCompleted: ", line)
            
            lineNum = findPoints(line) #[float, float, float]
            if lineNum[0] == borderLines[-1][1]: #borderLine1[1] # if endpoint of last line is the same as the startpoint on next line
                borderLine2 = lineNum
                borderLines.append(borderLine2)
                testVar= basePlaneCopy.pop(i)
                print("Poppede linje: ", testVar)
                break
        if borderLines[0][0] == borderLines[-1][1]:
            borderUnCompleted = True
    
    return basePlaneCopy #the base plane without borders
"""
########testing123############
testPlane = findBasePlane()
basePlaneWithoutBorders = removeBorderLine(testPlane)
