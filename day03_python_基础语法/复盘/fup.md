为什么学python：简单易上手，33个关键字，7个数据类型（str,数组类型，元组，列表，字典，集合）

anconda的使用：

（沙箱机制）：一个个独立环境互相不冲突

查看当前anaconda的环境：

创造一个新的环境（举例创建一个py310）：conda create -n py310 python=3.10

创建环境：cond activate  py310

删除环境：conda remove -npy310 --all

注释：

变量：就是运行过程中会变的量，字母数字下划线组成，数字不能为前

变量使用：字母数字下划线组成，一般不是以_开头以及和数字不能开头，不能使用关键字（严格区别大小写）

要先定义在调用



七种数据类型：数值（int,float),布尔类型（boolean),字符串（str),元组（tuple),列表（list),字典（dict)集合（set)

判断数据类型还是有一个不太会使用

isinstance:isinstance方法是比较这个数据类是否属于参数里面的数据类型，是则True,不是则False

isidentifier()方法是此法判断：字符串对象的方法，是否符合字符串的命名规则	

布尔类型

python的输出：格式化输出，百分号输出,.format,和f-string,其中有个遗忘的点就是比如要求的留下小数点这个方法忘记了：记忆点%直接.f要注意，“”后面不要有，才错的，。format里面占位符是：冒号让后.f最后就是f-string方法也是：.f但是要注意参数写前面在：.f

Python 的格式化默认使用**银行家舍入法**（四舍六入五成双）3.5成为4，2.5成为2不为3

转义字符：就是\就是转义字符，顾名思义，print方法后面固定有一个\n, 我有一个混淆点就是\n是换行，\t在表头为四个字缩进的空格，在其他地方则是空格一个

input方法：获取的数据类型都是字符串

数据类型的转换：

float(x),int(x),str(x),但是要注意一个字符串和int转换，要先用float去转换str,再用int去转换float

![image-20261108171352228](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20261108171352228.png)

这个就是int强制转换字符串可能会报的错误

如果在银行系统里面不要用float方法要用decimal模块

