# 需求1: 求相邻元素最大值.编写一个程序，求一个正整数数组中每对相邻元素的最大值。
#  例如, 输入: [7 8 9 5 6 7 2 3] 输出: [8, 9, 9, 6, 7, 7, 3]
count=[]
list1=[7,8,9,5,6,7,2,3]
for i in range(0,len(list1)-1):
    if list1[i]<list1[i+1]:
        count.append(list1[1+i])
    else:
        count.append(list1[i])

print(count)

# 需求2: 给定列表original_list其中包含1, 2, 2, 3, 4, 4, 5, 6, 6, 7元素，现在通过编写程序对列表中的数据进行去重
new_list=[]
original_list=[1,2,2,3,4,4,5,6,6,7]
for i in original_list:
    if i in new_list:
        pass
    else:
        new_list.append(i)
print(new_list)
