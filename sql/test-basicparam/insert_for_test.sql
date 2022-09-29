-- 开启某个参数，避免报错
set global log_bin_trust_function_creators=1;


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
create procedure insert_mptt(in p_name varchar(20),in n_level integer)
begin

-- declare p_name varchar(50);

-- set p_name = rand_string(4);



select @target_id:=MAX(node_id) from mptt where node_level=n_level-1 ;

select @nrgt:= rgt from mptt where node_id = @target_id ;
update mptt set rgt = rgt + 2 where rgt >= @nrgt ;
update mptt set lft = lft + 2 where lft >= @nrgt ;


insert into mptt (node_name, lft, rgt, node_level) values(p_name, @nrgt, @nrgt + 1, n_level);



end $$



-- 打造一个产品
delimiter $$
drop procedure if exists `create_product`;
create procedure `create_product`()
begin
    declare i int default 0;
    declare j int default 0;
    declare k int default 0;
    declare t int default 0;
    -- declare m int default 0;


    /* 有多少个项目 */
    while i < 2 do
    
   
    call insert_mptt(concat('风雷',i),2);
    /* call insert_mptt('200',3);
    call insert_mptt(concat('使用了算法',i),3);
    call insert_mptt('模块',3); */
   
  /* 每个项目有几个版本 */
    while j < 10 do

    call insert_mptt(rand_num(),3);
    /* 每个版本有多少参数要改 */
    while k < 10 do
   
    call insert_mptt(concat('旧参数',k),4);


    while t < 1 do

    call insert_mptt(concat('新参数',k),5);
    set t= t + 1;
    end while;
    set t = 0;

    set k= k + 1;
    end while;
    set k = 0;

    set j = j + 1;
    end while;
    commit;
    set j = 0;
    set i = i + 1;
   
    end while;
    
    
end $$

set global innodb_flush_log_at_trx_commit = 0;
call create_product();

