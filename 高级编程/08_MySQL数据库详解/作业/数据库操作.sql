# sql语句 选中运行
# 如何创建库  create database 数据库名称;
create database day07;
# 如何使用库
use day07;
# 判断 当数据库不存在时候 创建
create database if not exists day07;
# 指定字符集编码 数据库不是utf-8  而是utf8
create database if not exists day07 charset utf8;
# 展示库
show databases;

# 如何创建表
/*
create table 表名(
    字段的名称 字段的类型 [约束],
    字段的名称 字段的类型 [约束],
    字段的名称 字段的类型 [约束]
    最后一组字段字段名称 类型 约束后 不需要加逗号
)
*/
# 需求:创建学生表,用于存储学生的姓名,年龄,身高,生日信息
create table student(
    name varchar(10) ,
    age int ,
    height float ,
    birthday date
);


# 增
/*
    语法
        insert into 表名(字段,字段,字段...) values(值,值,值...)
        insert into 表名 values(值,值,值...)
            如果是省略语法,要求是每一个字段必须按照表顺序书写 且不能省略字段
        注意:
            1.字段的顺序和插入的值顺序应该保持一致
            2.字段的顺序和插入的值类型应该保持一致
            3.字段的顺序和插入的值个数应该保持一致

*/
# 插入数据
insert into student(name,age,height,birthday) values('jack' , 18,184.5 ,'1998-01-01');
insert into student values('rose' , 18,183.5 ,'1999-01-01');


# 删
/*
    语法:
        delete from 表名    删除所有数据
        delete from 表名 where 条件     根据指定的条件删除数据
*/
delete from student;
delete from student where name='jack';

# 改
/*
    语法:
        update 表名 set 字段名称=值,字段名称=值...
*/
update student set name = 'tom',age = 20 where name='jack';

# 约束
/*
    数据库数据 有限制的.需要有约束来控制数据的内容
        约束的主要作用: 规定数据的书写 保证数据的完整和有效性
        主键约束:   primary key 主键=唯一+非空
            一般取名叫id: 用于表示数据库中唯一的记录 且这个主键不可以重复 不可以为空
            主键约束还可以添加一个特殊的内容 主键自增 auto_increment
            auto_increment 作用: 当我们没有添加主键的时候 数据库自动管理 采用自增序列的方式
        唯一约束:   unique      保证数据在数据表中是唯一存在的
        非空约束:   not null    保证数据添加不能为空
        默认值约束: default      当不输入数据的时候 有一个默认值
        外键约束:   foreign key
*/
create table stu1(
    name varchar(10) ,
    phone varchar(11),
    gender varchar(2)
);
# 往表中添加数据
insert into stu1(name,phone) values('jack' , '13811112222');
insert into stu1(phone) values('13811112222');
#非空约束  唯一约束  默认值约束
create table stu2(
    name varchar(10) not null, # 非空约束
    phone varchar(11) unique,  # 唯一约束
    gender varchar(2) default '男' # 默认值
);
insert into stu2(name,phone) values('jack' , '13811112222');
#  Column 'name' cannot be null 名称不能为空
insert into stu2(name,phone) values(null , '13811112222');
# Duplicate entry '13811112222' for key 'phone'  唯一冲突
insert into stu2(name,phone) values('rose' , '13811112223');

create table stu3(
    id int primary key , # 主键约束
    name varchar(10)
);
#  Duplicate entry '1' for key 'PRIMARY' 主键冲突
insert into stu3(id,name) values(2,'jack');
# Column 'id' cannot be null  id不可以为空
insert into stu3(id,name) values(null,'jack');
# 每次添加数据 必须得保证id不可以为空
insert into stu3(id,name) values(3,'jack');


create table stu4(
    id int primary key auto_increment, # 主键约束
    name varchar(10)
);
# 有了auto_increment 以后 我们不需要操作主键 让数据库自动管理这个主键即可
insert into stu4(id,name) values(null,'jack');


