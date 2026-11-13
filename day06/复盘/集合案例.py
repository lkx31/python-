set1={2,5,3,7,5,7}
count=0
Max_num=max(set1)
Min_num=min(set1)
for i in range(Min_num,Max_num):
    if i not in set1:
        print(f"缺失的数字是{i}")
        count+=i

print(count)
