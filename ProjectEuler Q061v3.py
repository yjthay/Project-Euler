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

def last(i):
    mynumber=[int(x) for x in str(i)]
    lasttwo=int(str(mynumber[2])+str(mynumber[3]))
    return lasttwo

def first(i):
    mynumber=[int(x) for x in str(i)]
    firsttwo=int(str(mynumber[0])+str(mynumber[1]))
    return firsttwo

import scipy
from scipy.optimize import fsolve
mynumber=0

#functiontype = [tri,squ,pen,hex,hep,oct]
functiontype = [tri,pen,squ]
answerlist=[]
while len(answerlist)!=3:
    for i in xrange(10,100):
        firsttwo=i
        answerlist=[]
        for myfunct in functiontype:
            for j in xrange(10,100):
                lasttwo=j
                mynumber = int(str(firsttwo)+str(lasttwo))
                #print fsolve(tri,1),mynumber
                if fsolve(myfunct,1)[0].is_integer():
                    answerlist.append(mynumber)
                    firsttwo=lasttwo
                    #print answerlist
                    #break
        if len(answerlist)==3:
            print answerlist
            if first(answerlist[0])==last(answerlist[2]):
                print answerlist
                break
            #break
