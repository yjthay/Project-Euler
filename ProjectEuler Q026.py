# coding: utf-8
def remainder(num,den):
  num=float(num)
  den=float(den)
  if num==0:
    next
  else:
    while num<den:
      num*=10
      #print num
  divisor=int(num/den)
  remainder=num-(den*divisor)
  #print remainder, divisor, num,den
  return remainder
  
sortedlist=[]

for i in xrange (2,1001):
  den=i
  numlist=[]
  rem=remainder(1,den)
  count=0
  #print i
  while rem not in numlist and rem!=0:
    #print rem,numlist
    numlist.append(rem)
    count+=1
    rem=remainder(rem,den)
    #print den, num, count
  sortedlist.append([count,den])
  #print den,count ,numlist

sortedlist.sort()

print sortedlist[len(sortedlist)-1]