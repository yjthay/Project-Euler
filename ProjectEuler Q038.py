n=10
mylist=[i for i in xrange(1,n)]
number=9
n=5
concpdt=[]
maxholderconcpdt=[]

number=1
while number<1000000:
    concpdt=[]
    for i in xrange(1,10):
        concpdt+=[int(j) for j in str(number*i)]
        #holderconcpdt = [j for j in concpdt]
        if len(concpdt)!=9:
            next
        else:
            holderconcpdt = [j for j in concpdt]
            #print holderconcpdt, number,i
            concpdt.sort()
            duplicate=0
            #aprint holderconcpdt, number,i, concpdt
            for j in xrange(len(concpdt)):
                if j+1<len(concpdt):#print concpdt[i],concpdt[i+1]
                    if concpdt[j]==concpdt[j+1]:
                        #print concpdt,concpdt[i],concpdt[i+1]
                        duplicate=1
                        next
            #print duplicate,holderconcpdt, number,i, concpdt
            if duplicate==0:
                if holderconcpdt>maxholderconcpdt:
                    maxholderconcpdt=holderconcpdt
                    print maxholderconcpdt
    number+=1