-- ejercicio 1
SELECT firstname, lastname
FROM customers
WHERE country = "Brazil";

--SELECT DISTINCT country
--FROM customers;

-- ejercicio 2
SELECT *
FROM employees
WHERE title = "Sales Support Agent";

SELECT DISTINCT Title
FROM employees;

-- ejercicio 3
/*SELECT * 
FROM tracks
WHERE albumid == 1;

SELECT DISTINCT composer
FROM tracks;

SELECT * FROM artists
WHERE name like "%AC/DC%";

SELECT * FROM albums
WHERE artistid == 1;

SELECT *
FROM tracks
WHERE albumid IN (1,4);*/

SELECT tracks.Name, albums.title, artists.name
FROM tracks 
INNER JOIN albums ON tracks.albumid = albums.AlbumId
INNER JOIN artists ON albums.ArtistId = artists.ArtistId
WHERE artists.artistid = 1;




