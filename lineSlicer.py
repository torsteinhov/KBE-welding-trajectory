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

#aashild_path = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\KBE-welding-trajectory\\prt\\maze_test_3D.prt"
#torstein_path = "C:\\Kode\GitHub\\KBE-welding-trajectory\\prt\\maze_v4.prt"
#path = torstein_path

# find the face with most lines
def findBasePlane(path):
    theSession = loadPRTFile(path)
    objects = getFaces(theSession)
    aPoint= objects[0][0][0][0][0]

    basePlane = []
    for parts in objects:
        for faces in parts:
            for lines_in_face in faces:
                
                if len(lines_in_face) > len(basePlane):
                    basePlane= lines_in_face

    return basePlane

#iterates through a list of two NXOpen 3DPoint Objects and returns start and end point of the line in format [[X,Y,Z],[X,Y,Z]]
def findPoints(line):
    twoPoints = []

    #must make point a iterable object
    for j in range(2): #point in line:

        #securety
        #if type(line) == <class 'NXOpen.Point3d'>:

        strPoint = str(line[j])
        strPoint = strPoint.split(",")
        pointList = []

        for i in strPoint:
            pkt = i.split("=")[1]
            if pkt.find("]"):
                pkt =pkt.split("]")[0]
            pointList.append(round(float(pkt),1))

        twoPoints.append(pointList)
    
    return twoPoints


def removeBorderLines(basePlane):
    basePlaneCopy = basePlane
    lineNumberIndex = 0
    x_length = 0
    for i, line in enumerate(basePlaneCopy):

        points = findPoints(line)
        if abs(points[0][0]-points[1][0]) > x_length:
            x_length = abs(points[0][0]-points[1][0])
            lineNumberIndex = i

    borderLines = [] #[line, line]
    borderLines.append(findPoints(basePlaneCopy.pop(lineNumberIndex)))


    x_length = 0
    for i, line in enumerate(basePlaneCopy):

        points = findPoints(line)
        if abs(points[0][0]-points[1][0]) > x_length:
            x_length = abs(points[0][0]-points[1][0])
            lineNumberIndex = i

    borderLines.append(findPoints(basePlaneCopy.pop(lineNumberIndex)))

    y_length = 0
    for i, line in enumerate(basePlaneCopy):

        points = findPoints(line)
        if abs(points[0][1]-points[1][1]) > y_length:
            y_length = abs(points[0][1]-points[1][1])
            lineNumberIndex = i

    borderLines.append(findPoints(basePlaneCopy.pop(lineNumberIndex)))

    y_length = 0
    for i, line in enumerate(basePlaneCopy):

        points = findPoints(line)
        if abs(points[0][1]-points[1][1]) > y_length:
            y_length = abs(points[0][1]-points[1][1])
            lineNumberIndex = i

    borderLines.append(findPoints(basePlaneCopy.pop(lineNumberIndex)))

    return basePlaneCopy #weldinglines

def buildWeldingLines(weldinglines):
    for line in weldinglines:
        points = findPoints(line)
        startPoint = points[0]
        endPoint = points[1]

        dimensions = []

        zip_object = zip(startPoint, endPoint)
        for startPoint_i, endPoint_i in zip_object:
            dimensions.append(startPoint_i-endPoint_i)
        
        cylLength = math.sqrt(dimensions[0]**2+dimensions[1]**2+dimensions[2]**2)

        weldingDia = 10
        base1 = Cylinder(endPoint[0], endPoint[1], endPoint[2], weldingDia, cylLength, dimensions, "YELLOW", "Wood")
        base1.initForNX()

        corners = Sphere(endPoint[0], endPoint[1], endPoint[2], weldingDia, "YELLOW", "Wood")
        corners.initForNX()

