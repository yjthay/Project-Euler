#Powerful digit counts
Problem 63
#The 5-digit number, 16807=7**5, is also a fifth power. 
#Similarly, the 9-digit number, 134217728=8**9, is a ninth power.

#How many n-digit positive integers exist which are also an nth power?

mynumber=0

count=0
for i in xrange(1,10):
    for j in xrange(1,10000):
        mynumber=i**j
        mynumlist=[x for x in str(mynumber)]
        length = len(mynumlist)
        if j==length:
            print mynumber,i,j
            count+=1