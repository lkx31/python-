.Anaconda的使用
 打开anaconda的终端环境，搜索anaconda的终端

一些基础的命令

查看当前的anaconda的环境

conda env list  #查看当前conda的配置环境
conda叫做基础环境 env(environment）的缩写 list列表
base叫做基础环境
AI代码解释
python
运行
创建一个新的环境

conda create -n 名称 python=版本号
例子建立一个python的3.11版本
conda create -n py311 python=3.11
-n就是name的缩写 ，其中名称哪里不要有点踩坑了
AI代码解释
python
运行
激活环境：（创建事后要激活）

conda activate 环境名称
例子如上
conda activate py311
AI代码解释
python
运行
删除环境

conda remove -n 名称  或者conda  env remove -n 名称
AI代码解释
python
运行
python如何查看当前解释器的版本号

1.查看anaconda的命令行conda -V

2.在pycharm的界面右下角有一个地址点击Interpreter Settings...

如何切换版本和改名

右下角有一个地址点击Interpreter Settings...--》Python Interpreter:（就是长条选项），选择show all-->右键名称可以更改名字且上面加号可以更改解释器环境


​    

2.[熟悉】Python注释与快捷键
 注释的作用
        ：能够提高代码的阅读性

        有两种注释的方式shift+3以#开头的单行注释
    
        还有一种多行注释“”“”“是三个引号构成包裹
    
        快捷方式shift+/可以显示#的单行注释
    
        alt + shift + 鼠标左键 矩形编辑 批量操作多行代码
    
        ctrl + shift + U 快速大小写
    
        ctrl + f 搜索
    
        ctrl + r 替换
    
        ctrl + shift + 上下键 快速移动代码


​        

3.[掌握】Python中的变量
引|入变量的概念
        ：变量是什么

        变量就是一个存储数据的容器
    
        运行过程可以改变的量
    
        变量的存储是临时的
    
        字面量的含义本质上是一个固定的值
    
        变量=字面量

变量的定义
     

变量名称 = 变量的值
注：等号的两边都要保留一个空格，其实Python中建议符号的两边尽量都要保留一个空格
AI代码解释
python
运行
变量的命名规则
        以字母数字下划线组成

        不能关键字和特殊符号去命名（绝对）
    
        严格区分大小写
    
        不能数字开头以及最好不用下划线做开头

推荐变量的命名规则
        变量名要见名知道意思，例如name那么就是名字意思增强可读性

        大驼峰就是第一个单词首字母大写
    
        小驼峰就是第二个单词字母大写
    
        Username和userName
    
        或者下划线
    
        user_name

变量的定义与调用
        记住变量一定要先定义在调用

变量的定义与使用常见问题
        

        ① 变量与字符串如何区别：
    
        在Python中，如果要赋值的内容添加了单引号或者双引号，其就是Python中的一种数据  类        型：叫做字符串（日常生活中的文本信息）
    
        ② print打印变量时，喜欢为其添加引号

变量的数据类型

指的是字面量的类型

变量=字面量

总共七个数据类型：数值，布尔。字符串，列表，元组，集合，字典

数值类型：整型和浮点型。

布尔类型：True or False

字符串：单引号，双引号，或者三个单引号，或者三个双引号

要怎么确定字面量是什么类型呢？

使用type()方法判断数据类型

type是一个函数

单三个双引号单独出现表示注释，三个单或者双引号在赋值的时候是字符串，应用在多行文本的时候，中间不可拼接三个单引号或者双引号，

三引号 ''' ''' 或 """ """：专门用来定义多行字符串。它会原封不动地保留你输入的所有格式，包括空格和回车（换行符 \n）。

s = '''张
三'''
print(repr(s)) 
# 输出结果会是：'张\n三'
AI代码解释
小的注意事项：python特性，代码自上而下运行，变量本身没有数据类型，所有的数据类型取决于字面量，变量的定义是会被覆盖的

isinstance(参数1，参数2）判断参数1是不是参数2的数据类型    int,float,boolean,str

repr 是 representation（表示）的缩写。

它的作用是返回一个对象的“官方”字符串表示。简单来说，repr() 主要是给程序员（也就是你）看的，用来查看这个变量在 Python 底层到底长什么样。

print(repr(123))  # 输出：123 （没有引号，说明是数字）
print(repr('123'))# 输出：'123' （有引号，说明是字符串）
AI代码解释
%格式的运用

格式化 ：字符串加上变量=某种特殊的格式

print('我的名字是：+name,我的年龄是：+age‘）

方案1：format 不常用{}表示占用

print(“我的名字是：{}，年龄是：{}，身高是{}”.format(name,age,height))

方案2：%号方法不常用

print(“我的名字是：%s，年龄是：%d，身高是%f” %(name,age,height)

方案3：格式化；python3.6版本以后

print(f“我的名字是：{name}，年龄是：{age}，身高是{height}”)

转义符号

什么是转义：修改原本的语义

实例：
s1='I'm jack'
s1='I\'m jack'
AI代码解释
\t就是空格\n是换行，\t在前面就是制表符，\t在中间就是空格

想看源码CTRL+鼠标左键点击单词

print 有一个end属性，表示结尾\n表示换行        

输入input方法

程序外的内容进入程序

input接收到输入的都是字符串，只有字符串

看报错

先看line具体哪一行再看报错的原因

转换类型类型（变量）

例子price=float(price)

str->float

a='175.5'

print(type(a),)

str->int

int->str

eval机器学习 

eval可以将字符串变成可执行的代码片段

int->float

float->int
————————————————
版权声明：本文为CSDN博主「在学习的小胖」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/m0_70281824/article/details/169449817