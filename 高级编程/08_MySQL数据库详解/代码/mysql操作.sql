

create  database   if not exists day07;
create database  if not exists day07 character set utf8;
use day07;
show databases ;


# #创建表
# create table if not exists student(
#     name varchar(10),
#     age int ,
#     height float ,
#     birthday date
# );
# insert into student(name, age, height, birthday) value ("jack",18,111,'1999-01-11');
# insert into student(name, age, height, birthday) value ("rose",25,111,'2001-01-11');

#增删改
#删；
# delete from student where name="jack";
update student set name="lkt" where name="rose";
create  table stu2(
        name varchar(10),
        phone varchar(10),
    gender varchar(10)
);
insert  into stu2(name,phone)value ()

create table stu3(
    game varchar(10) primary key ,
    hp int not null ,
    name varchar(10) not null
);

insert into stu3(game,hp,name)value ("GTA1",100,"小胖")
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
#查看所有的商品
select  *from products;
select name,price,price from products;
select  name as n ,price p from products;
select  p.name,p.price from products as p ;
select distinct category_id from products;

select *from products where is_self='自营';
select *from products where score>9.5;
select *from products where products.score>=9.5;
select *from products where price<=999;
select *from products where score!=9.3;

select  *from products where price>2000 and is_self="自营";


#范围模糊in和between
select *from products where price between 1000 and 3000;
select *from products where price not between 1000 and 3000;

#模糊查询like   % 和__
select * from products where name like '%米%';
select * from products where name like '%兰%';

#非空判断is null   ="null"    =' '
insert into products(name,price) values('拯救者Y9000','9999');
insert into products(name,price) values('null','99');
insert into products(name,price) values('',0);


select * from products where score is null;
select * from products where name='null';
select * from products where name=' ';



#order by排序查询
select * from products order by score desc;
#聚合查询


select avg(price) from products;
select sum(price) from products;
select count(*) from products;
select is_self,avg(score)from products where is_self='非自营';
select  sum(price),
        avg(score),
        count(score),
        max(score),
        min(score)
from products
select * from products;
#内连接
select *
from products
inner join category
on products.category_id = category.id;


select
c.*,p.*
from products as p
inner join category as c
on p.category_id = c.id;

select
p.*,c.*
from products p
inner join category c
on p.category_id = c.id;

select
p.*,c.*
from products p
inner join category c
on c.id = p.category_id;


#右链接
select *
from  products
right join category
on category.id = products.category_id

#左链接
select *
from  products
left join category
on category.id = products.category_id


#左链接
select *
from  category c
left join products p
on p.category_id = c.id

#右链接
select *
from  category c
right  join products p
on p.category_id = c.id


#全链接
select *
from products p
left join category c on c.id = p.category_id
union all
select *
from products p
right  join category c on c.id = p.category_id