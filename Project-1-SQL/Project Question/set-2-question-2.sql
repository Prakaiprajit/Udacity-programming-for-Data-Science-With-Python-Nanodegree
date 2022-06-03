/* Udacity 1st project: Investigate a Relational Database */

/* Question Set # 2 */

/* Question 2: We would like to know who were our top 10 paying customers, how many payments they made on a monthly basis during 2007, and 
what was the amount of the monthly payments. Can you write a query to capture the customer name, month and year of payment, and total payment amount 
for each month by these top 10 paying customers?
*/

/*Query 2 */

WITH t1 AS (
		SELECT CONCAT(c.first_name,' ',c.last_name) AS full_name,
		c.customer_id CustomerID, p.amount amount, p.payment_date  
		FROM customer c
		JOIN payment p
		ON p.customer_id = c.customer_id),


  t2 AS (SELECT CustomerID,SUM(amount)
              FROM t1
             GROUP BY 1
             ORDER BY 2 DESC
             LIMIT 10),

  t3 AS (SELECT 
              DATE_TRUNC('month',payment_date) AS payment_month, full_name,
              COUNT (*),
              SUM(amount)
             
         FROM t1
              JOIN t2
               ON t1.CustomerID = t2.CustomerID
        GROUP BY 1, 2
        ORDER BY 1,2)

SELECT t3.*					
  FROM t3
 ORDER BY 2;