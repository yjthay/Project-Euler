#x**2 - D * y**2 ==1

for D in xrange(2,1001):
    if round(D**(0.5),10).is_integer():
        continue
    else:
        x = D-1
        y = int(x**(0.5))
        if x**2 - D*y**2==1:
            print x,D,y 
        while x**2 - D*y**2!=1:
            if y<x:
                y+=1
            else:
                x+=1
                y=int(x**(0.5))
            if x**2 - D*y**2==1:
                print x,D,y
            
