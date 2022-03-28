#Written by Noel Santillana Herrera

#Task 4a) #Not sure if to use ROUND OR FLOOR on SELECT here.
SELECT ROUND(AVG(age)) AS AverageAge 
FROM volunteer
JOIN volunteer_at_screening ON volunteer.volunteer_id = volunteer_at_screening.volunteer_id
JOIN screening ON screening.Screening_id = volunteer_at_screening.screening_id
JOIN film ON film.film_id = screening.film_id
WHERE genre = 'thriller';


#Task 4b)
SELECT volunteer.volunteer_id AS ID_number, volunteer.full_name AS Name, volunteer.age AS Age, SEC_TO_TIME(SUM(TIME_TO_SEC(film.duration))) AS Highest_Total_time
FROM screening
JOIN film on film.film_id = screening.film_id
JOIN volunteer_at_screening ON volunteer_at_screening.screening_id = screening.screening_id
JOIN volunteer ON volunteer.volunteer_id = volunteer_at_screening.volunteer_id
WHERE country = 'USA'
GROUP BY ID_number
ORDER BY Highest_Total_time DESC
LIMIT 1;


#Task 4c) 
SELECT ticket.full_name, volunteer.full_name, COUNT(*) AS watched_together
FROM screening
JOIN ticket ON screening.Screening_id = ticket.Screening_id
JOIN volunteer_at_screening ON volunteer_at_screening.screening_id = screening.screening_id
JOIN volunteer ON volunteer_at_screening.volunteer_id = volunteer.volunteer_id
JOIN film ON screening.film_id = film.film_id
WHERE film.country = 'France'
GROUP BY ticket.full_name, volunteer.full_name
HAVING watched_together > 1;


#Task 4d)
SELECT screening.showtime, screening.room, film.title
FROM film
JOIN screening ON screening.film_id = film.film_id
JOIN volunteer_at_screening ON volunteer_at_screening.Screening_id = screening.Screening_id
WHERE volunteer_id = 4;
