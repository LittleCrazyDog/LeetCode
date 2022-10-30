# Write your MySQL query statement below
WITH CTE AS (SELECT employee_id, experience, SUM(salary) OVER(PARTITION BY experience ORDER BY salary ASC) AS RN FROM Candidates)
      
SELECT employee_id FROM CTE WHERE experience = 'Senior' AND RN < 70000
UNION
SELECT employee_id FROM CTE WHERE experience = 'Junior' AND RN < (SELECT 70000 - IFNULL(MAX(RN),0) FROM CTE WHERE experience = 'Senior' AND RN < 70000)