SELECT * 
FROM crime_scene_report
WHERE date = 20180115 AND type="murder" AND city = "SQL City";
--Security footage shows that there were 2 witnesses. The first witness lives at the last house on "Northwestern Dr". The second witness, named Annabel, lives somewhere on "Franklin Ave".

-- 1º Testigo
SELECT i.*
FROM person p
INNER JOIN interview i ON p.id = i.person_id
WHERE p.name LIKE "%Annabel%" AND p.address_street_name = "Franklin Ave";
--I saw the murder happen, and I recognized the killer from my gym when I was working out last week on January the 9th.

-- 2º Testigo
SELECT i.*
FROM person p
INNER JOIN interview i ON p.id = i.person_id
WHERE p.address_street_name = "Northwestern Dr"
AND p.address_number = (SELECT
						MAX(address_number)
						FROM person
						WHERE address_street_name = "Northwestern Dr")
-- I heard a gunshot and then saw a man run out. He had a "Get Fit Now Gym" bag. The membership number on the bag started with "48Z". Only gold members have those bags. The man got into a car with a plate that included "H42W".

SELECT p.*
FROM drivers_license dl
INNER JOIN person p ON p.license_id = dl.id
INNER JOIN get_fit_now_member g ON g.person_id = p.id
WHERE dl.plate_number LIKE "%H42W%" AND dl.gender = "male"
AND g.id LIKE "48Z%" AND g.membership_status = "gold";
-- Jeremy Bowers!!! es el asesino

SELECT * 
FROM get_fit_now_member
WHERE id LIKE "48Z%" AND membership_status = "gold";

SELECT MIN(check_in_date),
MAX(check_in_date)
FROM get_fit_now_check_in


SELECT i.*
FROM drivers_license dl
INNER JOIN person p ON p.license_id = dl.id
INNER JOIN get_fit_now_member g ON g.person_id = p.id
INNER JOIN interview i ON p.id = i.person_id
WHERE dl.plate_number LIKE "%H42W%" AND dl.gender = "male"
AND g.id LIKE "48Z%" AND g.membership_status = "gold";
--I was hired by a woman with a lot of money. I don't know her name but I know she's around 5'5" (65") or 5'7" (67"). She has red hair and she drives a Tesla Model S. I know that she attended the SQL Symphony Concert 3 times in December 2017.

SELECT * 
FROM drivers_license
WHERE hair_color = "red" 
AND car_make = "Tesla" 
AND height BETWEEN 65 AND 67;

SELECT person_id,
COUNT(event_id)
FROM facebook_event_checkin
WHERE date BETWEEN 20171201 AND 20171231
AND event_name LIKE "%SQL Symphony Concert%"
GROUP BY 1
HAVING COUNT(event_id) = 3
--SQL Symphony Concert 3 times in December 2017


SELECT p.* 
FROM drivers_license dl
INNER JOIN person p ON dl.id = p.license_id
INNER JOIN (
  			SELECT person_id,
			COUNT(event_id)
			FROM facebook_event_checkin
			WHERE date BETWEEN 20171201 AND 20171231
			AND event_name LIKE "%SQL Symphony Concert%"
			GROUP BY 1
			HAVING COUNT(event_id) = 3
			) t2 ON p.id = t2.person_id
WHERE dl.hair_color = "red" 
AND dl.car_make = "Tesla" 
AND dl.height BETWEEN 65 AND 67;
