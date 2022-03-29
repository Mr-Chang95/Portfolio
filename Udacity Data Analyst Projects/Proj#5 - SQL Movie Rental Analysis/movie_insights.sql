/* Query #1: query used for 1st insight */
/* Qestion: Who were the top 10 most-rented actor of 2006?*/
WITH table_1 AS (SELECT  f.title AS film_title, 
				 CONCAT(a.first_name,' ',a.last_name) AS actor_name,
				 r.rental_date AS rental_date, 
				 DATE_PART('year', r.rental_date) AS year
					 FROM actor a
					 JOIN film_actor fa ON a.actor_id = fa.actor_id
					 JOIN film f ON fa.film_id = f.film_id
					 JOIN inventory i ON f.film_id = i.film_id
					 JOIN rental r ON i.inventory_id = r.inventory_id)

SELECT actor_name, COUNT(actor_name) AS actor_count
  FROM table_1
  WHERE year = 2006
  GROUP BY 1
  ORDER BY 2 DESC
  LIMIT 10;
  
/* Query #2: query used for 2nd insight */
/* How many rentals are missing from each category at the Woodridge store?*/
WITH table_1 AS (SELECT c.city AS city_name,
				 r.rental_date AS rental_day,
				 f.title AS film_title, ca.name As category_name,
				 r.return_date AS rental_return
					 FROM city c
					 JOIN address a ON c.city_id = a.city_id
					 JOIN staff s ON a.address_id = s.address_id
					 JOIN payment p ON s.staff_id = p.staff_id
					 JOIN rental r ON p.rental_id =r.rental_id
					 JOIN inventory i ON r.inventory_id = i.inventory_id
					 JOIN film f ON i.film_id = f.film_id
					 JOIN film_category fc ON f.film_id = fc.film_id
					 JOIN category ca ON fc.category_id = ca.category_id)

SELECT category_name, COUNT(rental_day) - COUNT(rental_return) AS missing_rental_count
	FROM table_1
	WHERE city_name = 'Woodridge'
	GROUP BY category_name
	ORDER BY missing_rental_count DESC;

/* Query #3: query used for 3rd insight */
/*  How much did the top 20 districts each spend?*/
SELECT DISTINCT(district), SUM(total_sum) OVER(PARTITION BY district) AS district_total
	FROM (
		SELECT CONCAT(c.first_name,' ',c.last_name) AS full_name,
			SUM(p.amount) AS total_sum, a.district AS district
		FROM address a
		JOIN customer c ON a.address_id = c.address_id
		JOIN payment p ON c.customer_id = p.customer_id
		JOIN rental r On p.rental_id = r.rental_id
		GROUP BY 1, 3
		ORDER BY 3) table_1
	ORDER BY 2 DESC
	LIMIT 20;

/* Query #4: query used for 4th insight */
/*  For the 15 top-spending district, by how much are
they outperforming the preceding district?*/
WITH table_1 AS (SELECT CONCAT(c.first_name,' ',c.last_name) AS full_name,
				 COUNT(r.rental_date) As rental_count,
				 SUM(p.amount) AS total_sum, a.district AS district
				 	FROM address a
				 	JOIN customer c ON a.address_id = c.address_id
				 	JOIN payment p ON c.customer_id = p.customer_id
				 	JOIN rental r ON p.rental_id = r.rental_id
				 	GROUP BY 1, 4
				 	ORDER BY 2 DESC),
	table_2 AS (SELECT DISTINCT (district),
				SUM(total_sum) OVER (PARTITION BY district) AS district_total
					FROM table_1
					ORDER BY 2 DESC)

SELECT district, district_total,
district_total - LEAD(district_total) OVER (ORDER BY district_total DESC) AS difference
    FROM table_2
    ORDER BY district_total DESC
    LIMIT 15;  