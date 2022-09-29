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
drop procedure if exists insert_mptt;
create procedure insert_mptt(in nid Integer,in p_name varchar(20),in n_level integer)
begin

-- declare p_name varchar(50);

-- set p_name = rand_string(4);

select @nrgt:= rgt from mptt where node_id = nid ;
update mptt set rgt = rgt + 2 where rgt >= @nrgt ;
update mptt set lft = lft + 2 where lft >= @nrgt ;


insert into mptt (node_name, lft, rgt, node_level) values(p_name, @nrgt, @nrgt + 1, n_level);


end $$



/* 二级节点 --产品名称*/
delimiter $$
drop procedure if exists `two_level`;
create procedure `two_level`(in p_name varchar(20))
begin

    /* 获取一级节点最大的id */
    select @target_id:=MAX(node_id) from mptt where node_level=1 ;

    call insert_mptt(@target_id, p_name, 2);
    


end $$


/* 三级节点-- 求解器版本号，产品说明，模块（module,name）*/
delimiter $$
drop procedure if exists `three_level`;
create procedure `three_level`(in p_name varchar(20))
begin

    
    select @target_id:=MAX(node_id) from mptt where node_level=2 ;

    call insert_mptt(@target_id, p_name, 3);

end $$
/* 四级节点--模块 */
delimiter $$
drop procedure if exists `four_level`;
create procedure `four_level`(in p_name varchar(20))
begin

    
    select @target_id:=MAX(node_id) from mptt where node_level=3 ;

    call insert_mptt(@target_id, p_name, 4);

end $$
/* 五级节点 */
/* 六级节点 */



--  call insert_mptt(1,'heop'); 
-- call two_level('风雷2号');

-- 打造一个产品
delimiter $$
drop procedure if exists `create_product`;
create procedure `create_product`()
begin
    declare i int default 0;
    call two_level('风雷1号');
    
    call three_level('200');
    call three_level('使用了算发2');
    call three_level('模块');
    while i < 3 do
    call four_level(concat('模块',i));


    set i = i + 1;
    end while;
    
end $$

call create_product();

