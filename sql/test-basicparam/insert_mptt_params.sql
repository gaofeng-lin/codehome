/* 这个是mptt版本的person_param */

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

select @target_id:=MAX(node_id) from mptt_param where node_level=n_level-1 ;

select @nrgt:= rgt from mptt_param where node_id = @target_id ;
update mptt_param set rgt = rgt + 2 where rgt >= @nrgt ;
update mptt_param set lft = lft + 2 where lft >= @nrgt ;


insert into mptt_param (node_name, lft, rgt, node_level) values(p_name, @nrgt, @nrgt + 1, n_level);


end $$




-- 打造一个产品
delimiter $$
drop procedure if exists `create_product`;
create procedure `create_product`()
begin
    declare i int default 0;
    declare j int default 0;
    declare k int default 0;
    DECLARE s int DEFAULT 0;
    declare p_t_id bigint(20);
    declare varmodule int DEFAULT 0;
    declare varparam int DEFAULT 0; 
    declare m_name varchar(255);
    -- declare m int default 0;

    declare pid cursor for select product_id from mptt_products;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET s=1;

    open pid;
    fetch pid into p_t_id;
    while s<>1 do
    call insert_mptt(p_t_id,2);
    while varmodule<3 do
    call insert_mptt(concat('模块',varmodule),3);

    while varparam<10 do
    call insert_mptt(concat('参数',varparam),4);

    call insert_mptt(concat('var_type',rand_string(2)),5);
    call insert_mptt(concat('var_name',rand_string(2)),5);
    call insert_mptt(concat('var_value',rand_string(2)),5);
   
    set varparam=varparam+1;
    end while;
    set varparam=0;
    set varmodule=varmodule+1;
    end while;
    set varmodule=0;
    fetch pid into p_t_id;
    end while;
    close pid;




/* 
    while i < 200 do

    start transaction;
    call insert_mptt(concat('风雷',i),2);
    call insert_mptt('200',3);
    call insert_mptt(concat('使用了算法',i),3);
    call insert_mptt('模块',3);
    commit;

    start transaction;
    while j < 3 do

    call insert_mptt(concat('模块',j),4);

    while k < 10 do
    start transaction;
    call insert_mptt(concat('参数',k),5);

    call insert_mptt(concat('var_type',rand_string(2)),6);
    call insert_mptt(concat('var_name',rand_string(2)),6);
    call insert_mptt(concat('var_value',rand_string(2)),6);
    commit;



    set k= k + 1;
    end while;
    set k = 0;

    set j = j + 1;
    end while;
    commit;
    set j = 0;
    set i = i + 1;
    end while; */




    
end $$

call create_product();

