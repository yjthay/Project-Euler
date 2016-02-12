i=2
limit = 9**5*5
while i<limit:
    #print i
    summation=0
    for digit in str(i):
        #print digit
        summation +=int(digit)**5
    if summation ==i:
        print summation
    i+=1
    
    