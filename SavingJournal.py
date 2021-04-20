# NX 1911
# Journal created by Hilde on Tue Apr 20 12:35:40 2021 W. Europe Summer Time
#
import math
import NXOpen
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: File->Save As...
    # ----------------------------------------------
    partSaveStatus1 = workPart.SaveAs("C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\KBE-welding-trajectory\\maze_test_3D_JournalSaving")
    
    partSaveStatus1.Dispose()
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()

def saveGeneratedCADFile(path, filename):
    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display

    partSaveStatus1 = workPart.SaveAs(path+filename)
    
    partSaveStatus1.Dispose()