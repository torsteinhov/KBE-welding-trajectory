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

testPlane = findBasePlane()
lineNumberIndex = 0
x-val = 0
for i, line in enumerate(testPlane):
    print("Line: ", line)
    print("points: ", line[0], line[1])
    print("type point: ", type(str(line[0])))
    print("x-val: ", line[0][0])

    for point in line:
        strPoint = str(line[0])
        # finn x-verdi
        #hvis x>x-val
            #lineNumberIndex=i

    # finn 