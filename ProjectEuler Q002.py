
        
#Euler q2
fib=0
fib1 = 1
fib2 = 2
sumfib=2

while fib <4e6:
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
    print fib
    if (fib%2 ==0): sumfib +=fib