/*
    面试题:
        数据库中 delete from 表    表示清空数据库表的数据
        数据库中 truncate  表      表示清空数据库表的数据
    区别:
        delete  只删除数据库中的表数据 但是不会重置自增序列
        truncate 重构表,不仅删除数据 而且还要重置自增序列

*/
delete from stu4;
insert into stu4(id,name) values(null,'jack');
truncate stu4;
insert into stu4(id,name) values(null,'jack');


# 必须会的
# 创建数据库: create database 库名;
CREATE DATABASE IF NOT EXISTS my_db CHARSET=utf8;

# 使用数据库: use 库名;
USE my_db;

# 创建表: create table 表名(字段名 字段类型 [约束],...);
# 建测试表
drop table if EXISTS products;
CREATE TABLE IF NOT EXISTS products
(
    id          INT PRIMARY KEY AUTO_INCREMENT, -- 商品ID
    name        VARCHAR(24)    NOT NULL,        -- 商品名称
    price       DECIMAL(10, 2) NOT NULL,        -- 商品价格
    score       DECIMAL(5, 2),                  -- 商品评分，可以为空
    is_self     VARCHAR(8),                     -- 是否自营
    category_id INT                             -- 商品类别ID
);

drop table if EXISTS category;
CREATE TABLE IF NOT EXISTS category
(
    id   INT PRIMARY KEY AUTO_INCREMENT, -- 商品类别ID
    name VARCHAR(24) NOT NULL            -- 类别名称
);

# 插入数据: insert into 表名 (字段名,字段名) values(字段值,字段值),(字段值,字段值);
# 添加测试数据
INSERT INTO category
VALUES (1, '手机'),
       (2, '电脑'),
       (3, '美妆'),
       (4, '家居');

INSERT INTO products
VALUES (1, '华为Mate50', 5499.00, 9.70, '自营', 1),
       (2, '荣耀80', 2399.00, 9.50, '自营', 1),
       (3, '荣耀80', 2199.00, 9.30, '非自营', 1),
       (4, '红米note 11', 999.00, 9.00, '非自营', 1),
       (5, '联想小新14', 4199.00, 9.20, '自营', 2),
       (6, '惠普战66', 4499.90, 9.30, '自营', 2),
       (7, '苹果Air13', 6198.00, 9.10, '非自营', 2),
       (8, '华为MateBook14', 5599.00, 9.30, '非自营', 2),
       (9, '兰蔻小黑瓶', 1100.00, 9.60, '自营', 3),
       (10, '雅诗兰黛粉底液', 920.00, 9.40, '自营', 3),
       (11, '阿玛尼红管405', 350.00, NULL, '非自营', 3),
       (12, '迪奥996', 330.00, 9.70, '非自营', 3);


# 单表
# 查询的基础语法:  select * from 表名    select 查询  *表示所有的字段  from 来自于xxx
select * from category; # category 分类
select * from products; # products 商品


-- 需求1: 查看所有商品
select * from products;

-- 需求2: 查看所有商品的名称和价格
# select 字段,字段,字段... from 表
select name,price from products;

-- 需求3: 查看所有商品的名称和价格,要求给字段名起别名展示
# 数据库中字段名都是提前定义好的  可以使用as 临时修改  注意: as可以省略
select name as 姓名,price 价格 from products;


-- 需求4: 查看所有商品的名称和价格,要求给表名起别名并使用

-- 如果给表起了表名,必须用别名调用字段
select p.name as 姓名,p.price 价格 from products as p;
-- 需求5: 查看所有的分类编号,要求 展示
#  重复的内容不展示   distinct  多字段重复的时候 才会去重
select distinct category_id , name from products;


# 列计算:  列上是可以直接进行计算  字段的展示由我们决定 可以加上多个同名字段
select name,price,price-100 from products;

