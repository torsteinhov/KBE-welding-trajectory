#https://docs.plm.automation.siemens.com/data_services/resources/nx/10/nx_api/en_US/custom/nxopen_python_ref/NXOpen.BasePart.html#NXOpen.BasePart

# open and read a prtFile

import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences


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
	objects = []	
	for partObject in theSession.Parts:
		objects.append(processPart(partObject))
	
	return objects
		
def processPart(partObject):
	parts = []
	for bodyObject in partObject.Bodies:
		parts.append(processBodyFaces(bodyObject))

	return parts
			
def processBodyFaces(bodyObject):
	faces = []
	for faceObject in bodyObject.GetFaces():
		faces.append(processFace(faceObject))
	
	return faces
			
def processFace(faceObject):

	lines_in_face = []
	for edgeObject in faceObject.GetEdges():
		lines_in_face.append(processEdge(edgeObject))

	return lines_in_face
		
def processEdge(edgeObject):
	#Printing vertices
	v1 = edgeObject.GetVertices()[0]
	v2 = edgeObject.GetVertices()[1] 

	line =[v1,v2]
	return line