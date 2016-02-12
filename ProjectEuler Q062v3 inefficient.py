#The cube, 41063625 (345**3), can be permuted to produce two other cubes: 
#56623104 (384**3) and 66430125 (405**3). In fact, 41063625 is the smallest 
#cube which has exactly three permutations of its digits which are also cube.

#Find the smallest cube for which exactly five permutations of its digits are cube.

def next_perm(numblist):
    #try:
    i=len(numblist)-1
    while numblist[i]<=numblist[i-1]:
        i-=1
    
    pivot=i-1

    i = len(numblist)-1
    while numblist[i]<=numblist[pivot]:
        i-=1
    numblist[i],numblist[pivot]=numblist[pivot],numblist[i]
        
    numblist[pivot+1:]=numblist[len(numblist):pivot:-1]
    #print numblist
    return numblist
    

x=201
mynumber=0
count=0
while count!=5:
    mynumber = x**3
    mylist=[int(i) for i in str(mynumber)]   
    count=0
    while mylist!=[]:
        newnumber=""
        for digit in mylist:
            newnumber+=str(digit)
        #print newnumber
        newnumber=int(newnumber)
        cuberoot = newnumber**(1./3)
        if round(cuberoot,10).is_integer():
            count+=1
            print mylist
        next_perm(mylist)
    print x
    x+=1


    
    
        