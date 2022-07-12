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



/* 构造一个节点 */

delimiter $$
drop procedure if exists `insert_mptt`;
create procedure `insert_mptt`(in nid Integer)
begin

declare p_name varchar(50);

set p_name = rand_string(4);

select @nrgt:= rgt from mptt where node_id = nid ;
update mptt set rgt = rgt + 2 where rgt >= @nrgt ;
update mptt set lft = lft + 2 where lft >= @nrgt ;


insert into mptt (node_name, lft, rgt) values(p_name, @nrgt, @nrgt + 1);


end $$



/* 二级节点 --产品名称*/
delimiter $$
drop procedure if exists `two_level`;
create procedure `two_level`(in p_name varchar, in level int)
begin

/* 获取一级节点最大的id */

delcare father_id int;



end $$


/* 三级节点 */

/* 四级节点 */
/* 五级节点 */
/* 六级节点 */



/* call insert_mptt(2); */