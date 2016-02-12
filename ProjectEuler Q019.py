#You are given the following information, 
#but you may prefer to do some research for yourself.

#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, 
#but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the 
#twentieth century (1 Jan 1901 to 31 Dec 2000)?

Months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
LeapMonths ={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
Days = {1:0,2:0,3:0,4:0,5:0,6:0,7:0}
LeapYearTigger =0
y=2001
#01/01/1900="Monday"
#minus 2 from 1900 as there are 2 sundays in 1900 that is the start of the month
#minus 1 as 0101/2001 is a sunday
firstdayofmonth = {1:1,2:0,3:0,4:0,5:0,6:0,7:0}
RemainderM=[0]*12
Remainder=3
firstday=1
for i in range(1900, y):
    print i
    if i%4!=0 or (i%4==0 and i%100==0):
        for j in xrange(1,13):
            RemainderM[j-1] = Months[j]%7
            firstday = (sum(RemainderM[:j])+Remainder)%7
            if firstday==0:
                firstday = 7
            firstdayofmonth[firstday]+=1
    elif i%4==0 and i%400==0:
        #century that is a leap year
        for j in xrange(1,13):
            RemainderM[j-1] = LeapMonths[j]%7
            firstday = (sum(RemainderM[:j])+Remainder)%7
            if firstday==0:
                firstday = 7
            firstdayofmonth[firstday]+=1    
    elif i%4 == 0 and i%100!=0:
        for j in xrange(1,13):
            RemainderM[j-1] = LeapMonths[j]%7
            firstday = (sum(RemainderM[:j])+Remainder)%7
            if firstday==0:
                firstday = 7
            firstdayofmonth[firstday]+=1
    Remainder+=sum(RemainderM)
    
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

RemainderM=[0]*12
RemainderY = [0]*(y-x)
Reps=0
for i in range(x, y):
    if i%4!=0 or (i%4==0 and i%100==0):
        for j in xrange(1,13):
            RemainderM[j-1] = Months[j]%7
            Reps = (Months[j]-RemainderM[j-1])/7
            for k in xrange(1,8):
                Days[k]+=Reps
        RemainderY[i-x] = sum(RemainderM)%7
        Reps = (sum(RemainderM)-RemainderY[i-x])/7
        for k in xrange(1,8):
            Days[k]+=Reps
    
    elif i%4==0 and i%400==0:
        #century that is a leap year
        for j in xrange(1,13):
            RemainderM[j-1] = LeapMonths[j]%7
            Reps = (LeapMonths[j]-RemainderM[j-1])/7
            for k in xrange(1,8):
                Days[k]+=Reps
        RemainderY[i-x]= sum(RemainderM)%7
        Reps = (sum(RemainderM)-RemainderY[i-x])/7
        for k in xrange(1,8):
            Days[k]+=Reps
    elif i%4 == 0 and i%100!=0:
        for j in xrange(1,13):
            RemainderM[j-1] = LeapMonths[j]%7
            Reps = (LeapMonths[j]-RemainderM[j-1])/7
            for k in xrange(1,8):
                Days[k]+=Reps
        RemainderY[i-x] = sum(RemainderM)%7
        Reps = (sum(RemainderM)-RemainderY[i-x])/7
        for k in xrange(1,8):
            Days[k]+=Reps
Remainder = (sum(RemainderY))%7
Reps = ((sum(RemainderY))-Remainder)/7
for k in xrange(1,8):
    Days[k]+=Reps
for k in xrange(1,Remainder+1):
    Days[k]+=1
 