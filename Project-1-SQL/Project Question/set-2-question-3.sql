/* Udacity 1st project: Investigate a Relational Database */

/* Question Set # 2 */

/* Question 3: Finally, for each of these top 10 paying customers, I would like to find out the difference across their monthly payments during 2007. 
Please go ahead and write a query to compare the payment amounts in each successive month. Repeat this for each of these 10 paying customers. 
Also, it will be tremendously helpful if you can identify the customer name who paid the most difference in terms of payments.
*/


/*Query 3 */

WITH table1 AS (
		SELECT CONCAT(c.first_name,' ',c.last_name) AS full_name,
		c.customer_id CustomerID, p.amount amount, p.payment_date  
		FROM customer c
		JOIN payment p
		ON p.customer_id = c.customer_id),


  table2 AS (SELECT CustomerID,SUM(amount)
              FROM table1
             GROUP BY 1
             ORDER BY 2 DESC
             LIMIT 10),

  table3 AS (SELECT 
              DATE_TRUNC('month',payment_date) AS payment_month, full_name,
              COUNT (*),
              SUM(amount),
	LEAD(SUM(amount)) OVER (PARTITION BY full_name ORDER BY 
	DATE_TRUNC('month',payment_date)) AS lead,
	LEAD(SUM(amount)) OVER (PARTITION BY full_name ORDER BY 
	DATE_TRUNC('month',payment_date)) - SUM(amount) AS lead_different    
         FROM table1
              JOIN table2
               ON table1.CustomerID = table2.CustomerID
        GROUP BY 1,2
        ORDER BY 2,1
	)

SELECT table3.*,
	CASE
	WHEN lead_different = (SELECT MAX(lead_different) FROM
table3 ORDER BY 1 DESC LIMIT 1) THEN 'maximum difference'
	ELSE NULL
	END AS MAX					
  FROM table3
 ORDER BY 1;