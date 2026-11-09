class Student():
    def __init__(self,name,score):
        self.name=name
        self.score=score
        self.function()
    def __str__(self):
        return f"学生的姓名{self.name},成绩{self.score},等级为{self.state}"
    def function(self):
        if self.score>=90:
            self.state="优秀"
        elif self.score>=80:
            self.state="良好"
        elif self.score >= 70:
            self.state = "中等"
        elif self.score >= 60:
            self.state = "及格"
        else:
            self.state="不及格"
student=Student("张三",100)
print(student)
