CREATE TABLE Countries(
Name varchar (20),
Area INT,
Capital_city varchar (20),
CONSTRAINT Countries_PK PRIMARY KEY (Name)
);
CREATE TABLE Cities(
Name varchar (20),
Area INT,
Country varchar (20),
CONSTRAINT Cities_PK PRIMARY KEY (Name),
CONSTRAINT Cities_FK FOREIGN KEY (Country) REFERENCES Countries(Name)
);
CREATE TABLE Population(
Name varchar (20),
Year smallint,
Number INT,
CONSTRAINT population_PK PRIMARY KEY (Name, Year),
CONSTRAINT population_FK1 FOREIGN KEY (Name) REFERENCES Countries(Name)
);
CREATE TABLE Border(
Country1 varchar (20),
Country2 varchar (20),
CONSTRAINT Border_PK PRIMARY KEY (Country1, Country2),
CONSTRAINT Border_FK1 FOREIGN KEY (Country1) REFERENCES Countries(Name),
CONSTRAINT Border_FK2 FOREIGN KEY (Country2) REFERENCES Countries(Name)
);
INSERT INTO Countries (Name, Area, Capital_city) VALUES ('Norway', 385178,
'Oslo');
INSERT INTO Countries (Name, Area, Capital_city) VALUES ('Sweden', 450295,
'Stockholm');
INSERT INTO Countries (Name, Area, Capital_city) VALUES ('Finland', 338424,
'Helsinki');
INSERT INTO Countries (Name, Area, Capital_city) VALUES ('Russia', 17098242,
'Moscow');
INSERT INTO Countries (Name, Area, Capital_city) VALUES ('Iceland', 102775,
'ReykjavÃk');
INSERT INTO Cities (Name, Area, Country) VALUES ('Oslo', 480, 'Norway');
INSERT INTO Cities (Name, Area, Country) VALUES ('Stockholm', 188, 'Sweden');
INSERT INTO Cities (Name, Area, Country) VALUES ('Helsinki', 715, 'Finland');
INSERT INTO Cities (Name, Area, Country) VALUES ('Moscow', 2511, 'Russia');
INSERT INTO Cities (Name, Area, Country) VALUES ('ReykjavÃk', 273, 'Iceland');
INSERT INTO Population (Name, Year, Number) VALUES ('Norway', '2015', 5166000);
INSERT INTO Population (Name, Year, Number) VALUES ('Norway', '2000', 4478000);
INSERT INTO Population (Name, Year, Number) VALUES ('Norway', '1980', 4091000);
INSERT INTO Population (Name, Year, Number) VALUES ('Sweden', '2015', 9802000);
INSERT INTO Population (Name, Year, Number) VALUES ('Sweden', '2000', 8861000);
INSERT INTO Population (Name, Year, Number) VALUES ('Sweden', '1980', 8318000);
INSERT INTO Population (Name, Year, Number) VALUES ('Finland', '2015', 5486000);
INSERT INTO Population (Name, Year, Number) VALUES ('Finland', '2000', 5171000);
INSERT INTO Population (Name, Year, Number) VALUES ('Finland', '1980', 4771000);
INSERT INTO Population (Name, Year, Number) VALUES ('Russia', '2015',
143976000);
INSERT INTO Population (Name, Year, Number) VALUES ('Russia', '2000',
146597000);
INSERT INTO Population (Name, Year, Number) VALUES ('Russia', '1980',
138483000);
INSERT INTO Population (Name, Year, Number) VALUES ('Iceland', '2015', 329000);
INSERT INTO Population (Name, Year, Number) VALUES ('Iceland', '2000', 318000);
INSERT INTO Population (Name, Year, Number) VALUES ('Iceland', '1980', 254000);
INSERT INTO Border (Country1, Country2) VALUES ('Norway', 'Sweden');
INSERT INTO Border (Country1, Country2) VALUES ('Norway', 'Russia');
INSERT INTO Border (Country1, Country2) VALUES ('Norway', 'Finland');
INSERT INTO Border (Country1, Country2) VALUES ('Sweden', 'Norway');
INSERT INTO Border (Country1, Country2) VALUES ('Sweden', 'Finland');
INSERT INTO Border (Country1, Country2) VALUES ('Finland', 'Norway');
INSERT INTO Border (Country1, Country2) VALUES ('Finland', 'Sweden');
INSERT INTO Border (Country1, Country2) VALUES ('Finland', 'Russia');
INSERT INTO Border (Country1, Country2) VALUES ('Russia', 'Norway');
INSERT INTO Border (Country1, Country2) VALUES ('Russia', 'Finland');