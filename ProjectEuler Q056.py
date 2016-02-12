def unsplicer(x):
  #x as number
  output=[int(i) for i in str(x)]
  return output


maxsummation=0
for a in xrange(1,101):
    for b in xrange(1,101):
        summation=0
        num = a**b
        numlist=unsplicer(num)
        for dig in numlist:
            summation+=dig
        if summation>maxsummation:
            maxsummation=summation

print maxsummation