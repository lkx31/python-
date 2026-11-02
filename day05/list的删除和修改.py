#del,pop,remove
list1=['红狼','威龙','露娜']
del list1[0]
print(list1)
list1.pop(1)
print(list1)
list1.remove('威龙')
print(list1)
list1.append('威龙')
list1[0]='露娜'
print(list1)
list2=[1,2,3,4,6,7,0]
list2.reverse()
print(list2)
list2.sort()
print(list2)
list2.sort(reverse=True)
print(list2)