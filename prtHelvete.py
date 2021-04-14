#https://docs.plm.automation.siemens.com/data_services/resources/nx/10/nx_api/en_US/custom/nxopen_python_ref/NXOpen.BasePart.html#NXOpen.BasePart

# open and read a prtFile

import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences

#import NXOpen.BasePart

path = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\KBE-welding-trajectory\\prt\\maze_test_3D.prt"
#**** Finding all the edges in PRT file
# NX 1957
# Journal created by andreilo on Mon Apr 12 13:22:45 2021 W. Europe Daylight Time
#
import math
import NXOpen
def main() : 

	theSession  = NXOpen.Session.GetSession()
	workPart = theSession.Parts.Work
	displayPart = theSession.Parts.Display
	# ----------------------------------------------
	#   Menu: File->Open...
	# ----------------------------------------------
	basePart1, partLoadStatus1 = theSession.Parts.OpenActiveDisplay(path, NXOpen.DisplayPartOption.AllowAdditional)
	
	workPart = theSession.Parts.Work # maze
	displayPart = theSession.Parts.Display # maze
	partLoadStatus1.Dispose()
	# ----------------------------------------------
	#   Menu: Tools->Journal->Stop Recording
	# ----------------------------------------------

def getFaces():
	theSession  = NXOpen.Session.GetSession()
	#workPart = theSession.Parts.Work
		
	for partObject in theSession.Parts:
		processPart(partObject)
		
def processPart(partObject):
	for bodyObject in partObject.Bodies:
		processBodyFaces(bodyObject)
		#processBodyEdges(bodyObject)
			
def processBodyFaces(bodyObject):
	for faceObject in bodyObject.GetFaces():
		processFace(faceObject)
			
def processFace(faceObject):
	print("Face found.")
	for edgeObject in faceObject.GetEdges():
		processEdge(edgeObject)
		
def processEdge(edgeObject):
	#Printing vertices
	v1 = edgeObject.GetVertices()[0]
	v2 = edgeObject.GetVertices()[1] 
	print("Vertex 1:", v1)
	print("Vertex 2:", v2)

if __name__ == '__main__':
	main()
	getFaces()

