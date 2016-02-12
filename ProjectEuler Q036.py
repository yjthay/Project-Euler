def binary2(x):
    import math
    binarylist =[]
    while x!=0:
        i=floor(log2(x))
        x = x-2**i
        binarylist.append(i)
    length = binarylist[0]+1
    output = [0]*length
    #print output,length,binarylist
    for i in binarylist:
        output[int(i)]=1
    return output[::-1]
    
summation=0
for i in xrange(1,1000000):
    binary10 = [int(j) for j in str(i)]
    j=0
    while j<=len(binary2(i))/2 and binary2(i)[0]!=0:
        binary2trigger=0
        if binary2(i)[j]==binary2(i)[-j-1]:
            next
        else:
            binary2trigger=1
            break
        j+=1
    j=0
    while j<=len(binary10)/2:
        binary10trigger=0
        if binary10[j]==binary10[-j-1]:
            next
        else:
            binary10trigger=1
            break
        j+=1
    if binary10trigger==binary2trigger==0:
        print i
        summation+=i
        