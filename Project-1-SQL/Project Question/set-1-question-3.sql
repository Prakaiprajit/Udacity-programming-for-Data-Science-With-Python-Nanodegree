/* Udacity 1st project: Investigate a Relational Database */

/* QUESTION SET #1 */

/* Question 3:Finally, provide a table with the family-friendly film category, each of the quartiles, and the corresponding count of movies within each combination of film category 
for each corresponding rental duration category. The resulting table should have three columns:

- Category
- Rental length category
- Count 
*/

/*Query 3 */

SELECT category_name,standard_quartile,COUNT(standard_quartile)
FROM (SELECT c.name category_name ,NTILE(4) OVER (ORDER BY f.rental_duration)
 AS standard_quartile
FROM film f
JOIN film_category fc
ON fc.film_id = f.film_id
JOIN category c
ON c.category_id = fc.category_id
WHERE c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')) sub
GROUP BY 1,2
ORDER BY 1,2;