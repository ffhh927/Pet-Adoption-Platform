
#CREATE DATABASE petadoption

create trigger Application_create_date before insert on adoptionapplication
for each row set NEW.ap_time = NOW();

delimiter ;;	
create trigger Application_create_city after insert on adoptionapplication
for each row begin
set @val = 0;
select @val:=count(*) from city where city.city_province = new.u_city;
if @val = 0 then insert into city (city_province) values(new.u_city); end if;
end;;
delimiter ;	

	
create definer = `root`@`localhost` trigger Application_update_date before update on adoptionapplication
for each row 
set new.a_time = NOW(); 



delimiter ;;	
create definer = `root`@`localhost` trigger account_add after insert on account
for each row begin
if new.u_type = 'U' then insert into adopter (u_no) values(new.u_no); end if;
if new.u_type = 'A' then insert into administrator (u_no) values(new.u_no); end if;
end;;

delimiter ;	

create
	algorithm = undefined
    definer = `root`@`localhost`
    sql security definer
view `petadoption`.`petInfo` as
select
	pet.p_name, pet.p_age, pet.p_sex, pet.p_character, pet.is_adopted, breed.b_name, type.type_name
    from pet,breed,type where pet.b_id = breed.b_id and breed.type_id = type.type_id


delimiter ;;	
create procedure add_pet(in p_name varchar(10), in p_age smallint, in p_sex char(1), p_character varchar(50),in b_name varchar(20),in type_name varchar(5))	
	begin
		set @var=0;
        set @var1=0;
		select @var:=count(*) from type where type.type_name = type_name;
        if @var = 0 then insert into type (type_name) values(type_name);end if;
        select @var:=type.type_id from type where type.type_name = type_name;
        select @var1:=count(*) from breed where breed.b_name = b_name;
        if @var1 = 0 then insert into breed (type_id,b_name) values(@var,b_name);end if;
        select @var1:=breed.b_id from breed where breed.b_name = b_name;
        insert into pet (b_id,p_name,p_age,p_sex,p_character,is_adopted) values (@var1,p_name,p_age,p_sex,p_character,'0');
	end;;

delimiter ;
ALTER TABLE breed ADD UNIQUE INDEX (b_name);


delimiter ;;	
create procedure alter_pet(in p_id_i int, in p_name varchar(10), in p_age smallint, in p_sex char(1), p_character varchar(50),in b_name varchar(20),in type_name varchar(5))	
	begin
		set @var=0;
        set @var1=0;
		select @var:=count(*) from type where type.type_name = type_name;
        if @var = 0 then insert into type (type_name) values(type_name);end if;
        select @var:=type.type_id from type where type.type_name = type_name;
        select @var1:=count(*) from breed where breed.b_name = b_name;
        if @var1 = 0 then insert into breed (type_id,b_name) values(@var,b_name);end if;
        select @var1:=breed.b_id from breed where breed.b_name = b_name;
        update pet set pet.b_id = @var1,pet.p_name = p_name,pet.p_age = p_age,pet.p_sex = p_sex,pet.p_character = p_character,pet.is_adopted = '0' where pet.p_id = p_id_i;
	end;;
delimiter ;

SET SQL_SAFE_UPDATES = 0;