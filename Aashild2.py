import os
import os.path
from os import path
aashild_path = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\KBE-welding-trajectory"
yourLocation = aashild_path


def readlogFile():
    logfilePath = yourLocation + "\\LogOrder.txt" 
    if not path.exists(logfilePath):
        print("Error, logfile for production does not exist.")
        return
    f=open(logfilePath, "r")
    linesToBeGenerated = []
    for line in f:
        if (".prt") in line and ("None" in line):
            lineList = line.split(", ")
            linesToBeGenerated.append(lineList)

    f.close()
    
    return linesToBeGenerated

test = readlogFile()
print(test)

order = ['20-Apr-2021 (08:03:25.532371)', 'Mats PER', 'mats@PER.no', 'PER AS', 'Mats_PERPER_ASnr2.prt', 'None.\n']