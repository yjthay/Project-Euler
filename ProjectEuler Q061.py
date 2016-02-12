#The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

#The set is cyclic, in that the last two digits of each number is 
#the first two digits of the next number (including the last number with the first).
#Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), 
#and pentagonal (P5,44=2882), is represented by a different number in the set.
#This is the only set of 4-digit numbers with this property.


#Find the sum of the only ordered set of six cyclic 4-digit numbers for which each 
#polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, 
#is represented by a different number in the set.

def tri(i):
    return mynumber-(i*(i+1)/2)

def squ(i):
    return mynumber -(i*i)

def pen(i):
    return mynumber-(i*(3*i-1)/2)

def hex(i):
    return mynumber-(i*(2*i-1))
    
def hep(i):
    return mynumber - (i*(5*i-3)/2)

def oct(i):
    return mynumber - (i*(3*i-2))

mynumber=0
tri=[0,0.50,0.50]
squ=[1,0]
pen=[1.5,-0.5]
hexa=[2,-1]
hep=[2.5,-1.5]
octa=[3,-2]
#
import scipy
import numpy
from scipy.optimize import fsolve
coefficientlist = [tri,squ,pen,hexa,hep,octa]
#functiontype = [tri,squ,pen]
answerlist=[]
for k in xrange(10,100):
    firsttwo=k
    for i in xrange(len(coefficientlist)):
        for j in xrange(1,100):
            if j<10:
                mynumber = int(str(firsttwo)+"0"+str(j))
            else:
                mynumber = int(str(firsttwo)+str(j))
            coefficientlist[i].append(-mynumber)
            #print mynumber,coefficientlist[i],i,k,j
            if round(numpy.roots(coefficientlist[i])[0],3).is_integer():
                #print numpy.roots(coefficientlist[i])
                answerlist.append([i,mynumber])
            coefficientlist[i].remove(-mynumber)

print len(answerlist)

answerlist.sort(reverse=True)
#print answerlist

def lasttwo(i):
    mynumber=[int(x) for x in str(i)]
    lasttwo=int(str(mynumber[2])+str(mynumber[3]))
    return lasttwo

def firsttwo(i):
    mynumber=[int(x) for x in str(i)]
    firsttwo=int(str(mynumber[0])+str(mynumber[1]))
    return firsttwo


masterlist=[]
x=0
circle=0
count=0
front=answerlist[x]   
degreelist=[front[0]]   
sortedlist=[front[1]]      
while circle==0:
    for i in answerlist:
        back=i
        #print front,back,x
        if lasttwo(front[1])==firsttwo(back[1]) and back[0] not in degreelist and back[1] not in sortedlist:
            sortedlist.append(back[1])
            degreelist.append(back[0])
            #print sortedlist,front,back
            front=back
            break
    else:
        #if len(sortedlist)==len(functiontype):
        #    count+=1
        #    print sortedlist,degreelist,count
        x+=1
        front=answerlist[x]
        sortedlist=[front[1]]
        degreelist=[front[0]]
    if len(sortedlist)==len(coefficientlist):
        count+=1
        print sortedlist,degreelist,count
    if firsttwo(sortedlist[0])==lasttwo(sortedlist[len(sortedlist)-1]) and len(sortedlist)==len(coefficientlist):
        circle=1
        print sortedlist,degreelist,count
print sortedlist
    