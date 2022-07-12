-- 创建表
-- create table tb_dept_bigdata(
-- id int unsigned primary key auto_increment,
-- deptno mediumint unsigned not null default 0,
-- dname varchar(20) not null default '',
-- loc varchar(13) not null default ''
-- )engine=innodb default charset=utf8;



-- 开启某个参数，避免报错
set global log_bin_trust_function_creators=1


-- 随机字符串
delimiter $$
drop function if exists rand_string;
create function rand_string(n int) returns varchar(255)
begin
declare chars_str varchar(52) default 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
declare return_str varchar(255) default '';
declare i int default 0;
while i<n do
set return_str=concat(return_str,substring(chars_str,floor(1+rand()*52),1));
set i=i+1;
end while;
return return_str;
end $$

-- 随机数
delimiter $$
drop function if exists rand_num;
create function rand_num() returns int(5)
begin
declare i int default 0;
set i=floor(100+rand()*100);
return i;
end $$

-- 往products表中插入数据的存储过程
delimiter $$
drop procedure if exists insert_products;
create procedure insert_products(in start int(10),in max_num int(10))
begin
declare i int default 0;
set autocommit=0;
repeat
set i=i+1;
insert into products (product_name,cfdversion,product_info,is_activated) values(concat('风雷',i),rand_num(),rand_string(8),1);
until i=max_num
end repeat;
commit;
end $$


-- 调用存储过程
call insert_products(100,200);


