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

def removeBorderLines(basePlane):
    basePlaneCopy = basePlane
    lineNumberIndex = 0
    x_length = 0
    for i, line in enumerate(basePlaneCopy):
        print("Line(removeBorderLine): ", line)
        points = findPoints(line)
        if abs(points[0][0]-points[1][0]) > x_length:
            x_length = abs(points[0][0]-points[1][0])
            lineNumberIndex = i
    print("lineNumberIndex: ", lineNumberIndex)
    borderLines = [] #[line, line]
    borderLines.append(findPoints(basePlaneCopy.pop(lineNumberIndex)))
    print("Borderlines: ", borderLines)
    print("BasePlaneCopy: ", basePlaneCopy)

    x_length = 0
    for i, line in enumerate(basePlaneCopy):
        print("Line(removeBorderLine): ", line)
        points = findPoints(line)
        if abs(points[0][0]-points[1][0]) > x_length:
            x_length = abs(points[0][0]-points[1][0])
            lineNumberIndex = i
    print("lineNumberIndex: ", lineNumberIndex)
    borderLines.append(findPoints(basePlaneCopy.pop(lineNumberIndex)))
    print("Borderlines: ", borderLines)
    print("BasePlaneCopy: ", basePlaneCopy)

    y_length = 0
    for i, line in enumerate(basePlaneCopy):
        print("Line(removeBorderLine): ", line)
        points = findPoints(line)
        if abs(points[0][1]-points[1][1]) > y_length:
            y_length = abs(points[0][1]-points[1][1])
            lineNumberIndex = i
    print("lineNumberIndex: ", lineNumberIndex)
    borderLines.append(findPoints(basePlaneCopy.pop(lineNumberIndex)))

    y_length = 0
    for i, line in enumerate(basePlaneCopy):
        print("Line(removeBorderLine): ", line)
        points = findPoints(line)
        if abs(points[0][1]-points[1][1]) > y_length:
            y_length = abs(points[0][1]-points[1][1])
            lineNumberIndex = i
    print("lineNumberIndex: ", lineNumberIndex)
    borderLines.append(findPoints(basePlaneCopy.pop(lineNumberIndex)))

    print("BorderLines: ", borderLines)
    print("Lengde av basePlaneCopy etter popping: ", len(basePlaneCopy))

    return basePlaneCopy #weldinglines



########testing123############
testPlane = findBasePlane()
basePlaneWithoutBorders = removeBorderLines(testPlane)
print("Vi tar påskehelg")
