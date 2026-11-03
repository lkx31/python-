# 	编写一个程序来统计缺失的数字并返回它们的总和。缺失的数字是指给定列表中两个极端（最大和最小数字）之间没有出现的数字。
# 例如，在集合{2, 5, 3, 7, 5, 7}中，两个极端（即2和7）之间缺失的数字是4和6。
set2 = {2, 5, 3, 7, 5, 7}
set1 = set()
set_number = max(set2)
set_number1 = min(set2)
for i in range(set_number1, set_number):
    if i not in set2:
        set1.add(i)
print(set1)
