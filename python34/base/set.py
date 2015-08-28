__author__ = 'lulizhou'
basket={'apple','bannner','apple','bannner'} #set：无序，不重复的集合
basket2={'Tom','Jack','apple'}
print(basket|basket2)   #二个集合包含的所有元素
print(basket2-basket)   #第一个集合包含的元素
print(basket2&basket)   #二个集合的共同部分
print(basket2^basket)   #二个集合不共同部分
print(basket)

a=[1,23,4,5,6,7,8,9,0,10] #list:表
a.append(2)
print(a)

#队列任务 头出尾进
from collections import deque
queue=deque(['Eric','John','Mick'])
queue.append('Tom')
queue.append('Graham')
print (queue.popleft())
print (queue.popleft())
print (queue.popleft())
print(queue)