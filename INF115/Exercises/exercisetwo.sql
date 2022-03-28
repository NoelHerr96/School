USE exercisetwo;

create table Game_info(
Boardgame varchar(32),
Year_Published integer not null,
Designer varchar(32) not null,
Publisher varchar (32),
Game_type varchar(32) not null,
Language varchar(16) not null,
Primary key (Publisher, Boardgame)
);

create table Game_store(
Store_numberId integer,
Store_name varchar(32) not null,
City_name varchar(32) not null,
Primary key (Store_numberId)
);

create table Game_sales(
Publisher varchar(32),
Boardgame varchar(32),
Store_numberId integer,
Year integer,
Month integer,
Quantity integer not null,
primary key (Publisher, Boardgame, Store_numberId, Year, Month),
Foreign key(Publisher, Boardgame) references Game_info(Publisher, Boardgame),
Foreign key(Store_numberId) references Game_store(Store_numberId)
);

insert into Game_info values ('Agricola', '2007', 'Uwe Rosenberg', 'Lookout Games', 'Strategy', 'German');
insert into Game_info values ('Pandemic', '2008', 'Matt Leacock', 'Z-Man Games', 'Cooperative', 'Norwegian');
insert into Game_info values ('Codesnames', '2015', 'Vlaada Chvatil', 'Czech Games Editions', 'Party game', 'English');
insert into Game_info values ('Five Tribes', '2014', 'Bruno Cathala', 'Days of Wonder', 'Strategy', 'English');
insert into Game_store values ('1', 'Outland', 'Bergen');
insert into Game_store values ('2', 'Tromsø Bruktbokhandel', 'Tromsø');
insert into Game_sales values ('Lookout Games', 'Agricola', '1', '2014', '8', '2');
insert into Game_sales values ('Lookout Games', 'Agricola', '2', '2014', '3', '1');
insert into Game_sales values ('Czech Games Edition', 'Codenames', '1', '2015', '2', '1');
 