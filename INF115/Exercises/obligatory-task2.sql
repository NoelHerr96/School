#Written by Noel Santillana Herrera

#Task 2a)
CREATE TABLE screening(
Screening_id INT,
film_id INT,
showtime TIME,
room VARCHAR(20),
PRIMARY KEY (screening_id),
FOREIGN KEY (film_id) REFERENCES film(film_id)
);


#Task 2b)
INSERT INTO screening VALUES (1, 20, "09:00:00", "MB04");
INSERT INTO screening VALUES (2, 18, "09:30:00", "MB03");
INSERT INTO screening VALUES (3, 23, "10:30:00", "MB02");
INSERT INTO screening VALUES (4, 12, "10:30:00", "MB05");
INSERT INTO screening VALUES (5, 19, "11:00:00", "MB04");
INSERT INTO screening VALUES (6, 19, "12:00:00", "MB03");
INSERT INTO screening VALUES (7, 24, "12:00:00", "MB05");
INSERT INTO screening VALUES (8, 6, "13:30:00", "MB04");
INSERT INTO screening VALUES (9, 25, "14:00:00", "MB03");
INSERT INTO screening VALUES (10, 11, "16:00:00", "MB01");
INSERT INTO screening VALUES (11, 13, "16:00:00", "MB03");
INSERT INTO screening VALUES (12, 21, "16:00:00", "MB04");
INSERT INTO screening VALUES (13, 12, "16:45:00", "MB05");
INSERT INTO screening VALUES (14, 10, "18:30:00", "MB01");
INSERT INTO screening VALUES (15, 13, "17:00:00", "MB01");
INSERT INTO screening VALUES (16, 23, "17:00:00", "MB02");
INSERT INTO screening VALUES (17, 7, "18:00:00", "MB04");
INSERT INTO screening VALUES (18, 25, "19:15:00", "MB05");
INSERT INTO screening VALUES (19, 22, "20:00:00", "MB03");
INSERT INTO screening VALUES (20, 12, "20:00:00", "MB04");
INSERT INTO screening VALUES (21, 4, "22:00:00", "MB03");
INSERT INTO screening VALUES (22, 14, "21:30:00", "MB02");
INSERT INTO screening VALUES (23, 21, "22:00:00", "MB04");
INSERT INTO screening VALUES (24, 13, "22:00:00", "MB05");
INSERT INTO screening VALUES (25, 3, "22:30:00", "MB01");


#Task 2c)
# i)
ALTER TABLE screening 
ADD CONSTRAINT Opening_hours 
CHECK(showtime > '08:30:00' AND showtime < '23:00:00');

# ii)
ALTER TABLE screening 
ADD CONSTRAINT Festival_screenings 
CHECK(room IN('MB01', 'MB02', 'MB03', 'MB04', 'MB05'));


#Task 2d)
ALTER TABLE film 
ADD CONSTRAINT Unique_name 
UNIQUE (title);

