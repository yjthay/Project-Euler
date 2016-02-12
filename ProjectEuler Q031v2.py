summation=200
for i in xrange(len(factors)):
    summation=200
    summation-factors[i][0]
    
def combi(n,x):
    import math
    return math.factorial(n)/(math.factorial(x)*math.factorial(n-x))

coins = [0,1,2,5,10,20,50,100,200]
count=0
for i in xrange(0,len(coins)):
    if coins[i]==200:
        count+=1
        break
    else:
        if coins[i]%coins[i-1]==0:
            reps = coins[i]/coins[i-1]
            
        else:
            remainder = coins[i]%coins[i-1]
            reps = (coins[i]-remainder)%coins[i-1]
            reps1 = remainder%coins[i-2]
            