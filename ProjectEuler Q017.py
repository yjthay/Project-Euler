#If the numbers 1 to 5 are written out in words: one, two, three, four, five,
#then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were written 
#out in words, how many letters would be used?


#NOTE: Do not count spaces or hyphens. For example, 342 
#(three hundred and forty-two) contains 23 letters and 115 
#(one hundred and fifteen) contains 20 letters. The use of "and" 
#when writing out numbers is in compliance with British usage.
import math

digits = dict()
digits = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
Mscale = {1:"ten",2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
Lscale = {100:"hundred",1000:"thousand"}
filler = "and"

x=999
count=len(Lscale[1000])+len(digits[1])
for i in xrange(1,x+1):
    if i<1000:
        if i<100:
            if i<20:
                count += len(digits[i])
            else:
                count +=len(Mscale[math.floor(i/10)])
                i=i-(math.floor(i/10)*10)
                if i!=0:
                    count += len(digits[i])
        else:
            count += len(digits[math.floor(i/100)])+len(Lscale[100])
            i=i-(math.floor(i/100)*100)
            if i!=0:    
                count+=len(filler)
                if i<20:
                    count += len(digits[i])
                else:
                    count +=len(Mscale[math.floor(i/10)])
                    i=i-(math.floor(i/10)*10)
                    if i!=0:
                        count += len(digits[i])
        