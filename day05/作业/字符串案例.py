# 案例1 给定一个图片的名称为"avatar.png"，代码实现获取这个图片的名称(avatar)以及这个图片的后缀(.png)。
#
# * 分析：
#
#   * ① 建议先获取点号的位置（目前还未学习，只能一个一个数）
#   * ② 从开头切片到点号位置，得到的就是文件的名称
#   * ③ 从点号开始切片，一直到文件的结尾，则得到的就是文件的后缀
name="avatar.png"

print(name.index("."))
new_name=name[6::]
print(new_name)

# 案例2:

# 将字符串向右旋转n位，例如“abcdef”向右旋转2位得到“efabcd”
#
# “abcdef” ==> "efabcd"
name1="abcdef"
#首先是不是要获取er和abcd的切片然后在进行字符串的拼接
new_name1=name1[0:4]
new_name2=name1[4:6]
ans=new_name2+new_name1
print(ans)