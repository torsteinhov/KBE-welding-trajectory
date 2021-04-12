#this is how the logic will be in MainServer, adjustments in each file (MazeConverter, WeldingProcessor and ImgGenerator) has not been done
#do this when implementing this logic template

import numpy as np
from PIL import Image
from MazeConverter import convert2binary
from WeldingProcessor import makeWeldLines
from ImgGenerator import convert2Img

filename = 'maze_test2.png'

binarymaze = convert2binary(filename)
pixels = makeWeldLines(binaryMaze)

#lagrer en bildefil
convert2Img(pixels)