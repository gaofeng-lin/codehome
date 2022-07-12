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


/* 构造一个产品 */

delimiter $$
drop procedure if exists insert_mptt;
create procedure insert_mptt(in start int(10),in max_num int(10))
begin

declare p_name varchar;
/* declare p_cfdversion int;
declare p_info varchar;
declare p_is_activated int; */

set p_name=rand_string(2);
/* p_cfdversion = rand_num();
p_info = rand_string();
p_is_activated = 1; */

/* select @nrgt:= rgt from mptt where node_id = 1 ;
update mptt set rgt = rgt + 2 where rgt >= @nrgt ;
update mptt set lft = lft + 2 where lft >= @nrgt ;


insert into mptt (node_name, lft, rgt) values(p_name, @nrgt, @nrgt + 1); */

select p_name;

end $$
