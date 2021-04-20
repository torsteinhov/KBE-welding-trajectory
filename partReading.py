#https://docs.plm.automation.siemens.com/data_services/resources/nx/10/nx_api/en_US/custom/nxopen_python_ref/NXOpen.BasePart.html#NXOpen.BasePart

# open and read a prtFile

import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences

#import NXOpen.BasePart

#aashild_path = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\KBE-welding-trajectory\\prt\\maze_test_3D.prt"
#torstein_path = "C:\\Kode\GitHub\\KBE-welding-trajectory\\prt\\maze_test_3D.prt"
#path = aashild_path


def loadPRTFile(path):
	theSession  = NXOpen.Session.GetSession()
	workPart = theSession.Parts.Work
	displayPart = theSession.Parts.Display

	basePart1, partLoadStatus1 = theSession.Parts.OpenActiveDisplay(path, NXOpen.DisplayPartOption.AllowAdditional)
	
	workPart = theSession.Parts.Work # maze
	displayPart = theSession.Parts.Display # maze
	partLoadStatus1.Dispose()

	return theSession


def getFaces(theSession):
	theSession  = NXOpen.Session.GetSession()
	#workPart = theSession.Parts.Work
	objects = []	
	for partObject in theSession.Parts:
		objects.append(processPart(partObject))
	
	print("objects: \n", objects)
	return objects
		
def processPart(partObject):
	parts = []
	for bodyObject in partObject.Bodies:
		parts.append(processBodyFaces(bodyObject))
		#processBodyEdges(bodyObject)
	
	print("Parts: \n", parts)
	return parts
			
def processBodyFaces(bodyObject):
	faces = []
	for faceObject in bodyObject.GetFaces():
		faces.append(processFace(faceObject))
	
	print("Faces: \n", faces)
	return faces
			
def processFace(faceObject):
	print("Face found.")
	lines_in_face = []
	for edgeObject in faceObject.GetEdges():
		lines_in_face.append(processEdge(edgeObject))
	print("lines in face: \n", lines_in_face)
	return lines_in_face
		
def processEdge(edgeObject):
	#Printing vertices
	v1 = edgeObject.GetVertices()[0]
	v2 = edgeObject.GetVertices()[1] 
	print("Vertex 1:", v1)
	print("Vertex 2:", v2)

	line =[v1,v2]
	return line

#if __name__ == '__main__':
	#main()
#theSession = loadPRTFile(path)
#objects = getFaces(theSession)
#aPoint= objects[0][0][0][0][0]
#print("a Point: ", aPoint)

