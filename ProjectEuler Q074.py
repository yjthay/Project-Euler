# coding: utf-8
import math
def facmod(x):
  import math
  total=0
  for i in str(x):
    total+=math.factorial(int(i))
  return total

max=1000001
answer=0

info=dict()
for x in xrange(69,max):
  master=[x]
  new=x
  count=0
  while len(master)<60:
    new=facmod(new)
    if new in master:
      info[x]=len(master)
      break
    elif new in info.keys():
      count=info[new]
      break
    else:
      master.append(new)
  if new in info.keys():
    count=info[new]+len(master)
  else:
    count=len(master)
  if count>=60:
    answer+=1
    print answer,x
  