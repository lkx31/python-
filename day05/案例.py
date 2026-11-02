# tuple1=((1,2,3),
#         (2,4,6),
#         (2,3,5)
#         )
# count=0
# count1=0
# ans=[]
# for t in tuple1:
#     for j in t:
#         if j not in ans:
#             ans.append(j)
# print(ans)
tuple1=((1,2,3),
        (2,4,6),
        (2,3,5)
        )

ans=[]
for t in tuple1:
    for j in t:
        if j  in ans:
           pass
        else:
            ans.append(j)
print(ans)