import warehouse
import config

w=warehouse.w
scale=config.scale

# input: warehouse template
# output: 2D array of [0,0],"x",False] cells to be
#         filled in later
#name:
#args:
#returns:
#effect:
def createEmptyMatrix(w):
    m=[]
    for row in range (len(w)):
        n=[]
        for col in range(len((w[row])[0])):
            n.append([[0,0],"x",False])
        m.append(n)


    return m
#input: warehouse template
#output: [['x', '', ''......]....]

#name:
#args:
#returns:
#effect:
def splitTemplateRowsIntoDistinctListsOfSingleCharacters(input):
    matrix = []
    for row in range(len(input)):
        for col in range(len(input[0])):
            matrix.append(list(map(str, (input[row])[col])))

    return matrix

#name:
#args:
#returns:
#effect:
def assignCoordinates(row,column):
    hCoord = column*scale
    vCoord = row*scale
    return[hCoord,vCoord]

# input: list of single characters, empty matrix
# output: matrix with all fields complete
#name:
#args:
#returns:
#effect:
def addDetailsToMatrix(listOfSingleCharacters,emptyMatrix):
    numRowsinEmptyMatrix = len(emptyMatrix)
    numColumnsinEmptyMatrix = len(emptyMatrix[0])
    for row in range(numRowsinEmptyMatrix):
        for col in range(numColumnsinEmptyMatrix):
            ((emptyMatrix[row])[col])[0]=assignCoordinates(row,col)
            ((emptyMatrix[row])[col])[1]=listOfSingleCharacters[row][col]
            ((emptyMatrix[row])[col])[2]=False
    finalMatrix=emptyMatrix
    return finalMatrix

emptyMatrix = createEmptyMatrix(w)

listOfSingleCharacters = splitTemplateRowsIntoDistinctListsOfSingleCharacters(w)
#name:
#args:
#returns:
#effect:
def getMatrix():
    return addDetailsToMatrix(listOfSingleCharacters,emptyMatrix)


#name:
#args:
#returns:
#effect:
def getInitialForkliftCoordinates():
    temp = getMatrix()
    for row in temp:
        for col in row:
            if col[1]=='f':
                tempCol = (col[0])[0]
                tempRow = (col[0])[1]
                return [int(tempCol/config.scale),int(tempRow/config.scale)]
#name:
#args:
#returns:
#effect:
def getListOfWalls():
    listOfWalls = []
    ID=1
    temp = getMatrix()
    for row in temp:
        for col in row:
            if col[1]=='w':
                listOfWalls.append(col)
    return listOfWalls

#name:
#args:
#returns:
#effect:
def getListOfBoxes():
    listOfBoxes = []
    ID=1
    temp = getMatrix()
    for row in temp:
        for col in row:
            if col[1][0]=='b':
                listOfBoxes.append(col)
    return listOfBoxes

#name:
#args:
#returns:
#effect:
def getListOfEmptyCells():
    listOfEmptyCells = []
    ID=1
    temp = getMatrix()
    for row in temp:
        for col in row:
            if col[1][0]=='e':
                listOfEmptyCells.append(col)
    return listOfEmptyCells

def queryWarehouse(row,col):
    cellType=(((getMatrix()[row])[col])[1])
    config.queriedCells.append([col*config.scale,row*config.scale])
    return cellType



