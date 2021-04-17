#https://stackoverflow.com/questions/384759/how-to-convert-a-pil-image-into-a-numpy-array
import numpy as np
from PIL import Image

#takes in a file, transforms to greyscale and then transforms to binary and returns a np.array
def convert2binary(filename):
    # Open the maze image and converts it to greyscale
    im = Image.open(filename).convert('L')
    # Gets the dimensions
    w, h = im.size

    # We now have greyscale but we want every shade of grey to be 0 and white to be 1
    threshold = 128
    binary = im.point(lambda p: p > threshold)

    nim = np.array(binary)

    #adds white space around the maze to simplify search for the WeldingProcessor, it therefore only has to check space in front of and under
    verticalVector = np.full(shape=h,fill_value=1,dtype=np.int).reshape(len(nim),1)
    horizontalVector = np.full(shape=w+2,fill_value=1,dtype=np.int)

    Img = np.block([[horizontalVector],[verticalVector,nim,verticalVector],[horizontalVector]])

    return Img

#takes in a binary np.array and based on where it finds "walls", generates a welding line in the indexes around the wall.
def makeWeldLines(binaryMaze):

    for i in range(1,len(binaryMaze)-1):
        for j in range(1,len(binaryMaze[0])-1):
            if binaryMaze[i][j] == 1 and binaryMaze[i+1][j] == 0:
                binaryMaze[i][j] = 255
            if binaryMaze[i][j] == 1 and binaryMaze[i][j+1] == 0:
                binaryMaze[i][j] = 255
            if binaryMaze[i][j] == 0 and binaryMaze[i+1][j] == 1:
                binaryMaze[i+1][j] = 255
            if binaryMaze[i][j] == 0 and binaryMaze[i][j+1] == 1:
                binaryMaze[i][j+1] = 255
            if binaryMaze[i][j] == 0 and binaryMaze[i+1][j+1] == 1:
                binaryMaze[i+1][j+1] = 255
            if binaryMaze[i+1][j+1] == 0 and binaryMaze[i][j] == 1:
                binaryMaze[i][j] = 255
            if binaryMaze[i][j] == 0 and binaryMaze[i+1][j+1] == 1:
                binaryMaze[i+1][j+1] = 255
            if binaryMaze[i][j] == 0 and binaryMaze[i+1][j-1] == 1:
                binaryMaze[i+1][j-1] = 255
            if binaryMaze[i][j] == 0 and binaryMaze[i+1][j+1] == 1:
                binaryMaze[i+1][j+1] = 255
            if binaryMaze[i][j] == 0 and binaryMaze[i-1][j-1] == 1:
                binaryMaze[i-1][j-1] = 255
            if binaryMaze[i][j] == 0 and binaryMaze[i-1][j+1] == 1:
                binaryMaze[i-1][j+1] = 255

    #for illustration purposes in Terminal
    '''
    for row in range(len(binaryMaze)):
        for column in range(len(binaryMaze[0])):
            print(binaryMaze[row,column],end='')
        print()
    '''
    return binaryMaze

#takes in the processed binaryMaze and with a function .fromarray() transforms back to .jpg format with finished welding lines
def convert2Img(pixels, saveName):
    
    img = Image.fromarray(pixels,mode='CMYK')
    img = img.save(saveName)

def runImgGenerator(filename, saveName):

    binaryMaze = convert2binary(filename)
    pixels = makeWeldLines(binaryMaze)
    convert2Img(pixels, saveName)

#runImgGenerator("ImgWeldLinesGenerator\\img_mazes\\maze_test2.png")