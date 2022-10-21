<h2><a href="https://leetcode.com/problems/rectangles-area/">1459. Rectangles Area</a></h2><h3>Medium</h3><hr><div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div><p>Table: <code>Points</code></p>

<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| x_value       | int     |
| y_value       | int     |
+---------------+---------+
id is the primary key for this table.
Each point is represented as a 2D coordinate (x_value, y_value).</pre>

<p>&nbsp;</p>

<p>Write an SQL query to report all possible <strong>axis-aligned</strong> rectangles with a <strong>non-zero area</strong> that can be formed by any two points from the <code>Points</code> table.</p>

<p>Each row in the result should contain three columns <code>(p1, p2, area)</code> where:</p>

<ul>
	<li><code>p1</code> and <code>p2</code> are the <code>id</code>'s of the two points that determine the opposite corners of a rectangle.</li>
	<li><code>area</code> is the area of the rectangle and must be <strong>non-zero</strong>.</li>
</ul>

<p>Return the result table <strong>ordered</strong> by <code>area</code> <strong>in descending order</strong>. If there is a tie, order them by <code>p1</code> <strong>in ascending order</strong>. If there is still a tie, order them by <code>p2</code> <strong>in ascending order</strong>.</p>

<p>The query result format is in the following table.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/12/rect.png" style="width: 303px; height: 500px;">
<pre><strong>Input:</strong> 
Points table:
+----------+-------------+-------------+
| id       | x_value     | y_value     |
+----------+-------------+-------------+
| 1        | 2           | 7           |
| 2        | 4           | 8           |
| 3        | 2           | 10          |
+----------+-------------+-------------+
<strong>Output:</strong> 
+----------+-------------+-------------+
| p1       | p2          | area        |
+----------+-------------+-------------+
| 2        | 3           | 4           |
| 1        | 2           | 2           |
+----------+-------------+-------------+
<strong>Explanation:</strong> 
The rectangle formed by p1 = 2 and p2 = 3 has an area equal to |4-2| * |8-10| = 4.
The rectangle formed by p1 = 1 and p2 = 2 has an area equal to |2-4| * |7-8| = 2.
Note that the rectangle formed by p1 = 1 and p2 = 3 is invalid because the area is 0.
</pre>
</div>