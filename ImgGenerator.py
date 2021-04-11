#https://stackoverflow.com/questions/384759/how-to-convert-a-pil-image-into-a-numpy-array
import numpy as np
from PIL import Image
from MazeConverter import convert2binary
from WeldingProcessor import makeWeldLines

binaryMaze = convert2binary('maze_test.png')

def convert2Img():

    pixels = makeWeldLines(binaryMaze)
    
    for row in range(len(pixels)):
        for column in range(len(pixels[0])):
            print(pixels[row,column],end='')
        print()

    print("hey")
    img = Image.fromarray(pixels,mode='RGB')
    print("hey")
    img = img.save("finished_processed.png")

convert2Img()