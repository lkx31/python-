# 场景一：共吃5个苹果，吃完第一个，吃第二个…，如果吃的过程中，吃完第三个吃饱了
# ，则不需要再吃第4个和第5个苹果，
# 即是吃苹果的动作停止，这里就是break控制循环流程，即终止此循环。
#首先有重复动作，用循环目前只学习了while循环那就while来写
count=1#用一个变量承接苹果数量
#因为吃到第三个就饱了那么就是要终止循环关键字break
while count<6:
    print(f"我开始吃第{count}个苹果")
    if count==3:
        print("我吃饱了")
        break
    print(f"我吃完了第{count}个苹果")
    count += 1



# # 场景二：如果吃的过程中，吃到第三个吃出一个大虫子...,是不是这个苹果就不吃了，
# 开始吃第四个苹果，这里就是continue控制循环流程，
# 即退出当前一次循环继而执行下一次循环代码。
# count1=1
# while count1<6:
#     print(f"我开始吃第{count1}个苹果")
#     if count1==3:
#         count1+=1
#         print("吃到大虫子了")
#         continue
#     print(f"我吃完第{count1}个苹果")
#     count1+=1

