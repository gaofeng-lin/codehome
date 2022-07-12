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



-- 往person_param表中插入数据的存储过程
delimiter $$
drop procedure if exists insert_person_param;
create procedure insert_person_param()
begin


DECLARE s int DEFAULT 0;
declare p_t_id bigint(20);
/* declare varmodule int DEFAULT 0;
declare varparam int DEFAULT 0; */
declare pid cursor for select product_id from products;

DECLARE CONTINUE HANDLER FOR NOT FOUND SET s=1;

open pid;
fetch pid into p_t_id;
while s<>1 do

/* while varmodule<3 do */

/* while varparam<10 do */

insert into person_param (product_id, module_name, param_name, var_type, var_name, var_value, is_activated, compute_value) 
values(p_t_id,concat('模块','varmodule'),rand_string(3),'int',rand_string(6),'200',1,'ok');

/* set varparam=varparam+1;
end while;
set varparam=0; */

/* set varmodule=varmodule+1;

end while;
set varmodule=0; */

fetch pid into p_t_id;
end while;
close pid;

end $$

call insert_person_param();