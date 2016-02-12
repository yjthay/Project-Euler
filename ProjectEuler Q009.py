#A Pythagorean triplet is a set of three natural 
#numbers, a < b < c, for which,

#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for 
#which a + b + c = 1000.
#Find the product abc.

for a in xrange(1,1000):
    for b in xrange(a,1000):
        for c in xrange(b,1000):
            if c**2 == a**2+b**2:
                if c+b+a==1000:
                    print a*b*c
                    print a,b,c
                #else: break
            #else: break
            