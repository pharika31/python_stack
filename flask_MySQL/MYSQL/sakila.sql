SELECT customer.first_name, customer.last_name, customer.email, address.address FROM customer 
JOIN address ON customer.address_id = address.address_id 
JOIN city ON city.city_id = address.city_id
where  city.city_id=312;

----------------------
SELECT f.title, f.description, f.release_year, f.rating, f.special_features
FROM film f
JOIN film_category fc ON fc.film_id = f.film_id
JOIN category c ON c.category_id = fc.category_id
WHERE c.name = 'Comedy';

-----------------------
SELECT a.actor_id, CONCAT(a.first_name," ",a.last_name) AS actor_name, f.film_id,f.title, f.description, f.release_year
FROM film f
JOIN film_actor fa ON fa.film_id = f.film_id
JOIN actor a ON a.actor_id = fa.actor_id
WHERE fa.actor_id = 5;

-----------------------
SELECT s.store_id, a.city_id, c.first_name, c.last_name, a.address
FROM customer c 
JOIN store s ON s.store_id=c.store_id
JOIN address a ON a.address_id = c.address_id
WHERE a.city_id IN(1, 42, 312,459) AND s.store_id=1;

------------------------
SELECT f.title, f.description, f.release_year, f.rating,f.special_features
FROM film f
JOIN film_actor fa ON fa.film_id = f.film_id
JOIN actor a ON a.actor_id = fa.actor_id
WHERE fa.actor_id = 15 AND f.special_features LIKE'%behind the scenes%' AND f.rating='G';

------------------------
SELECT f.film_id, f.title, a.actor_id, CONCAT(a.first_name,a.last_name) AS actor_name
FROM film f
JOIN film_actor fa ON fa.film_id = f.film_id
JOIN actor a ON a.actor_id = fa.actor_id
WHERE f.film_id = 369 ;

-------------------------
SELECT f.title, f.description, f.release_year, f.rating, f.special_features, c.name, f.rental_rate
FROM film f
JOIN film_category fc ON fc.film_id = f.film_id
JOIN category c ON c.category_id = fc.category_id
WHERE c.name = 'drama' and f.rental_rate = 2.99;

---------------------------

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, actor.first_name, actor.last_name
FROM actor
	JOIN film_actor ON actor.actor_id = film_actor.actor_id
	JOIN film ON film_actor.film_id = film.film_id
	JOIN film_category ON film.film_id = film_category.film_id
	JOIN category ON film_category.category_id = category.category_id
WHERE actor.first_name = 'Sandra'
	AND actor.last_name = 'Kilmer'
	AND category.name = 'Action';