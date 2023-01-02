"""
Created on Sat Apr 25 08:50:31 2020

@author: Deepayan Banik
Wiki link: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, 
each of which is in one of two possible states, alive or dead, (or populated and unpopulated, 
respectively). Every cell interacts with its eight neighbours, which are the cells that are 
horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:
1. Any live cell with two or three live neighbors survives.
2. Any dead cell with three live neighbors becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.
"""

# The Game of Life
import numpy as np
import matplotlib.pyplot as plt

numgen = 1000 # number of generations

""" Initial conditions for a board having a fixed number of randomly distributed live cells 
Please comment this if you want to try some specific examples """
#def make_board(shape, ones):
#    size = np.product(shape)
#    board = np.zeros(size, dtype=np.int)
#    i = np.random.choice(np.arange(size), ones)
#    board[i] = 1
#    return board.reshape(shape)
#a = make_board((30,20), 60) # board dimensions in () and number of live cells
#endsx = [0,len(a)-1]
#endsy = [0,len(a[0])-1]
#for i in endsx:
#    for j in range (0,len(a[0])):
#        a[i][j] = 0
#for j in endsy:
#    for i in range (0,len(a)):
#        a[i][j] = 0

""" Some initial conditions for verification (uncomment to use, also comment from line 12 till before this) """
a = np.zeros((100,50))

#a[4][4]=1 # Blinker
#a[5][4]=1 # Blinker
#a[6][4]=1 # Blinker
#a[5][5]=1 # Toad (include blinker)
#a[6][5]=1 # Toad (include blinker)
#a[7][5]=1 # Toad (include blinker)
#a[5][6]=1 # Glider/Spaceship (include blinker, not toad)
#a[6][5]=1 # Spaceship (include blinker, not toad)

""" Gosper glider gun initial conditions, generates gliders at regular intervals """
x=40
a[x][14]=1
a[x][15]=1

a[x+1][13]=1
a[x+1][17]=1

a[x+2][12]=1
a[x+2][18]=1
a[x+2][26]=1

a[x+3][2]=1
a[x+3][3]=1
a[x+3][12]=1
a[x+3][16]=1
a[x+3][18]=1
a[x+3][19]=1
a[x+3][24]=1
a[x+3][26]=1

a[x+4][2]=1
a[x+4][3]=1
a[x+4][12]=1
a[x+4][18]=1
a[x+4][22]=1
a[x+4][23]=1

a[x+5][13]=1
a[x+5][17]=1
a[x+5][22]=1
a[x+5][23]=1
a[x+5][36]=1
a[x+5][37]=1

a[x+6][14]=1
a[x+6][15]=1
a[x+6][22]=1
a[x+6][23]=1
a[x+6][36]=1
a[x+6][37]=1

a[x+7][24]=1
a[x+7][26]=1

a[x+8][26]=1

""" Some variables for temporary storage of the board """
b = np.zeros((len(a),len(a[0])))
c = np.zeros((len(a)-2,len(a[0])-2))

check = [-1,0,1]
fig = plt.figure(figsize=(3,5))

for step in range (numgen): # number of generations inside loop
    plt.cla()
    t = plt.imshow(c)
    plt.savefig("{}.png".format(step))
    # The main algorithm of the game of life is really this small and simple
    for i in range (1,len(a)-1):
        for j in range (1,len(a[0])-1):
            count = 0
            for k in check:
                for l in check:
                    if ((a[i+k][j+l] == 1)):
                        count = count + 1
            if (a[i][j] == 1):
                count = count - 1
            if (count < 2 or count > 3):
                b[i][j] = 0
            elif (count == 3):
                b[i][j] = 1
            else:
                b[i][j] = a[i][j]
    
    # Periodic boundary conditions (PBCs) for edges
    for j in range (1,len(a[0])-1):
        b[0][j] = b[len(a)-2][j]
        b[len(a)-1][j] = b[1][j]
    for i in range (1,len(a)-1):
        b[i][0] = b[i][len(a[0])-2]
        b[i][len(a[0])-1] = b[i][1]
        
    # PBCs for corners
    b[0][0] = b[len(a)-2][len(a[0])-2]
    b[0][len(a[0])-1] = b[len(a)-2][1]
    b[len(a)-1][len(a[0])-1] = b[1][1] 
    b[len(a)-1][0] = b[1][len(a[0])-2]
    
    # Trimming ghost cells
    for i in range (1,len(a)-1):
        for j in range (1,len(a[0])-1):
            c[i-1][j-1] = b[i][j]
            
    # b is basically the temporary variable
    a = b
    b = np.zeros((len(a),len(a[0])))
    plt.pause(0.01)

