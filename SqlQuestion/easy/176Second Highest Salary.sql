Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

# Write your MySQL query statement below
SELECT max(Salary) as SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT max(Salary) FROM Employee)

Employee
  Id	Salary
0	1	100
1	2	200
2	3	300

Output
{"headers": ["SecondHighestSalary"], "values": [[200]]}

another answer:
SELECT (CASE 
        WHEN (SELECT COUNT(DISTINCT Salary) FROM Employee) < 2 
        THEN NULL 
        ELSE (SELECT Salary FROM Employee 
              ORDER BY Salary DESC LIMIT 1,1) 
        END) AS SecondHighestSalary
