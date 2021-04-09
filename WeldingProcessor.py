from MazeConverter import convert2binary

print(convert2binary('maze_test.png'))
binaryMaze = convert2binary('maze_test.png')

def makeWeldLines(binaryMaze):
    print("type binaryMaze: ", type(binaryMaze))
    for i in range(1,len(binaryMaze)-1):
        for j in range(1,len(binaryMaze[0])-1):
            if binaryMaze[i][j] == 1 and binaryMaze[i+1][j] == 0:
                binaryMaze[i][j] = 2
            if binaryMaze[i][j] == 1 and binaryMaze[i][j+1] == 0:
                binaryMaze[i][j] = 2
            if binaryMaze[i][j] == 0 and binaryMaze[i+1][j] == 1:
                binaryMaze[i+1][j] = 2
            if binaryMaze[i][j] == 0 and binaryMaze[i][j+1] == 1:
                binaryMaze[i][j+1] = 2
            if binaryMaze[i][j] == 0 and binaryMaze[i+1][j+1] == 1:
                binaryMaze[i+1][j+1] = 2
            if binaryMaze[i+1][j+1] == 0 and binaryMaze[i][j] == 1:
                binaryMaze[i][j] = 2
            if binaryMaze[i][j] == 0 and binaryMaze[i+1][j+1] == 1:
                binaryMaze[i+1][j+1] = 2
            if binaryMaze[i][j] == 0 and binaryMaze[i+1][j-1] == 1:
                binaryMaze[i+1][j-1] = 2
            if binaryMaze[i][j] == 0 and binaryMaze[i+1][j+1] == 1:
                binaryMaze[i+1][j+1] = 2
            if binaryMaze[i][j] == 0 and binaryMaze[i-1][j-1] == 1:
                binaryMaze[i-1][j-1] = 2
            if binaryMaze[i][j] == 0 and binaryMaze[i-1][j+1] == 1:
                binaryMaze[i-1][j+1] = 2

    print(binaryMaze)

    '''

    for row in range(len(binaryMaze)):
        for column in range(len(binaryMaze[0])):
            print(binaryMaze[row,column],end='')
        print()
            
    '''
    return binaryMaze

print(makeWeldLines(binaryMaze))