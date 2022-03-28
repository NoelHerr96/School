USE exerciseone;
create table Film (
FNr integer,
Title varchar(32),
Year integer,
Country varchar(32),
Director varchar(32),
Run_time integer,
Price integer,
CONSTRAINT pk PRIMARY KEY (FNr)
);
insert into Film values ('1', '2001: A Space Odyssey', '1968', 'USA', 'Stanley
Kubrick', '141', '149');
insert into Film values ('2', 'Blade Runner', '1982', 'USA', 'Ridley Scott',
'117', NULL);
insert into Film values ('3', 'Alien', '1979', 'USA', 'Ridley Scott', '116',
'123');
insert into Film values ('4', 'Aliens', '1986', 'USA', 'James Cameron', '137',
'123');
insert into Film values ('5', 'Star wars', '1977', 'USA', 'George Lucas', '121',
NULL);
insert into Film values ('6', 'Brazil', '1985', 'UK', 'Terry Gilliam', '142',
'149');
insert into Film values ('7', 'Metropolis', '1927', 'Germany', 'Fritz Lang',
'124', '87');
insert into Film values ('8', 'The Terminator', '1984', 'USA', 'James Cameron',
'107', '149');
insert into Film values ('9', 'The Empire Strikes Back', '1980', 'USA', 'George
Lucas', '124', '123');
insert into Film values ('10', 'ET the Extra-Terrestrial', '1982', 'USA',
'Steven Spielberg', '115', '87');
insert into Film values ('11', 'The Thing', '1982', 'USA', 'John Carpenter',
'109', '135');
insert into Film values ('12', 'Moon', '2009', 'UK', 'Duncan Jones', '97',
NULL);
insert into Film values ('13', 'Stalker', '1979', 'Soviet Union', 'Andrei
Tarkovsky', '161', NULL);