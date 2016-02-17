import numpy as np
fname = "C:\Users\YJ\OneDrive\Documents\Project Euler\Grids\Project Euler Q067 Grid.txt"
fhand = open(fname)

#grid=[[3],[7,4],[2,4,6],[8,5,9,3]]
grid = []

for line in fhand:
    newline = [int(number) for number in line.split(" ")]
    grid.append(newline)

#grid=[[1],[2,3],[4,5,6],[7,8,9,10],[11,12,13,14,15]]
pyramid = np.array(grid)

answerlist=[]

for rownum in xrange(len(pyramid)-1,0,-1):
    currentrow=pyramid[rownum]
    previousrow=pyramid[rownum-1]
    for colnum in xrange(len(currentrow)-1):
        if currentrow[colnum]>currentrow[colnum+1]:
            answerlist.append(previousrow[colnum]+currentrow[colnum])
        else:
            answerlist.append(previousrow[colnum]+currentrow[colnum+1])
    pyramid[rownum-1]=answerlist
    print answerlist
    answerlist=[]

print pyramid[0][0]