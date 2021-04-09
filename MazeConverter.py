import numpy as np
from PIL import Image

def convert2binary(filename):
    # Open the maze image and converts it to greyscale
    im = Image.open(filename).convert('L')
    # Gets the dimensions
    w, h = im.size

    # We now have greyscale but we want every shade of grey to be 0 and white to be 1
    binary = im.point(lambda p: p > 128 and 1)


    # Resize to be able to illustrate in terminal, can be removed when finalizing
    binary = binary.resize((w//2,h//2),Image.NEAREST)
    w, h = binary.size

    # Numpy arrays are best processed in Python
    nim = np.array(binary)

    for r in range(h):
        for c in range(w):
            print(nim[r,c],end='')
        print()


convert2binary('maze_test.png')