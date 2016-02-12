def tri(x):
    z = x*(x+1)/2
    return z

def checkpent(x):
    z = ((24*x+1)**0.5+1)/6
    return z
    
def checkhex(x):
    z = (1+(8*x+1)**0.5)/4
    return z
 
i=286
#285 is the first one which satisfies the conditions
while True:
    trinum= tri(i)
    pent = checkpent(trinum)
    hexa = checkhex(trinum)
    if pent.is_integer():
        if hexa.is_integer():
            print trinum
            break
    i+=1
    if i%1000000==0:
        print i
        
