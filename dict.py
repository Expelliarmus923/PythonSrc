#-*-coding:utf-8-*-
__author__ = 'lulizhou'
d = {
    'Adam':95,
    'Lisa':85,
    'Bart':59
}
print len(d)
if 'Adam' in d:
    print d['Adam']
d['Plu']=100
print d
for key in d:
    print  key + ":",d[key]
print d.get('Adam')
def square_of_sum(L):
    sum=0
    for num in L:
        sum+=num*num
    return  sum

print square_of_sum([1, 2, 3, 4, 5])
print square_of_sum([-5, 0, 5, 15, 25])