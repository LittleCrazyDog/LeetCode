<h2><a href="https://leetcode.com/problems/find-the-missing-ids/">1613. Find the Missing IDs</a></h2><h3>Medium</h3><hr><div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div><p>Table: <code>Customers</code></p>

<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| customer_name | varchar |
+---------------+---------+
customer_id is the primary key for this table.
Each row of this table contains the name and the id customer.
</pre>

<p>&nbsp;</p>

<p>Write an SQL query to find the missing customer IDs. The missing IDs are ones that are not in the <code>Customers</code> table but are in the range between <code>1</code> and the <strong>maximum</strong> <code>customer_id</code> present in the table.</p>

<p><strong>Notice</strong> that the maximum <code>customer_id</code> will not exceed <code>100</code>.</p>

<p>Return the result table ordered by <code>ids</code> in <strong>ascending order</strong>.</p>

<p>The query result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> 
Customers table:
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
| 1           | Alice         |
| 4           | Bob           |
| 5           | Charlie       |
+-------------+---------------+
<strong>Output:</strong> 
+-----+
| ids |
+-----+
| 2   |
| 3   |
+-----+
<strong>Explanation:</strong> 
The maximum customer_id present in the table is 5, so in the range [1,5], IDs 2 and 3 are missing from the table.
</pre>
</div>