import numpy as np
fname = "C:\Users\YJ\OneDrive\Documents\Project Euler\Grids\Project Euler Q18 Grid.txt"
fhand = open(fname)
grid = []
for line in fhand:
    newline = [int(number) for number in line.split(" ")]
    grid.append(newline)
    
pyramid = np.array(grid)
tempgrid =[]
for i in xrange(len(pyramid)-1,-1,-1):
    x=0
    k=0
    sumgrid = [1]*(i+1)
    if i==len(pyramid)-1:
        for j in xrange(0,i+1,1):
            #x and y is determined by j
            #y is the gap for each bite, this is a function of i
            tempgrid.append(pyramid[i][j])
    else:
        for j in xrange(0,i+1,1):
            sumgrid[j]=(max(pyramid[i][j]+tempgrid[k],pyramid[i][j]+tempgrid[k+1]))
            k+=1   
        tempgrid = sumgrid
    print tempgrid