# 条件是数据库中用于锁定数据的依据  where 条件
# 条件查询-比较 > < = >= <= != <>

-- 需求1: 查询所有'自营'的商品
select * from products where is_self = '自营';

-- 需求2: 查询评分在'9.50'(不含)以上的商品
select * from products where score>9.5;

-- 需求3: 查询评分在'9.50'(含)以上的商品
select * from products where score>=9.6;
-- 需求4: 查询价格在999(不含)以下的商品
select * from products where price < 920;
-- 需求5: 查询价格在999(含)以下的商品
select * from products where price <= 920;

-- 需求6: 查询评分不等于9.30的商品
select * from products where score!=9.3;
select * from products where score <> 9.3;

# 条件查询-逻辑 and or  not
-- and: 并且  or:或者  not:取反

-- 需求1: 查询自营商品中所有价格大于2000的商品信息
select * from products where is_self='自营' and price > 2000;
-- 需求2: 查询商品评分在9.0(含)-9.5(含)之间的商品信息
select * from products where score >=9.0 and score <=9.5;
-- 需求3: 查询商品价格在1000(含)到3000(含)之间的商品信息
select * from products where price >=1000 and price <=3000;
-- 需求4: 查询价格是999或者2199或者2399的商品
select * from products where price =999 or price =2199 or price = 2399;
-- 需求5: 查询商品是'华为Mate50'或者'荣耀80'的商品
select * from products where name = '华为Mate50' or name = '荣耀80';
-- 需求6: 查询商品不是自营的商品
select * from products where is_self= '非自营';
select * from products where is_self!= '自营';
select * from products where not is_self= '自营';
-- 需求7: 查询商品不在1000到3000之间的商品
select * from products where price > 3000 or price < 1000;
select * from products where not (price <= 3000 and price >= 1000);


# 条件查询-范围
-- 需求1: 查询商品价格在1000(含)到3000(含)之间的商品信息
select * from products where price >=1000 and price<=3000;
# 字段 between 最小值 and 最大值
select * from products where price between 1100 and 2399;
-- 注意: 以下语法是错误的
select * from products where price between 3000 and 1000;
-- 需求2: 查询商品不在1000到3000之间的商品
select * from products where price not between 1100 and 2399;
select * from products where not price between 1100 and 2399;
-- 需求3: 查询价格是999或者2199或者2399的商品
select * from products where price = 999 or price = 2199 or price =2399;
# 使用in的语法替代  in (值1,值2,值3)
select * from products where price in (999,2199,2399);
-- 需求4: 查询商品是'华为Mate50'或者'荣耀80'的商品
select * from products where name in ('华为Mate50','荣耀80');

# 条件查询-模糊  =表示完全匹配
# like表示模糊匹配  % 匹配0到多个字符   _匹配一个字符
-- 需求1: 查询商品名称以'华'开头的商品信息
select * from products where name like '华%';

-- 需求2: 查询商品名称以'华'开头并且8个字符的商品信息
select * from products where name like '华_______';
-- 需求3: 查询商品名称以'66'结尾商品信息
select * from products where name like '%66';
-- 需求4: 查询商品名称中包含'兰'字的商品信息
select * from products where name like '%兰%';
-- 需求5: 查询商品名称中第3个字是'兰'字的商品信息
select * from products where name like '__兰%';


# 条件查询-非空
-- 为了方便演示null和'','null'的区别,可以插入部分测试数据
select * from products;
insert into products(name,price) values('拯救者Y9000','9999');
insert into products(name,price) values('null','99');
insert into products(name,price) values('',0);

/*
    <null> : 表示不存在  空间都没有
        不能使用等号 只能使用is null 或者 is not null
    null : 表示这个字符串是null
    空   : 空间是有 但是没有存入任何内容 空串

*/
-- 需求1:查询未评分的商品信息
select * from products where score is null;
select * from products where score is not null;
-- 需求2:查询商品名称是'null'的商品信息
select * from products where name  = 'null';
-- 需求3:查询商品名称是''的商品信息
select * from products where name  = '';

