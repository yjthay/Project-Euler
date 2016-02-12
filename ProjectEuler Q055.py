def palindrome(x):
  #x as number
  import math
  xlist=[int(i) for i in str(x)]
  length=len(xlist)
  palindrometrigger=1
  #print length,math.floor(length/2)
  for i in xrange(int(math.floor(length/2))):
    #print xlist[i], xlist[-i-1]
    if xlist[i]!=xlist[-i-1]:
      palindrometrigger=0
      return palindrometrigger
  return palindrometrigger

def unsplicer(x):
  #x as number
  output=[int(i) for i in str(x)]
  return output

def splicer(xlist):
  #x as list
  return int("".join(str(n) for n in xlist) )

count=0
limit=50
mylist=[]
for i in xrange(1,10000):
    #print i
    main=i
    num=i
    LychrelTrigger=1
    reps=0
    while reps<limit+1:
        print num, reps
        if palindrome(num)==1:
            if reps!=0:
                LychrelTrigger=0
                break
            else:
                x=unsplicer(num)
                x1=[i for i in x]
                x1.reverse()
                num=splicer(x1)+splicer(x)
        else:
            x=unsplicer(num)
            x1=[i for i in x]
            x1.reverse()
            num=splicer(x1)+splicer(x)
        reps+=1
    if LychrelTrigger==1:
        count+=1
        mylist.append(main)
        #print i, reps, count
    
print 'my answer:'+str(count)
        
    
    
  
