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

from app.views import updatLogFile(name,email,company,infile,outfile)

aashild_path = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\KBE-welding-trajectory\\prt\\maze_test_3D.prt"
torstein_path = "C:\\Kode\GitHub\\KBE-welding-trajectory\\prt\\maze_v4.prt"
path = torstein_path

#testPlane = findBasePlane()
#basePlaneWithoutBorders = removeBorderLines(testPlane)
#buildWeldingLines(basePlaneWithoutBorders)
#print("Vi tar påskehelg")