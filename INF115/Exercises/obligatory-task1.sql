#Written by Noel Santillana Herrera

#Task 1a)
SELECT DISTINCT country 
FROM film;


#Task 1b
SELECT * FROM film 
WHERE genre='Drama' AND duration < '02:00:00';


#Task 1c)
SELECT * FROM film 
WHERE title LIKE 'L%';


#Task 1d)
SELECT country, COUNT(*) AS NumFilms 
FROM film GROUP BY country 
HAVING COUNT(NumFilms) > 2;


#Task 1e)
SELECT country, SEC_TO_TIME(SUM(TIME_TO_SEC(duration))) AS TotalTime 
FROM FILM 
WHERE country='Italy';
