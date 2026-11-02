numstr = '0123456789'
# 1、从2到5开始切片，步长为1
test1=numstr[2:5]
print(f"截取的片段是{test1}")
# 2、只有结尾的字符串切片：代表从索引为0开始，
# 截取到索引为5的位置（不包含索引为5的数据）
print(numstr[:5])
# 3、只有开头的字符串切片：代表从起始位置开始(例如 1)，已知截取到字符串的结尾
print(numstr[1::])
# 4、获取或拷贝整个字符串
print(numstr[::])
# 5、调整步阶：类似求偶数
print(numstr[::2])
# 6、把步阶设置为负整数：类似字符串翻转
print(numstr[::-1])
# 7、起始位置与结束位置都是负数
print(numstr[-1:-5])
print(numstr[-5:-1])
print(numstr[-5:-1:-1])
print(numstr[-1:-5:-1])
