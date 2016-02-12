#By starting at the top of the triangle below and moving to 
#adjacent numbers on the row below, the maximum total from top to bottom is 23.

#3
#7 4
#2 4 6
#8 5 9 3

#That is, 3 + 7 + 4 + 9 = 23.

#Find the maximum total from top to bottom of the triangle below:

#75
#95 64
#17 47 82
#18 35 87 10
#20 04 82 47 65
#19 01 23 75 03 34
#88 02 77 73 07 63 67
#99 65 04 28 06 16 70 92
#41 41 26 56 83 40 80 70 33
#41 48 72 33 47 32 37 16 94 29
#53 71 44 65 25 43 91 52 97 51 14
#70 11 33 28 77 73 17 78 39 68 17 57
#91 71 52 38 17 14 91 43 58 50 27 29 48
#63 66 04 68 89 53 67 30 73 16 69 87 40 31
#04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

#NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

import numpy as np
fname = "C:\Users\YJ\OneDrive\Documents\Project Euler\Grids\Project Euler Q18 Test Grid.txt"
fhand = open(fname)
grid = []
for line in fhand:
    newline = [int(number) for number in line.split(" ")]
    grid.append(newline)
    
pyramid = np.array(grid)

  
lst =[]
for i in xrange(len(grid)-1,1,-1):
    for j in xrange(i,-1,-1):
        if i>13:
            if i!=0 or j!=0:
                if j==i:
                    lst.append([i,j,pyramid[i][j]+pyramid[i-1][j-1]])
                else:
                    if j==0:
                        lst.append([i,j,pyramid[i][j]+pyramid[i-1][j]])
                    else:
                        lst.append([i,j,pyramid[i][j]+pyramid[i-1][j-1]])
                        lst.append([i,j,pyramid[i][j]+pyramid[i-1][j]])
        else:
            if i!=0 or j!=0:
                if j==i:
                    lst.append([i,j,pyramid[i-1][j-1]])
                else:
                    if j==0:
                        lst.append([i,j,pyramid[i-1][j]])
                    else:
                        lst.append([i,j,pyramid[i-1][j-1]])
                        lst.append([i,j,pyramid[i-1][j]])

sumgrid = []
holdinggrid = []
k = 2
for i in xrange(len(grid)-1,0,-1):
    if i!=len(grid)-1:
        holdinggrid = sumgrid
    if i< len(grid)-2:
        k3= k3+(2**(k-2))
    sumgrid = [1]*k*2
    k +=1
    k1=0
    k2 =0         
    for j in xrange(0,i+1):
        if i==len(grid)-1:
            holdinggrid.append(pyramid[i][j])
            print holdinggrid
            sumgrid = holdinggrid
            k3=1
        else:
            for rep in xrange(0,k3):     
                sumgrid[k1] = pyramid[i][j]+ holdinggrid[rep]
                k1+=1
                #k2+=1
            #sumgrid[k1] = pyramid[i][j]+ holdinggrid[k2]
            k1+=1
            #print j,sumgrid[k1],pyramid[i][j],holdinggrid[k2]
            #sumgrid[k1] = pyramid[i][j] + holdinggrid[k2+1]
            #print j+1,sumgrid[k1],pyramid[i][j],holdinggrid[k2+1]
            print sumgrid




            
