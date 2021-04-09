from MazeConverter import convert2binary

print(convert2binary('maze_test.png'))
binaryMaze = convert2binary('maze_test.png')

def makeWeldLines(binaryMaze):

    '''
    for i in range(len(binaryMaze)):
        for j in range(len(binaryMaze[0])):

            if i == 0 and j == 0:
                #what happens in first element

            elif i == len(binaryMaze)-1 and j == len(binaryMaze[0])-1:
                #what happens in last element

            elif i == 0 and j == len(binaryMaze[0])-1:
                #what happens in top right corner element

            elif i == len(binaryMaze)-1 and j == 0:
                #what happens in bottom left corner element

            elif i == 0:
                #what happens in first row    

            elif i == len(binaryMaze)-1:
                #what happens in last row

            elif j == 0:
                #what happens in first column
            
            elif j == len(binaryMaze[0])-1:
                #what happens in last column

            else:
    '''       