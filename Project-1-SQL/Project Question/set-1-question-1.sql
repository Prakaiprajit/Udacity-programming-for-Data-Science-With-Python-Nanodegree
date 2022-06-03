/* Udacity 1st project: Investigate a Relational Database */

/* QUESTION SET #1 */

/* Question 1: We want to understand more about the movies that families are watching. The following categories are considered family movies: 
Animation, Children, Classics, Comedy, Family and Music.
Create a query that lists each movie, the film category it is classified in, and the number of times it has been rented out.
*/

/*Query 1 */

SELECT DISTINCT film_title,category_name, COUNT(rental_count) rental_count
FROM (SELECT f.title film_title ,c.name category_name,COUNT(r.rental_id) OVER 
(PARTITION BY r.rental_id ORDER BY c.name) AS rental_count
FROM film f
JOIN film_category fc
ON fc.film_id = f.film_id
JOIN category c
ON c.category_id = fc.category_id
JOIN inventory i
ON i.film_id = f.film_id
JOIN rental r 
ON r.inventory_id = i.inventory_id
) sub
WHERE category_name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
GROUP BY 1,2
ORDER BY 2,1;