# 排序 select * from 表  order by 排序的字段 asc升序 / desc 降序 ,排序的字段 asc升序 / desc 降序...   默认升序
-- 示例1：查询所有商品，并按照评分从高到低进行排序
select * from products order by score desc;
-- 示例2：查询所有商品，先按照评分从高到低进行排序，评分相同的再按照价格从低到高排序
select * from products order by score desc,price asc;
# 聚合
/*
    五个聚合函数: avg(字段) 平均数  min(字段) 最小值  max(字段) 最大值 sum(字段)求和  count(字段) 计数
    所有的聚合一般用于 统计的需求
*/
-- 示例1：统计当前商品一共有多少件
select count(*) from products;
-- 示例2：对商品评分列进行计数、求最大、求最小、求和、求平均
select count(*),max(score),min(score),sum(score),avg(score) from products;
-- 示例3：统计所有非自营商品评分的平均值
select avg(score) from products where is_self='非自营';


# 分组 : 本质上就是数据归类 一般来说 聚合函数要匹配分组一起使用
# select 分组的字段或者聚合函数 from 表名 where 分组前条件 group by 分组的字段 having 分组后条件
-- 示例1：统计每个分类的商品数量
select category_id,count(*) from products group by category_id;
-- 示例2：统计每个分类商品的平均价格
select category_id,avg(price) from products group by category_id;

# select 字段 from 表 where 条件 group by 分组
# 需求: 统计每个分类商品的平均价格  只需要自营商品
select category_id,avg(price)
    from products
    where is_self = '自营'
    group by category_id;

-- 示例3： 统计每个分类商品的平均价格 只需要自营商品 并筛选出平均价格低于1100的分类
select category_id,avg(price)
    from products
    where is_self = '自营'
    group by category_id
    having avg(price)< 1100;


# 分页 select * from products 查询当前表中的所有记录
/*
    在平常访问网页的过程中 通过页码翻找数据  还需要设置每页展示的条数
        页码 pageNumber currentPage
        展示条数 pageSize
    语法:
        select * from 表 limit 参数1,参数2
    参数1: startIndex  开始的索引  计算公式 (pageNumber-1)*pageSize
    参数2: pageSize    每页展示的个数
*/
select * from products;
# 查询第1页3条数据
# 如果查询的是第一页的数据 参数1可以省略
select * from products limit 0,3;
select * from products limit 5;
# 查询第2页3条数据
select * from products limit 3,3;
# 查询第3页3条数据
select * from products limit 6,3;
# 查询第4页3条数据
select * from products limit 9,3;
# 查询第5页3条数据
select * from products limit 12,3;
# 查询第pageNumber页pageSize条数据
#select * from products limit (pageNumber-1)*pageSize,pageSize
# 多表

