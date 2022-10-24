-- Write your MySQL query statement below
SELECT name, SUM(amount) balance
FROM transactions
JOIN users on users.account = transactions.account
GROUP BY transactions.account
HAVING SUM(amount) > 10000
