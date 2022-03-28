select * from cities;

select Name, Area from cities where Area < 2000 order by Area desc; #1a)

select * from border;

select Country1, count(country2) as neighborAmount from border group by Country1 having count(country1) <= 2; #1b

select * from population;

select Name, Number from population where year = 1980 order by Number desc; #1c?

select * from countries, population;


