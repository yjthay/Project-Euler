#The cube, 41063625 (345**3), can be permuted to produce two other cubes: 
#56623104 (384**3) and 66430125 (405**3). In fact, 41063625 is the smallest 
#cube which has exactly three permutations of its digits which are also cube.

#Find the smallest cube for which exactly five permutations of its digits are cube.

import itertools

from itertools import permutations
def next_permutation(seq, pred=cmp):
    """Like C++ std::next_permutation() but implemented as
    generator. Yields copies of seq."""

    def reverse(seq, start, end):
        # seq = seq[:start] + reversed(seq[start:end]) + \
        #       seq[end:]
        end -= 1
        if end <= start:
            return
        while True:
            seq[start], seq[end] = seq[end], seq[start]
            if start == end or start+1 == end:
                return
            start += 1
            end -= 1
    
    if not seq:
        raise StopIteration

    try:
        seq[0]
    except TypeError:
        raise TypeError("seq must allow random access.")

    first = 0
    last = len(seq)
    seq = seq[:]

    # Yield input sequence as the STL version is often
    # used inside do {} while.
    yield seq
    
    if last == 1:
        raise StopIteration

    while True:
        next = last - 1

        while True:
            # Step 1.
            next1 = next
            next -= 1
            
            if pred(seq[next], seq[next1]) < 0:
                # Step 2.
                mid = last - 1
                while not (pred(seq[next], seq[mid]) < 0):
                    mid -= 1
                seq[next], seq[mid] = seq[mid], seq[next]
                
                # Step 3.
                reverse(seq, next1, last)

                # Change to yield references to get rid of
                # (at worst) |seq|! copy operations.
                yield seq[:]
                break
            if next == first:
                raise StopIteration
    raise StopIteration
    

x=1
mynumber=0
answerlist=[]
count=0
while count!=3:
    mynumber = x**3
    mylist=[int(i) for i in str(mynumber)]   
    count=0
    answerlist=[]
    for i in next_permutation(mylist):
        newnumber=""
        if i[0]<mylist[0]:
            break
        for digit in i:
            newnumber+=str(digit)
        #print newnumber
        newnumber=int(newnumber)
        if newnumber<mynumber or newnumber in answerlist:
            continue
        else:
            cuberoot = newnumber**(1./3)
            if round(cuberoot,10).is_integer():
                if newnumber not in answerlist:
                    answerlist.append(newnumber)
                    count+=1
                    #print x, newnumber,mynumber,count
    #print x
    x+=1
    


    