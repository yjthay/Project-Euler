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

def hexa(i):
    return mynumber-(i*((2*i)-1))
    
def hep(i):
    return mynumber - (i*(5*i-3)/2)

def octo(i):
    return mynumber - (i*(3*i-2))


import scipy
from scipy.optimize import fsolve
functiontype = [tri,squ,pen,hexa,hep,octo]
#functiontype = [tri,squ,pen]
answerlist=[]
for k in xrange(10,100):
    firsttwo=k
    for i in xrange(len(functiontype)):
        for j in xrange(10,100):
            mynumber = int(str(firsttwo)+str(j))
            #print mynumber
            if fsolve(functiontype[i],5)[0].is_integer():
                answerlist.append([i,mynumber])
                #print answerlist

answerlist.sort()
#print answerlist

def lasttwo(i):
    mynumber=[int(x) for x in str(i)]
    lasttwo=int(str(mynumber[2])+str(mynumber[3]))
    return lasttwo

def firsttwo(i):
    mynumber=[int(x) for x in str(i)]
    firsttwo=int(str(mynumber[0])+str(mynumber[1]))
    return firsttwo
    
#**********************************************************************************

#answerlist=[[0,1234],[0,1256],[0,1278],[1,5678],[1,7891],[2,9112],[2,7812]]

masterlist=[]
x=0
circle=0
count=0
front=answerlist[x]   
degreelist=[front[0]]   
sortedlist=[front[1]]      
origfront=answerlist[x] 

for i in xrange(len(answerlist)-1):
    back=answerlist[i]
    for j in xrange(len(answerlist)):
        backnext=answerlist[j]
        if firsttwo(back[1])==firsttwo(backnext[1]):
            print back, backnext
            count+=1
            pass
        
while circle==0:
    for i in answerlist:
        back=i
        #print front,back,x
        if lasttwo(front[1])==firsttwo(back[1]) and back[0] not in degreelist:
            sortedlist.append(back[1])
            degreelist.append(back[0])
            front=back
            #break
            print sortedlist
        break
    else:
        print front, sortedlist
        x+=1
        front=answerlist[x]
        sortedlist=[front[1]]
        degreelist=[front[0]]
        #break
    if len(sortedlist)==len(functiontype):
        count+=1
        print sortedlist,degreelist,count
    if firsttwo(sortedlist[0])==lasttwo(sortedlist[len(sortedlist)-1]) and len(sortedlist)==len(functiontype):
        circle=1
print sortedlist
    
