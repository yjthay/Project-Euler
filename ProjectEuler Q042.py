alphabets = "abcdefghijklmnopqrstuvwxyz"
alphabetdict = dict()
j=1
for i in alphabets:
    alphabetdict[i.upper()]=j
    j+=1
count=0
fname = "C:\Users\YJ\OneDrive\Documents\Project Euler\Grids\p042_words.txt"
fhand = open(fname)
for line in fhand:
    for word in line.split(","):
        wordsum=0
        for alp in word:
            if alp !='"':
                wordsum+=alphabetdict[alp]
        #print word, wordsum, (1+4*1*2*wordsum)**0.5
        y= (1+4*1*2*wordsum)**0.5
        if y.is_integer():
            count +=1
            print word, count
