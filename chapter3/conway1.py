import random, time, sys,copy

width = 60
height = 20
#generating a random cell
nextcells = []
for x in range(width):
    column = []
    for y in range(height):
        if random.randint(0, 1) == 0:
            column.append("#")
        else:
            column.append(" ")
    nextcells.append(column)
while True:
    print('\n'*5)
    currentCells=copy.deepcopy(nextcells)
    for y in range(height):
        for x in range(width):
            print(currentCells[x][y], end='')
        print()
    for x in range(width):
        for y in range(height):
            leftCoord=(x-1)%width
            rightCoord=(x+1)%width
            aboveCoord=(y-1)%height
            belowCoord=(y+1)%height
    
            numNeighbors=0
            if currentCells[leftCoord][aboveCoord]=='#':
                numNeighbors+=1 #top-left
            if currentCells[x][aboveCoord]=='#':
                numNeighbors+=1 #top
            if currentCells[rightCoord][aboveCoord]=='#':
                numNeighbors+=1 #top-right
            if currentCells[leftCoord][y]=='#':
                numNeighbors+=1 #left
            if currentCells[rightCoord][y]=='#':
                numNeighbors+=1 #right
            if currentCells[leftCoord][belowCoord]=='#':
                numNeighbors+=1 #bottom-left
            if currentCells[rightCoord][belowCoord]=='#':
                numNeighbors+=1 #bottom-right
            if currentCells[x][belowCoord]=='#':
                numNeighbors+=1 #bottom
            if currentCells[x][y]=='#' and (numNeighbors==2 or numNeighbors==3):
                nextcells[x][y]='#'
            elif currentCells[x][y]==' ' and numNeighbors==3:
                nextcells[x][y]=='#'
            else:
                nextcells[x][y]=' '
    time.sleep(1)
    
