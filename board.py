# import random
import random
import copy
import os
import time

grid = []
newState = []
# dead or alive bool

def fill():
    for x in range(50):
        grid.append( [None] * 50 )
    for x in range(50):
        newState.append( [None] * 50 )
    chars = ["O", " "]
    
    for x in range(50):
        for i in range(50):
            grid[x][i] =  random.choice(chars)
def printGrid():
    for x in range(len(grid)):
        for i in range(50):
            print(grid[x][i], end=" ")
        print()
def printNewGrid():
    for x in range(len(grid)):
        for i in range(50):
            print(newState[x][i], end=" ")
        print()
def adjacent(a,b):
    totalAlive = 0
    if a == 0 and b == 0:
        if grid[a][b+1] == "O":
            totalAlive += 1
        if grid[a+1][b] == "O":
            totalAlive += 1
        if grid[a+1][b+1] == "O":
            totalAlive += 1
        return totalAlive
    elif a == 0 and b == 49:
        if grid[a][b-1] == "O":
            totalAlive ==1
        if grid[a+1][b-1] == "O":
            totalAlive += 1
        if grid[a+1][b] == "O":
            totalAlive += 1
        return totalAlive
    elif a == 49 and b == 0:
        if grid[a-1][b] == "O":
            totalAlive +=1
        if grid[a-1][b+1] == "O":
            totalAlive += 1
        if grid[a][b+1] == "O":
            totalAlive += 1
        return totalAlive
    elif a == 49 and b == 49:
        if grid[a][b-1] == "O":
            totalAlive += 1
        if grid[a-1][b-1] == "O":
            totalAlive += 1
        if grid[a-1][b] == "O":
            totalAlive += 1
        return totalAlive
    elif a == 0:
        if grid[a][b-1] == "O":
            totalAlive += 1
        if grid[a+1][b-1] == "O":
            totalAlive += 1
        if grid[a+1][b] == "O":
            totalAlive += 1
        if grid[a+1][b+1] == "O":
            totalAlive += 1
        if grid[a][b+1] == "O":
            totalAlive +=1
        return totalAlive
    elif b == 0:
        if grid[a-1][b] == "O":
            totalAlive += 1
        if grid[a-1][b+1] == "O":
            totalAlive += 1
        if grid[a][b+1] == "O":
            totalAlive += 1
        if grid[a+1][b+1] == "O":
            totalAlive += 1
        if grid[a+1][b] == "O":
            totalAlive +=1
        return totalAlive
    elif b == 49:
        if grid[a-1][b] == "O":
            totalAlive += 1
        if grid[a-1][b-1] == "O":
            totalAlive += 1
        if grid[a][b-1] == "O":
            totalAlive += 1
        if grid[a+1][b-1] == "O":
            totalAlive += 1
        if grid[a+1][b] == "O":
            totalAlive +=1
        return totalAlive
    elif a == 49:
        if grid[a][b-1] == "O":
            totalAlive += 1
        if grid[a-1][b-1] == "O":
            totalAlive += 1
        if grid[a-1][b] == "O":
            totalAlive += 1
        if grid[a-1][b+1] == "O":
            totalAlive += 1
        if grid[a][b+1] == "O":
            totalAlive +=1
        return totalAlive
    else:
        if grid[a-1][b-1] == "O":
            totalAlive += 1
        if grid[a-1][b] == "O":
            totalAlive += 1
        if grid[a-1][b+1] == "O":
            totalAlive +=1
        if grid[a][b-1] == "O":
            totalAlive += 1
        if grid[a][b+1] == "O":
            totalAlive +=1
        if grid[a+1][b-1] == "O":
            totalAlive += 1
        if grid[a+1][b] == "O":
            totalAlive +=1
        if grid[a+1][b+1] == "O":
            totalAlive += 1
        return totalAlive
def cellState(i,j):
    if grid[i][j] == "O":
        return True
def conway():
    global grid
    for i in range(50):
        for j in range(50):
            totalAlive = adjacent(i,j)
            isAlive = cellState(i,j)
            if isAlive:
                if totalAlive < 2 or totalAlive > 3:
                    newState[i][j] = " "
                    
                elif totalAlive == 2 or totalAlive == 3:
                    newState[i][j] = "O"
                    
            else:
                if totalAlive == 3:
                    newState[i][j] = "O"
                else:
                    newState[i][j] = " "
    grid = copy.deepcopy(newState)
def screen_clear():
    _ = os.system('cls')
if __name__ == '__main__':
    fill()
    printGrid()
    while True:
        conway()
        screen_clear()
        printNewGrid()
        time.sleep(.5)