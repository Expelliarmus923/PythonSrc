#-*-coding:utf-8-*-
L = range(1,101)
#for x in L:
#    if x%7==0:
#        print x
#N =['Adam','Lisa','Bart','Paul']
#for t in enumerate(N):
#    index = t[0]
#    name = t[1]
#    print index,'-',name
#for t in zip(range(1,len(L)+1),N):
#    index = t[0]
#    name = t[1]
#    print index,'-',name
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
for k, v in d.iteritems():
    sum = sum + v
    print k,':',v
print 'average', ':', sum / len(d)
print[x*(x+1) for x in range(1,100,2)]
