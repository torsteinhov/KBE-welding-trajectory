import numpy as np
from PIL import Image

def convert2binary(filename):
    # Open the maze image and converts it to greyscale
    im = Image.open(filename).convert('L')
    # Gets the dimensions
    w, h = im.size
    '''
    print("width: ", w)
    print("height: ", h)
    print("im: ", im)
    '''

    # We now have greyscale but we want every shade of grey to be 0 and white to be 1
    threshold = 128
    binary = im.point(lambda p: p > threshold)

    # Resize to be able to illustrate in terminal, can be removed when finalizing
    binary = binary.resize((w//2,h//2),Image.NEAREST)
    w, h = binary.size

    # Numpy arrays are best processed in Python
    nim = np.array(binary)

    #adds white space around the maze to simplify search for the WeldingProcessor, it therefore only has to check space in front of and under
    verticalVector = np.full(shape=h,fill_value=1,dtype=np.int).reshape(len(nim),1)
    horizontalVector = np.full(shape=w+2,fill_value=1,dtype=np.int)
    '''
    print("verticalVector: ",verticalVector)
    print("horizontalVector: ", horizontalVector)
    print("shape horizontalVector: ", horizontalVector.shape)
    print("shape verticalVector: ", verticalVector.shape)
    print("nim: ", nim)
    '''

    Img = np.block([[horizontalVector],[verticalVector,nim,verticalVector],[horizontalVector]])

    return Img

    #for illustration in terminal
    '''
    for row in range(h+2):
        for column in range(w+2):
            print(Img[row,column],end='')
        print()
    '''
    
    
#convert2binary('maze_curvy.png')
#convert2binary('maze_test.png')