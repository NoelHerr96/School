#Written by Noel Santillana Herrera

#Task 3a)
SELECT film.title AS title, screening.showtime AS director 
FROM film 
JOIN screening ON screening.film_id = film.film_id 
WHERE genre='Horror' ;


#Task 3b)
SELECT title, director, COUNT(screening.film_id) as Num_screens 
FROM film 
JOIN screening ON screening.film_id = film.film_id 
GROUP BY screening.film_id
HAVING COUNT(screening.film_id) >= 2
ORDER BY screening.film_id ASC;


#Task 3c) 
SELECT full_name, film.genre, AVG(ticket_price) AS Average_price
FROM ticket
JOIN screening ON screening.screening_id = ticket.screening_id
JOIN film ON film.film_id = screening.film_id
GROUP BY full_name, genre;


#Task 3d)
SELECT director, AVG(ticket_price) as Highest_AVGprice
FROM ticket
JOIN screening ON screening.screening_id = ticket.screening_id
JOIN film ON film.film_id = screening.film_id
GROUP BY director
ORDER BY Highest_AVGprice DESC
LIMIT 1;


#Task 3e)
SELECT film.title, showtime, room
FROM screening
JOIN film ON film.film_id = screening.film_id;
