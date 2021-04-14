#https://stackoverflow.com/questions/384759/how-to-convert-a-pil-image-into-a-numpy-array
import numpy as np
from PIL import Image
from MazeConverter import convert2binary
from WeldingProcessor import makeWeldLines

binaryMaze = convert2binary('maze_test2.png')

def convert2Img():

    pixels = makeWeldLines(binaryMaze)
    
    img = Image.fromarray(pixels,mode='CMYK')
    img = img.save("finished_processed.jpg")

convert2Img()