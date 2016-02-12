fpath = "C:\Users\YJ\OneDrive\Documents\Project Euler\Grids\Project Euler Q59 Cipher.txt"
fhand = open(fpath)
# encryption key consists of three lower case characters
loweralphabets = "abcdefghijklmnopqrstuvwxyz "
upperalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerasciilist =[]
upperasciilist=[]
asciilist=[]


for alphabet in loweralphabets:
    lowerasciilist.append(ord(alphabet))


def crypter(x,y):
    return x^y

def listfreq(mylist1):
    mylist1freq=dict()
    for i in mylist1:
        if i not in mylist1freq.keys():
            mylist1freq[i]=1
        else:
            mylist1freq[i]+=1
    return mylist1freq

def maxvaluekey(listfreq):
    i  = listfreq.values()
    j = listfreq.keys()
    #print i ,j
    return j[i.index(max(i))]

def decrypt(inputx,outputy):
    found=0
    for num in lowerasciilist:
        if chr(crypter(num,inputx))==chr(outputy):
            return num
            
charactercount=0
mylist1=[]
mylist2=[]
mylist3=[]

asciilist = [i for i in xrange(0,128)]

charactercount=0
mylist=[]
fpath = "C:\Users\YJ\OneDrive\Documents\Project Euler\Grids\Project Euler Q59 Cipher.txt"
fhand = open(fpath)
for line in fhand:
    for character in line.split(","):
        charactercount+=1
        character=int(character)
        #print wordcount,crypter(myword,lowerasciilist[key]),key
        if charactercount in [i for i in xrange(1,1202,3)]:
            mylist1.append(character)
            print charactercount
        if charactercount in [i for i in xrange(2,1202,3)]:
            mylist2.append(character)
            print charactercount
        if charactercount in [i for i in xrange(3,1202,3)]:
            mylist3.append(character)
            print charactercount
        #print mycharacter

listfreq1=listfreq(mylist1)
listfreq2=listfreq(mylist2)
listfreq3=listfreq(mylist3)

masterlist=[listfreq1,listfreq2,listfreq3]
key=[]
for i in xrange(3):
    key.append(decrypt(maxvaluekey(masterlist[i]),ord(" ")))

#key=[ord("g"),ord("o"),ord("d")]
i=0
paragraph=[]
summation=0
while i<len(mylist2):
    paragraph.append(chr(crypter(mylist1[i],key[0])))
    paragraph.append(chr(crypter(mylist2[i],key[1])))
    paragraph.append(chr(crypter(mylist3[i],key[2])))

    summation+=crypter(mylist1[i],key[0])
    summation+=crypter(mylist2[i],key[1])
    summation+=crypter(mylist3[i],key[2])
    i+=1

summation+=crypter(mylist1[400],key[0])
paragraph.append(chr(crypter(mylist1[400],key[0])))
"".join(paragraph)

        



#for i,j in mylist:
#    for 