/*
    多表: 多张表
    多表查询: 将多张表的数据放在一起 统一查询出来
        交叉连接(笛卡尔积查询): 没用. 两个表数据的乘积.
            以其中一张表为例,将此表数据全部查询出来.匹配另一张表中的所有记录
            4x15 = 60   15x4 = 60
            语法: select * from 表名,表名,表名,表名....
        内连接: 基于笛卡尔积的基础之上  将数据筛选出来有效数据
        无论是显示内连接还是隐式内连接 书写表顺序没有所谓  展示顺序有变化 内容还是一致 , 查询多个表的交集
            隐式内连接:(用的人少 只有一些老程序员用) 书写过多的条件 分不清楚
                select * from 表名,表名,表名,表名.... where 从表的外键字段= 主表的主键字段
            显示内连接:
                select * from A表
                    inner join B表 on 从表的外键字段= 主表的主键字段
                    inner join C表 on 从表的外键字段= 主表的主键字段
                    inner join D表 on 从表的外键字段= 主表的主键字段
                    where 普通条件
        外连接: 左外连接和右外连接 表顺序 不能随意书写  左外连接和右外连接记一个即可
            左外连接: 以关键字左边的表为主 ,将左表的数据全部查询出来 再次匹配右表,如果匹配上的展示,匹配不上的数据 展示为null

                select * from A表
                    left join B表 on 从表的外键字段= 主表的主键字段
                    left join C表 on 从表的外键字段= 主表的主键字段
                    left join D表 on 从表的外键字段= 主表的主键字段
                    where 普通条件
            右外连接: 以关键字右边的表为主 ,将右表的数据全部查询出来 再次匹配左表,如果匹配上的展示,匹配不上的数据 展示为null
                select * from A表
                    right join B表 on 从表的外键字段= 主表的主键字段
                    right join C表 on 从表的外键字段= 主表的主键字段
                    right join D表 on 从表的外键字段= 主表的主键字段
                    where 普通条件
        全连接:
                将任意的组合在一起 哪怕字段不一致都可以  但是得保证 两张表的字段个数一致的
                union     : 用于拼接两张表的关键字 , 展示所有的数据 包括自动去重 : 要求是字段的顺序必须是一致的 内容必须是一致的
                    查询语句 union 查询语句
                union all : 用于拼接两张表的关键字 , 展示所有的数据 包括重复的数据
                    查询语句 union all  查询语句
        自连接:
        子查询:
*/
# 交叉查询: 理论知识, 会产生大量的冗余数据 错误数据
select * from category , products;

# 解决笛卡尔积带来的问题  条件书写的时候 需要携带 表名
select * from category , products
    where category.id = products.category_id;
# 这种查询就是 隐式内连接
select * from category as c , products as p
    where c.id = p.category_id;

# 显示内连接
select c.*,p.*
    from category c
    inner join products p on c.id = p.category_id;
# 无论是显示内连接还是隐式内连接 书写表顺序没有所谓  展示顺序有变化 内容还是一致
# 内连接查询的时候 只展示两个表的交集部分
select c.*,p.*
    from products p
    inner join category c on c.id = p.category_id;


#左外连接
select *
    from category c
    left join products p on c.id = p.category_id;
#右外连接
select c.*,p.*
    from category c
    right join products p on c.id = p.category_id;


select c.*,p.*
    from products p
    left join category c  on c.id = p.category_id;


# 全连接
/*
    将任意的组合在一起 哪怕字段不一致都可以  但是得保证 两张表的字段个数一致的
    union     : 用于拼接两张表的关键字 , 展示所有的数据 包括自动去重 : 要求是字段的顺序必须是一致的 内容必须是一致的
        查询语句 union 查询语句
    union all : 用于拼接两张表的关键字 , 展示所有的数据 包括重复的数据
        查询语句 union all  查询语句
*/
# select id,name from category
# union
# select id,name from products;

# 左外连接和左外连接 使用union进行拼表
select c.*,p.* from category c
    left join products p on c.id = p.category_id
union
select c.*,p.* from products p
    left join category c on c.id = p.category_id;


select c.*,p.* from category c
    left join products p on c.id = p.category_id
union all
select c.*,p.* from products p
    left join category c on c.id = p.category_id;


select * from areas where title like '%市';

# 自关联
-- 查询'广东省'下所有城市
select * from areas as sheng
    left join areas as shi on shi.pid = sheng.id
    where sheng.title = '广东省';


-- 查询'深圳市'下所有的区县
select * from areas as shi
    left join areas as qu on qu.pid= shi.id
    where shi.title='深圳市';
-- 查询'广东省'下所有的市,以及市下面的区县信息
# 多表代码书写的时候 先关心 两张表 再去关联第三张
select sheng.title,shi.title,qu.title
    from areas  as sheng
    left join areas as shi on sheng.id=shi.pid
    left join areas as qu on shi.id = qu.pid
    where sheng.title='广东省';