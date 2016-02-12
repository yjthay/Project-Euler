#Project Euler Q4
multiplier=0
palindrome=0
j=999
i=999
for j in range(100,999):
    for i in range(100,999):
        multiplier = str(j*i)
        count = len(multiplier)-1
        multiplierlist = [multiplier.split() for multiplier in multiplier]
        #print multiplierlist
        #print multiplier,i,j
        if multiplierlist[0] ==multiplierlist[count]:
            if multiplierlist[1]==multiplierlist[count-1]:
                if multiplierlist[2]==multiplierlist[count-2]:
                    #print j*i
                    if int(i*j)>palindrome:
                        palindrome = i*j
print palindrome