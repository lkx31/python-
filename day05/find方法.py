# 案例：使用input方法输入任意一个文件名称(名称+后缀 录入 a.txt)，求点号的索引下标
# 1- 键盘录入
user_file_name = input('请输入一个文件名称:')

# 2- 判断 用户输入的内容中  . 位置
index = user_file_name.find('.')
print(f"您输入的文件名:{user_file_name},对应的点出现的索引的位置:{index}")