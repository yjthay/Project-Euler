#The cube, 41063625 (345**3), can be permuted to produce two other cubes: 
#56623104 (384**3) and 66430125 (405**3). In fact, 41063625 is the smallest 
#cube which has exactly three permutations of its digits which are also cube.

#Find the smallest cube for which exactly five permutations of its digits are cube.


count=0
x=1
cubelist=[]
while x<10000:
    num=x**3
    numlist = [int(i) for i in str(num)]
    numlist.sort()
    cubelist.append([numlist,num,x])
    cubelist.sort()
    x+=1

count=1
answer=0
for j in xrange(0,len(cubelist)-1):
    if cubelist[j][0]==cubelist[j+1][0]:
        count+=1
        if count==5:
            print count, cubelist[j][1],cubelist[j][2],j
            answer=j
    else:
        count=1
        
print cubelist[answer-3][1]