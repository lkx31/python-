# 需求描述】** 期末考试结束后，班主任需要统计学生的成绩。
# 请编写程序，通过键盘录入**学生姓名**，以及**语文**、
# **数学**、**英语**三门课程的成绩（成绩可能包含小数，如89.5）。
# 程序需要计算该学生的**总分**和**平均分**，并按照指定格式打印成绩单，
# **平均分需保留一位小数**。
name=input('请输入学生姓名')
yuwen=float(input('请输入语文成绩'))
shuxue=float(input('请输入数学成绩'))
english=float(input('请输入英语成绩'))
totall=yuwen+shuxue+english
peace=totall/3
print(f'你的语文成绩是{yuwen}')
print(f'你的数学成绩是{shuxue}')
print(f'你的英语成绩是{english}')
print(f'你的总分成绩是{totall}')
print(f'你的平均分成绩是{peace:.1f}')
