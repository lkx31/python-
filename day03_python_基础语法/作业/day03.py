"""**【需求描述】** BMI（身体质量指数）是国际常用的衡量人体胖瘦程度的标准。
请编写程序，通过键盘录入用户的**姓名**、**身高（单位：米，如1.75）**、
**体重（单位：千克，如70.0）**。 程序需要计算该用户的BMI指数（计算公式：
`BMI = 体重 / (身高 * 身高)`），并按照指定格式输出结果，
**BMI指数需保留两位小数**。"""
name1=input('请输入你的姓名')
tall=input('请输入你的身高/米')
weight=input('请输入你的体重kg')
tall=float(tall)
Bmi=weight/(tall*tall)
weight=float(weight)
print(f'你的bmi是{Bmi:.2f}')
print(f'你的name11是{name1}')
print(f'你的身高是{tall}米')
print(f'你的体重是{weight}kg')