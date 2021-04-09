import numpy as np
from PIL import Image

def convert2binary(filename):
    # Open the maze image and converts it to greyscale
    im = Image.open(filename).convert('L')
    # Gets the dimensions
    w, h = im.size
    print("width: ", w)
    print("height: ", h)

    # We now have greyscale but we want every shade of grey to be 0 and white to be 1
    threshold = 128
    binary = im.point(lambda p: p > threshold)

    # Resize to be able to illustrate in terminal, can be removed when finalizing
    binary = binary.resize((w//2,h//2),Image.NEAREST)
    w, h = binary.size

    # Numpy arrays are best processed in Python
    nim = np.array(binary)
    #adds white space around the maze
    np.append(nim,np.ones(len(nim)))
    print(nim.shape)
    print(type(nim))
    #return(nim)

    #for illustration in terminal
    
    for row in range(h):
        for column in range(w):
            print(nim[row,column],end='')
        print()
    
    
#convert2binary('maze_curvy.png')
convert2binary('maze_test.png')